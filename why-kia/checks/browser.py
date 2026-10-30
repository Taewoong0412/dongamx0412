from playwright.sync_api import sync_playwright
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--enable-unsafe-swiftshader','--use-angle=swiftshader']);q=b.new_page(viewport={'width':1440,'height':1000});errors=[];q.on('pageerror',lambda e:errors.append(str(e)))
 q.goto('http://127.0.0.1:8020');assert q.locator('.gamecard').count()==5;q.screenshot(path='checks/home-desktop.png',full_page=True)
 q.get_by_role('button',name='퍼즐',exact=True).click();assert q.locator('.gamecard').count()==1
 assert q.locator('.gamecard .play').count()==1;assert q.locator('.gamecard .play').get_attribute('href')=='play.html?game=puzzle'
 for route in ['team','project','data','tutorial','games']:
  q.goto('http://127.0.0.1:8020/#'+route);q.wait_for_timeout(120);assert q.locator('h1').count()==1
  if route=='data':
   q.locator('#pitcher').select_option('1');assert '네일' in q.locator('#pitchChart').inner_text();assert q.locator('#pitchChart tbody tr').count()==7
 q.goto('http://127.0.0.1:8020/play.html');q.frame_locator('#game').locator('#start').wait_for();assert '경기 시작' in q.frame_locator('#game').locator('#start').inner_text()
 q.set_viewport_size({'width':390,'height':844});q.goto('http://127.0.0.1:8020');q.screenshot(path='checks/home-mobile.png',full_page=True);assert q.evaluate('document.documentElement.scrollWidth<=innerWidth')
 q.locator('#mobile').click();q.locator('nav a[href="#team"]').click();q.get_by_text('약 한 달간',exact=False).wait_for();assert q.locator('.person').count()==5;assert '약 한 달' in q.locator('main').inner_text()
 for route in ['project','data','games','tutorial']:
  q.goto('http://127.0.0.1:8020/#'+route);q.wait_for_timeout(80);assert q.evaluate('document.documentElement.scrollWidth<=innerWidth'),route
 assert not errors,errors
 print('PASS: 5 game cards, category filters, puzzle launch link, 6 pages, pitcher chart, embedded 3D game, mobile navigation and overflow, no JS errors.')
 b.close()
