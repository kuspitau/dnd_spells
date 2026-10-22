#!/usr/bin/env python3
"""Construit la bibliothèque de démonstration à partir des transcriptions dans spells_data.py.
Usage: python build_library.py
Dépendances: pyyaml, markdown-it-py, Pillow, playwright/chromium pour les JPG.
"""
import csv, html, json, re, unicodedata
from pathlib import Path
from PIL import Image
import yaml
from markdown_it import MarkdownIt
from spells_data import SPELLS
import spells_lot2  # ajoute les transcriptions du deuxième lot

ROOT=Path(__file__).resolve().parent
# Lot automatique ajouté sans modifier les 29 transcriptions historiques.
auto_file=ROOT/'spells_auto.json'
if auto_file.exists():
 SPELLS.extend(json.loads(auto_file.read_text(encoding='utf-8')))
for folder in ['md','fiches_html','fiches_jpg','illustrations']:
 (ROOT/folder).mkdir(parents=True,exist_ok=True)
md=MarkdownIt('commonmark',{'html':False}).enable('table')


def slug(name):
 text=unicodedata.normalize('NFKD',name)
 text=''.join(c for c in text if not unicodedata.combining(c))
 return re.sub(r'[^a-z0-9]+','-',text.lower()).strip('-')

# Illustrations: elles restent distinctes de la transcription du sort.
illustration_regions={
 'familiers.jpg':(243,(0.09,0.04,0.94,0.45)),
 'arme-spirituelle.jpg':(244,(0.04,0.02,0.96,0.47)),
 'armure-du-mage.jpg':(245,(0.02,0.01,0.96,0.48)),
}
for filename,(page,bounds) in illustration_regions.items():
 im=Image.open(ROOT/'source'/f'page_{page}.jpeg').convert('RGB')
 w,h=im.size
 piece=im.crop(tuple(round(v*(w if i%2==0 else h)) for i,v in enumerate(bounds)))
 if piece.width>1450:piece.resize((1450,round(piece.height*1450/piece.width)),Image.Resampling.LANCZOS).save(ROOT/'illustrations'/filename,quality=90,subsampling=0,optimize=True)
 else:piece.save(ROOT/'illustrations'/filename,quality=90,optimize=True)

