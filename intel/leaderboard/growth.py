#!/usr/bin/env python3
"""Compare two leaderboard snapshots: score/day per player, top climbers, our band.

usage: growth.py [OLD.json NEW.json]   (default: the two newest in this directory)
"""
import json, sys, glob, os
from datetime import datetime
here = os.path.dirname(os.path.abspath(__file__))
files = sorted(glob.glob(os.path.join(here, '*.json')))
old, new = (sys.argv[1], sys.argv[2]) if len(sys.argv) == 3 else (files[-2], files[-1])
def load(p):
    d = json.load(open(p)); t = datetime.strptime(d['taken_at'], '%Y-%m-%dT%H:%MZ')
    return t, {r['username']: r for r in d['players']}
t0, a = load(old); t1, b = load(new)
days = (t1 - t0).total_seconds() / 86400 or 1e-9
rows = []
for u, r in b.items():
    if u in a:
        d = r['score'] - a[u]['score']
        rows.append((d / days, d, r['rank'], a[u]['rank'], u, r['score'], r.get('alliance') or ''))
rows.sort(reverse=True)
print(f"{old.split('/')[-1]} → {new.split('/')[-1]}  ({days:.2f} d)\n")
def line(x): print(f"{x[2]:>4} ({x[3]:>4})  {x[4]:<18} {x[6]:<7} {x[5]:>8}  +{x[1]:>7}  {x[0]:>9.0f}/d")
print("rank (was)  player             ally    score      Δ        score/day")
print("── top 15 climbers ──"); [line(x) for x in rows[:15]]
me = [x for x in rows if x[4] == 'yabepa']
if me:
    i = rows.index(me[0]); print(f"\n── us: growth rank {i+1}/{len(rows)} ──"); line(me[0])
    band = sorted([x for x in rows if abs(x[2] - me[0][2]) <= 10], key=lambda x: x[2])
    print("── our band (±10 ranks) ──"); [line(x) for x in band]
