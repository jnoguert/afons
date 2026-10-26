// Càlcul del perfil i del consum d'aire d'una immersió planificada.
// Script clàssic (sense mòduls) perquè funcioni obrint planner.html des del disc; també es pot fer require() des de node.

// Profunditat del fons (m, positiva cap avall) per interpolació bilineal. NaN o terra -> 0.
function makeDepthAt(site, elev) {
  return function depthAt(x, y) {
    const c = (x - site.xmin) / site.res - 0.5, r = (site.ymax - y) / site.res - 0.5;
    const c0 = Math.max(0, Math.min(site.w - 2, Math.floor(c))), r0 = Math.max(0, Math.min(site.h - 2, Math.floor(r)));
    const fx = Math.min(1, Math.max(0, c - c0)), fy = Math.min(1, Math.max(0, r - r0));
    const at = (rr, cc) => { const v = elev[rr * site.w + cc]; return Number.isFinite(v) ? Math.max(0, -v) : 0; };
    return (at(r0, c0) * (1 - fx) + at(r0, c0 + 1) * fx) * (1 - fy) + (at(r0 + 1, c0) * (1 - fx) + at(r0 + 1, c0 + 1) * fx) * fy;
  };
}

// waypoints: [{x, y, depth}] on depth és la profunditat objectiu del bussejador (m).
// Entre punts la profunditat s'interpola i mai baixa per sota de (fons - offset): segueix el relleu.
// Retorna mostres {t (min), dist (m), x, y, depth, bottom, gas (L consumits), p (bar)} i un resum.
function planDive(waypoints, o, depthAt) {
  const S = [];
  if (!waypoints.length) return { samples: S, summary: null };
  let t = 0, dist = 0, gas = 0;
  const push = (x, y, depth, dt, dd) => {
    const prev = S[S.length - 1];
    if (prev) gas += o.sac * (1 + (prev.depth + depth) / 20) * dt; // pressió absoluta mitjana del tram
    t += dt; dist += dd;
    S.push({ t, dist, x, y, depth, bottom: depthAt(x, y), gas, p: o.p0 - gas / o.vol });
  };
  const vt = (d0, d1) => (d1 > d0 ? (d1 - d0) / o.descRate : (d0 - d1) / o.ascRate); // minuts verticals
  const clampD = (x, y, d) => Math.max(0, Math.min(d, depthAt(x, y) - o.offset));

  const w0 = waypoints[0];
  push(w0.x, w0.y, 0, 0, 0); // superfície al primer punt
  for (let d = 1; d <= clampD(w0.x, w0.y, w0.depth); d++) push(w0.x, w0.y, d, 1 / o.descRate, 0);
  const d0 = clampD(w0.x, w0.y, w0.depth);
  if (S[S.length - 1].depth < d0) push(w0.x, w0.y, d0, vt(S[S.length - 1].depth, d0), 0);

  for (let i = 1; i < waypoints.length; i++) {
    const a = waypoints[i - 1], b = waypoints[i];
    const L = Math.hypot(b.x - a.x, b.y - a.y), n = Math.max(1, Math.ceil(L / o.step));
    for (let k = 1; k <= n; k++) {
      const f = k / n, x = a.x + (b.x - a.x) * f, y = a.y + (b.y - a.y) * f;
      const d = clampD(x, y, a.depth + (b.depth - a.depth) * f);
      const prev = S[S.length - 1];
      push(x, y, d, Math.max(L / n / o.speed, vt(prev.depth, d)), L / n); // nedar i pujar/baixar alhora
    }
  }

  const last = S[S.length - 1];
  const maxDepth = Math.max(...S.map(s => s.depth));
  const stop = o.stopTime > 0 && maxDepth >= o.stopMinDepth ? o.stopDepth : 0;
  for (let d = Math.floor(last.depth); d > stop; d--) if (d < last.depth) push(last.x, last.y, d, vt(S[S.length - 1].depth, d), 0);
  if (stop) { // si ja ets més amunt de la cota de parada, la fas on ets
    const sd = Math.min(stop, last.depth);
    if (S[S.length - 1].depth !== sd) push(last.x, last.y, sd, vt(S[S.length - 1].depth, sd), 0);
    push(last.x, last.y, sd, o.stopTime, 0);
  }
  push(last.x, last.y, 0, vt(S[S.length - 1].depth, 0), 0);

  const reserveAt = S.find(s => s.p <= o.reserve) || null;
  let area = 0;
  for (let i = 1; i < S.length; i++) area += (S[i].depth + S[i - 1].depth) / 2 * (S[i].t - S[i - 1].t);
  return {
    samples: S,
    summary: { time: t, dist, maxDepth, avgDepth: t ? area / t : 0, gas, endP: o.p0 - gas / o.vol, reserveAt, safetyStop: !!stop },
  };
}

// Mostra a l'instant t (min), per al cursor de reproducció.
function sampleAt(samples, t) {
  let i = samples.findIndex(s => s.t >= t);
  if (i <= 0) return samples[Math.max(0, i)];
  const a = samples[i - 1], b = samples[i], f = b.t > a.t ? (t - a.t) / (b.t - a.t) : 1;
  const lerp = k => a[k] + (b[k] - a[k]) * f;
  return { t, x: lerp('x'), y: lerp('y'), depth: lerp('depth'), bottom: lerp('bottom'), p: lerp('p'), gas: lerp('gas'), dist: lerp('dist') };
}

// Rumb (graus des del nord, en sentit horari) i distància de cada tram entre punts.
// Coordenades UTM: el nord de quadrícula difereix del geogràfic menys de 0,2° a la costa catalana.
const RUMBS = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSO', 'SO', 'OSO', 'O', 'ONO', 'NO', 'NNO'];
function legs(wps) {
  return wps.slice(1).map((b, i) => {
    const a = wps[i], dx = b.x - a.x, dy = b.y - a.y, bearing = (Math.atan2(dx, dy) * 180 / Math.PI + 360) % 360;
    return { from: i + 1, to: i + 2, bearing, card: RUMBS[Math.round(bearing / 22.5) % 16], dist: Math.hypot(dx, dy) };
  });
}

if (typeof module !== 'undefined') module.exports = { makeDepthAt, planDive, sampleAt, legs };