CSS='''
:root{--ink:#253042;--muted:#626c79;--accent:#5a466c;--rule:#d7d4ce;--soft:#f7f5f1;--paper:#fffefa}
*{box-sizing:border-box} html{color-scheme:light} body{margin:0;font-family:Arial,Helvetica,sans-serif;color:var(--ink);background:#e9e6e0;line-height:1.48}
.card{max-width:760px;margin:26px auto 40px;background:var(--paper);border:1px solid var(--rule);box-shadow:0 4px 26px #25232316;padding:38px 44px;border-radius:4px}
.kicker{font-size:11px;letter-spacing:1.9px;font-weight:700;text-transform:uppercase;color:var(--accent);margin:0 0 9px}
h1{font-family:Georgia,'Times New Roman',serif;font-size:34px;line-height:1.12;letter-spacing:-.5px;color:#272631;margin:0 0 6px;font-weight:600}
.subtitle{font-family:Georgia,'Times New Roman',serif;font-size:15px;color:var(--muted);font-style:italic;margin-bottom:22px}
.meta{border-block:1px solid var(--rule);padding:13px 0;display:grid;grid-template-columns:1fr 1fr;column-gap:24px;row-gap:10px;margin-bottom:25px}
.meta-item{min-width:0}.meta-label{font-size:10px;letter-spacing:.9px;text-transform:uppercase;color:var(--muted);font-weight:700;margin-bottom:1px}
.meta-value{font-size:14px;font-weight:500;overflow-wrap:anywhere}
.body{font-family:Georgia,'Times New Roman',serif;font-size:16px;line-height:1.57;color:#292a2d}
.body p{margin:0 0 14px}.body h2{font-size:21px;line-height:1.2;border-bottom:1px solid var(--rule);padding-bottom:7px;margin:28px 0 14px;color:var(--accent)}
.body h3{font-family:Arial,Helvetica,sans-serif;font-size:13px;text-transform:uppercase;letter-spacing:1.15px;color:var(--accent);margin:22px 0 8px}
.body strong{font-weight:700}.body em{font-style:italic}
.body table{width:100%;border-collapse:collapse;font-family:Arial,Helvetica,sans-serif;font-size:13px;margin:16px 0 24px}
.body th{text-align:left;background:#eeeaf0;color:#40394b;padding:9px 11px;border-bottom:2px solid #b5a7bf}
.body td{padding:7px 11px;border-bottom:1px solid #dedbd8}.body tr:nth-child(even) td{background:#f5f2f1}.body td:not(:first-child):where(.body table td){text-align:left}
.art{margin:22px 0 25px}.art img{width:100%;max-height:230px;object-fit:cover;object-position:center;border-radius:3px;display:block}.art figcaption{font:italic 12px Georgia,serif;color:var(--muted);padding-top:7px}
.footer{border-top:1px solid var(--rule);margin-top:28px;padding-top:12px;font:11px Arial,sans-serif;color:var(--muted);display:flex;justify-content:space-between}
@media screen and (max-width:660px){.card{margin:0;box-shadow:none;padding:27px 22px;border:0}.meta{column-gap:12px}.body{font-size:15px}h1{font-size:29px}}
@media print{@page{size:A4;margin:13mm 13mm}body{background:#fff}.card{box-shadow:none;border:0;padding:0;margin:0;max-width:none}.art img{max-height:105px}.body{font-size:11pt}.meta{margin-bottom:15px}.body p{margin-bottom:10px}.body h2,.body h3,.body table,.art{break-inside:avoid}.body h2,.body h3{break-after:avoid}.card[data-spell="appel-de-destrier"] .body h2{break-before:page}}
'''
CSS += '\n.source-links{font:12px Arial,sans-serif;color:#5f5867;margin-top:22px}.source-links a{color:#5a466c;margin-right:10px}\n'
(ROOT/'styles.css').write_text(CSS,encoding='utf-8')

def page_html(s,artref):
 cover=f'<figure class="art"><img src="{artref}" alt="Illustration associée au sort"><figcaption>{html.escape(s["legende_illustration"] or "")}</figcaption></figure>' if artref else ''
 return f'''<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(s['nom'])} | Bibliothèque de sorts</title><link rel="stylesheet" href="../styles.css"></head><body>
<main class="card" id="spell-card" data-spell="{s['id']}"><div class="kicker">Bibliothèque de sorts · D&amp;D 2024</div><h1>{html.escape(s['nom'])}</h1><div class="subtitle">{html.escape(s['ecole'])} {"mineure" if s['niveau']==0 else 'du '+('1er' if s['niveau']==1 else str(s['niveau'])+'e')+' niveau'} ({html.escape(', '.join(s['classes']))})</div>
<div class="meta"><div class="meta-item"><div class="meta-label">Temps d'incantation</div><div class="meta-value">{html.escape(s['incantation'])}</div></div><div class="meta-item"><div class="meta-label">Portée</div><div class="meta-value">{html.escape(s['portee'])}</div></div><div class="meta-item"><div class="meta-label">Composantes</div><div class="meta-value">{html.escape(s['composantes'])}</div></div><div class="meta-item"><div class="meta-label">Durée</div><div class="meta-value">{html.escape(s['duree'])}</div></div></div>
{cover}<article class="body">{md.render(s['description'])}</article><nav class="source-links">Consulter le scan original : {' · '.join('<a href="../source_pages/page_'+str(p)+'.jpg">p. '+str(p)+'</a>' for p in s['pages_source'] if (ROOT/'source_pages'/('page_'+str(p)+'.jpg')).exists())}</nav><footer class="footer"><span>Source : Manuel des joueurs, p. {', '.join(str(x) for x in s['pages_source'])}</span><span>{'OCR à vérifier — valeurs non certifiées' if s['statut']=='ocr_non_valide' else 'Transcription du prototype relue'}</span></footer></main></body></html>'''

