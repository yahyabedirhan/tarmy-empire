import json,sys,glob,os
f=sys.argv[1] if len(sys.argv)>1 else max(glob.glob(os.path.expanduser('~/.claude/projects/-home-yabepa-tarmy-empire/*/tool-results/mcp-commander-empire_overview-*.txt')),key=os.path.getmtime)
raw=open(f).read()
try: o=json.loads(raw)
except: o=json.loads(json.loads(raw)[0]['text'])
if isinstance(o,list): o=json.loads(o[0]['text'])
for p in o['planet_detail']:
    pr=p['production']; b=p['buildings']
    caps=[p['metal']/pr['storage_cap_metal'],p['crystal']/pr['storage_cap_crystal'],p['deuterium']/pr['storage_cap_deuterium']]
    flag=' CAP!' if max(caps)>=0.8 else ''
    q=[(x['item_key'],x.get('target_level',x.get('count')),x['finished_at'][11:19]) for x in p['build_queue']]
    print(f"{p['name']:<16} M{p['metal']/1000:6.0f}k C{p['crystal']/1000:5.0f}k D{p['deuterium']/1000:5.0f}k  E+{pr['energy_produced']-pr['energy_used']:<5} C/h {pr['crystal_per_hour']:6.0f} F{p['fields_used']}/{p['fields_total']}{flag}  cm{b.get('crystal_mine',0)} mm{b.get('metal_mine',0)} rob{b.get('robotics_factory',0)} sy{b.get('shipyard',0)}  def={ {k:v for k,v in p.get('defense',{}).items()} }  ships={ {k:v for k,v in p.get('ships',{}).items() if v} }")
    for x in q: print('    q',x)
print('fleets_out', [(x['id'],x['mission'],x['target_position'],x['arrival_at'][11:19]) for x in o.get('fleets_out',[])])
print('quests ready', o['quests'].get('ready'))
