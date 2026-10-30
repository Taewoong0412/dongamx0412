from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--enable-unsafe-swiftshader','--use-angle=swiftshader'])
 results=[]
 for key in ['catch','dodge','survival','innings','tutorial','puzzle']:
  q=b.new_page(viewport={'width':1100,'height':720});err=[];bad=[];q.on('pageerror',lambda e:err.append(str(e)));q.on('response',lambda r:bad.append(r.url) if r.status>=400 else None);q.goto('http://127.0.0.1:8020/games/'+key+'/index.html');q.wait_for_timeout(900);q.screenshot(path='assets/screens/'+key+'.png');buttons=q.locator('button').all_text_contents();print(key,'buttons',buttons[:15], 'errors',err,'bad',bad);results.append({'game':key,'errors':err,'bad':bad});q.close()
 b.close()
 print(json.dumps(results,ensure_ascii=False))