rows=[]
for s in SPELLS:
 s['id']=slug(s['nom'])
 fm={k:s[k] for k in ['nom','ecole','niveau','classes','incantation','portee','composantes','duree','pages_source','statut']}
 if s['illustration']:fm['illustration']='../illustrations/'+s['illustration'];fm['legende_illustration']=s['legende_illustration']
 text='---\n'+yaml.safe_dump(fm,allow_unicode=True,sort_keys=False,width=100)+'---\n\n# '+s['nom']+'\n\n'+s['description']+'\n'
 if s['statut']=='ocr_non_valide':
  text+='\n---\n\n> **Transcription OCR non validée.** Les valeurs et passages complexes sont à contrôler sur les scans ci-dessous.\n'
  if s.get('notes_verification'): text+='\n**Anomalies détectées :** '+s['notes_verification']+'\n'
  text+='\n## Pages sources\n\n'+'\n'.join(f'- [Page {p}](../source_pages/page_{p}.jpg)' for p in s['pages_source'])+'\n'
 if s['illustration']:
  text+='\n## Illustration associée (distincte du texte du sort)\n\n!['+s['legende_illustration']+'](../illustrations/'+s['illustration']+')\n\n*'+s['legende_illustration']+'*\n'
 (ROOT/'md'/f'{s["nom"].replace(chr(47),"-")}.md').write_text(text,encoding='utf-8')
 (ROOT/'fiches_html'/f'{s["nom"].replace(chr(47),"-")}.html').write_text(page_html(s,'../illustrations/'+s['illustration'] if s['illustration'] else ''),encoding='utf-8')
 rows.append({'sort':s['nom'],'pages':','.join(str(n) for n in s['pages_source']),'statut':s['statut'],
     'type_cas':'encadre_statistiques' if '## Monture' in s['description'] else 'tableau' if s['nom']=='Augure' else 'continuation_multi_pages' if len(s['pages_source'])>1 else 'standard',
     'a_verifier':'Relecture exhaustive des valeurs et ponctuation conseillée; corrections sur les images sources.'})

