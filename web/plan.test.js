// node web/plan.test.js
const assert = require('assert');
const { planDive, makeDepthAt, legs, simplify } = require('./plan.js');

// simplificació: un zig-zag suau cap al nord queda en un sol rumb; un gir de 90° es manté
const zig = [{ x: 0, y: 0 }, { x: 2, y: 20 }, { x: -2, y: 40 }, { x: 1, y: 60 }, { x: 40, y: 60 }, { x: 80, y: 62 }];
assert.deepStrictEqual(simplify(zig, 20), [0, 3, 5]);
assert.deepStrictEqual(simplify(zig, 3), [0, 1, 2, 3, 5]);
assert.deepStrictEqual(simplify(zig.slice(0, 2), 20), [0, 1]);
// corba suau: cap gir supera 20° per si sol, però l'acumulat respecte a l'últim punt mantingut sí
const arc = Array.from({ length: 10 }, (_, i) => ({ x: 100 * Math.sin(i * Math.PI / 18), y: 100 * Math.cos(i * Math.PI / 18) }));
assert.ok(simplify(arc, 20).length > 2 && simplify(arc, 20).length < arc.length, 'corba: alguns girs');

// rumbs: nord = 0°, est = 90°, sud-oest = 225°
const L = legs([{ x: 0, y: 0 }, { x: 0, y: 10 }, { x: 10, y: 10 }, { x: 0, y: 0 }]);
assert.deepStrictEqual(L.map(l => Math.round(l.bearing)), [0, 90, 225]);
assert.deepStrictEqual(L.map(l => l.card), ['N', 'E', 'SO']);
assert.ok(Math.abs(L[2].dist - Math.hypot(10, 10)) < 1e-9 && L[0].from === 1 && L[0].to === 2);
assert.strictEqual(legs([{ x: 0, y: 0 }, { x: -1, y: 1 }])[0].card, 'NO');

const o = { sac: 20, vol: 15, p0: 200, reserve: 50, speed: 10, descRate: 18, ascRate: 9, offset: 0, step: 2,
  stopDepth: 5, stopTime: 3, stopMinDepth: 10 };
const flat = () => 20; // fons pla a 20 m

// 200 m a 20 m de fons, a 10 m/min: ~20 min de fons a 3 bar -> ~1200 L
const r = planDive([{ x: 0, y: 0, depth: 20 }, { x: 200, y: 0, depth: 20 }], o, flat);
const s = r.summary;
assert.ok(Math.abs(s.dist - 200) < 1e-6, 'distància');
assert.strictEqual(s.maxDepth, 20);
assert.ok(s.safetyStop, 'parada de seguretat a >= 10 m');
// descens 20/18 min*2 bar*20 = 44.4 + fons 20*3*20 = 1200 + ascens 20->5 a 9 m/min (2.25 bar) = 75
// + parada 3*1.5*20 = 90 + 5->0 (1.25 bar) = 13.9  => 1423.3 L
assert.ok(Math.abs(s.gas - 1423.33) < 0.1, `gas ${s.gas}`);
assert.ok(Math.abs(s.endP - (200 - s.gas / 15)) < 1e-9, 'pressió = P0 - gas/V');
assert.ok(s.reserveAt === null, 'no arriba a reserva');
assert.strictEqual(r.samples[r.samples.length - 1].depth, 0, 'acaba a superfície');

// acabant a 4 m després d'anar a 20 m, la parada de 3 min es fa igualment (a 4 m)
const shoreEnd = planDive([{ x: 0, y: 0, depth: 20 }, { x: 100, y: 0, depth: 4 }], o, flat);
const atStop = shoreEnd.samples.filter((p, i, a) => i && p.depth === 4 && a[i - 1].depth === 4);
assert.ok(atStop.some(p => Math.abs(p.t - shoreEnd.samples[shoreEnd.samples.indexOf(p) - 1].t - 3) < 1e-9), 'parada en sortir per costa');

// el bussejador no pot quedar per sota del fons: demana 30 m sobre un fons de 20 m
const deep = planDive([{ x: 0, y: 0, depth: 30 }, { x: 50, y: 0, depth: 30 }], o, flat);
assert.ok(deep.samples.every(p => p.depth <= 20 + 1e-9), 'segueix el fons');

// ampolla petita -> toca reserva
const small = planDive([{ x: 0, y: 0, depth: 20 }, { x: 400, y: 0, depth: 20 }], { ...o, vol: 10 }, flat);
assert.ok(small.summary.reserveAt && small.summary.reserveAt.t > 0, 'arriba a reserva');

// interpolació bilineal sobre una graella 2x2 (elevacions negatives = profunditat)
const site = { xmin: 0, ymax: 2, res: 1, w: 2, h: 2 };
const dAt = makeDepthAt(site, new Float32Array([-10, -20, -10, -20]));
assert.ok(Math.abs(dAt(1, 1) - 15) < 1e-6, 'bilineal');
assert.strictEqual(makeDepthAt(site, new Float32Array([NaN, 5, NaN, 5]))(0.5, 1.5), 0, 'terra/NaN -> 0');
console.log('ok', s.time.toFixed(1), 'min', s.gas.toFixed(0), 'L', s.endP.toFixed(0), 'bar');
