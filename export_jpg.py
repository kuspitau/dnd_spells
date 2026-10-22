#!/usr/bin/env python3
"""Capture une image JPEG complète par fiche HTML via Chromium local."""
import asyncio, base64, re
import fitz
from pathlib import Path
from PIL import Image
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parent

async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
  page=await browser.new_page(viewport={'width':840,'height':900},device_scale_factor=1.6)
  (ROOT/'fiches_pdf').mkdir(exist_ok=True)
  for f in sorted((ROOT/'fiches_html').glob('*.html')):
   contents=f.read_text(encoding='utf-8').replace('<link rel="stylesheet" href="../styles.css">','<style>'+ (ROOT/'styles.css').read_text(encoding='utf-8') +'</style>')
   def embed(m):
    fp=(f.parent/m.group(1)).resolve()
    return 'src="data:image/jpeg;base64,'+base64.b64encode(fp.read_bytes()).decode()+'"'
   contents=re.sub(r'src="(\.\./illustrations/[^"]+)"',embed,contents)
   await page.set_content(contents,wait_until='load')
   imgpath=ROOT/'fiches_jpg'/f'{f.stem}.jpg'
   await page.screenshot(path=str(imgpath),type='jpeg',quality=91,full_page=True,animations='disabled')
   bottom=await page.locator('#spell-card').evaluate('(el)=>el.getBoundingClientRect().bottom+window.scrollY')
   with Image.open(imgpath) as raw:
    cutoff=min(raw.height,int((bottom+35)*1.6))
    if cutoff<raw.height:
     raw.crop((0,0,raw.width,cutoff)).save(imgpath,format='JPEG',quality=91,subsampling=0,optimize=True)
   await page.pdf(path=str(ROOT/'fiches_pdf'/f'{f.stem}.pdf'),format='A4',print_background=True,prefer_css_page_size=True)
   print(f.stem,'=>',await page.evaluate('document.documentElement.scrollHeight'))
  await page.set_content((ROOT/'Bibliotheque.html').read_text(encoding='utf-8'),wait_until='load')
  print('INDEX', await page.locator('#count').inner_text(), 'cards',await page.locator('#items > tr').count())
  await page.screenshot(path=str(ROOT/'Apercu_bibliotheque.png'),full_page=True)
  await page.locator('#search').fill('familier')
  print('SEARCH', await page.locator('#count').inner_text())
  await page.locator('#search').fill('')
  await page.locator('#class').select_option('Paladin')
  print('FILTER', await page.locator('#count').inner_text())
  await page.locator('#search').fill('aversion/attirance')
  await page.locator('#class').select_option('')
  print('SLASH SEARCH',await page.locator('#count').inner_text())
  link=await page.locator('#items > tr a').first.get_attribute('href')
  print('SLASH LINK',link, 'target exists', (ROOT/link.replace('%20',' ')).exists())
  await browser.close()
  merged=fitz.open();toc=[]
  for f in sorted((ROOT/'fiches_pdf').glob('*.pdf')):
   doc=fitz.open(f);toc.append([1,f.stem,len(merged)+1]);merged.insert_pdf(doc);doc.close()
  merged.set_toc(toc);merged.save(ROOT/'Classeur_sorts.pdf',garbage=3,deflate=True);print('PRINT PDF',len(merged),'pages');merged.close()

if __name__=='__main__':asyncio.run(main())