with (ROOT/'controle_extraction.csv').open('w',encoding='utf-8-sig',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
(ROOT/'index.json').write_text(json.dumps([{k:v for k,v in s.items() if k not in ['notes_verification']} for s in SPELLS],ensure_ascii=False,indent=2),encoding='utf-8')

# Index interactif local: prévisualisation au survol, recherche/filtres, lien vers la fiche complète.
JSON=json.dumps([{**s,'html_body':md.render(s['description'])} for s in SPELLS],ensure_ascii=False).replace('</','<\\/')
INDEX_CSS='''
:root{font-family:Arial,sans-serif;color:#242831;background:#f3f1ed}*{box-sizing:border-box}
body{max-width:1180px;margin:0 auto;padding:32px 24px}header{margin:0 0 24px}h1{margin:0 0 6px;font:normal 36px Georgia,serif}header p{color:#62676e;margin:0}
.controls{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 16px}.controls input,.controls select{background:white;border:1px solid #c8c8c9;border-radius:5px;padding:10px;font:14px Arial;min-width:160px}.controls input{flex:1;min-width:230px}
.count{font-size:12px;letter-spacing:.4px;color:#656771;padding:8px 0}
.tablewrap{background:#fff;border:1px solid #dad7d3;border-radius:7px;overflow:visible}table{width:100%;border-collapse:collapse}th{text-align:left;background:#efede9;color:#5f6166;font-size:12px;letter-spacing:.5px;padding:13px 15px;text-transform:uppercase}td{border-top:1px solid #eceae6;padding:13px 15px;font-size:14px}tbody tr:hover{background:#f7f5f9}.spellname a{font-weight:700;color:#423754;text-decoration:none}.spellname a:hover{text-decoration:underline}.subtext{color:#7b7980;font-size:12px;margin-top:3px}
.chip{display:inline-block;border:1px solid #dad6e0;color:#554761;background:#f7f4fa;border-radius:20px;font-size:12px;padding:3px 8px}
.spellname{position:relative}.tooltip{display:none;z-index:50;position:absolute;left:calc(100% - 8px);top:-20px;width:420px;max-height:450px;overflow:auto;box-shadow:0 10px 42px #0002;border:1px solid #dcd7dd;background:#fffdfa;border-radius:7px;padding:18px 21px;font:14px Georgia,serif;line-height:1.45;pointer-events:auto}.spellname:hover .tooltip{display:block}.tooltip h3{font:normal 20px Georgia,serif;margin:0 0 6px;color:#473953}.tooltip p{margin:0 0 9px}.tooltip .small{font:12px Arial;color:#666;margin-bottom:12px}.tooltip table{font:12px Arial}.tooltip th,.tooltip td{padding:4px 6px}.tooltip h2{font-size:16px}.tooltip h3:not(:first-child){font-size:14px}
@media(max-width:830px){.tooltip{display:none!important}body{padding:16px 10px}td,th{padding:11px 7px}.hide-small{display:none}}
'''
html_index=f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Bibliothèque de sorts · Prototype</title><style>{INDEX_CSS}</style></head><body><header><h1>Bibliothèque de sorts</h1><p>Bibliothèque locale · {len(SPELLS)} sorts · pages sources 239 à 343 · Survol : aperçu · Clic : fiche détaillée</p></header><section class="controls"><input id="search" type="search" placeholder="Rechercher un sort, une école ou un terme…" aria-label="Rechercher"><select id="class"><option value="">Toutes les classes</option></select><select id="level"><option value="">Tous les niveaux</option></select><select id="school"><option value="">Toutes les écoles</option></select></section><div class="count" id="count"></div><div class="tablewrap"><table><thead><tr><th>Sort</th><th>Niveau</th><th class="hide-small">École</th><th class="hide-small">Incantation</th><th>Portée</th></tr></thead><tbody id="items"></tbody></table></div><script>
const spells={JSON};
const el=id=>document.getElementById(id);const esc=s=>String(s).replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));
function options(id,values){{for(const v of values.sort((a,b)=>String(a).localeCompare(String(b),'fr'))){{const o=document.createElement('option');o.value=v;o.textContent=v;el(id).append(o)}}}}
options('class',[...new Set(spells.flatMap(x=>x.classes))]);options('level',[...new Set(spells.map(x=>String(x.niveau)))].sort((a,b)=>+a-+b));options('school',[...new Set(spells.map(x=>x.ecole))]);
function norm(s){{return String(s).normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase()}}
function render(){{const q=norm(el('search').value), cl=el('class').value, lvl=el('level').value, sch=el('school').value;
const list=spells.filter(s=>(!q||norm([s.nom,s.ecole,s.classes.join(' '),s.description].join(' ')).includes(q))&&(!cl||s.classes.includes(cl))&&(!lvl||String(s.niveau)===lvl)&&(!sch||s.ecole===sch));
el('count').textContent=list.length+' sort'+(list.length>1?'s':'')+' affiché'+(list.length>1?'s':'');
el('items').innerHTML=list.map(s=>`<tr><td class="spellname"><a href="fiches_html/${{encodeURIComponent(s.nom.replaceAll('/', '-'))}}.html">${{esc(s.nom)}}</a><div class="subtext">${{esc(s.classes.join(', '))}}${{s.statut==='ocr_non_valide'?' · OCR à contrôler':''}}</div><div class="tooltip"><h3>${{esc(s.nom)}}</h3><p class="small">${{esc(s.ecole)}} · Niveau ${{s.niveau}} · ${{esc(s.incantation)}} · ${{esc(s.duree)}}</p>${{s.html_body}}</div></td><td><span class="chip">${{s.niveau===0?'Mineur':s.niveau}}</span></td><td class="hide-small">${{esc(s.ecole)}}</td><td class="hide-small">${{esc(s.incantation)}}</td><td>${{esc(s.portee)}}</td></tr>`).join('');}}
for(const id of ['search','class','level','school'])el(id).addEventListener('input',render);render();
</script></body></html>'''
(ROOT/'Bibliotheque.html').write_text(html_index,encoding='utf-8')
print('Generated markdown, HTML cards and interactive local index for',len(SPELLS),'spells')
