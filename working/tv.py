from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/535.46 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"')
driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)
try:
    url_home = "http://m.iptv345.com/iptv.php?tid=gt"
    driver.get(url_home)
    ac = driver.find_element_by_link_text('TVB翡翠台')
except:
    try:
        url_home = "http://m.iptv222.com/iptv.php?tid=gt"
        driver.get(url_home)
        ac = driver.find_element_by_link_text('TVB翡翠台')
    except:
        try:
            url_home = "http://m.iptv805.com/iptv.php?tid=gt"
            driver.get(url_home)
            ac = driver.find_element_by_link_text('TVB翡翠台')
        except:
            url_home = "http://m.iptv456.com/iptv.php?tid=gt"
            driver.get(url_home)
            ac = driver.find_element_by_link_text('TVB翡翠台')         
count = 0
for channel in ['TVB翡翠台','TVB無線新聞台','TVB J2台','香港有線新聞台','HBO HD','ViuTV','香港開電視','亚洲电视ATV','TVB無線財經資訊台','NOW新聞台']:
    count+=1
    locals()['CH'+str(count)] = channel
for count in range(1,11):  
    CH = locals()['CH'+str(count)]
    try:   
        driver.get(url_home)
        ac = driver.find_element_by_link_text(CH)
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        subpage = BeautifulSoup(driver.page_source, 'html.parser')
        locals()['CH_URL'+str(count)] = subpage.video.attrs['src']
    except:
        continue
driver.quit()
for count in range(1,11):
    try:
        locals()['m3u_URL'+str(count)] = locals()['CH_URL'+str(count)]
    except:
        locals()['m3u_URL'+str(count)] = '\n#EXTINF:0,【'+locals()['CH'+str(count)]+'】:此頻道直播源獲取失敗\nhttps://fail.m3u8'
file = open(r'./tv.m3u', mode='w', encoding='utf-8')
file.write('#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-MEDIA-SEQUENCE:0\n#EXT-X-ALLOW-CACHE:YES\n#EXT-X-TARGETDURATION:20')
file.write('\n#EXTINF:0,【翡翠台】線路1\n'+m3u_URL1+'\n#EXTINF:0,【翡翠台】線路2\n'+m3u_URL1+'&p=2'+'\n#EXTINF:0,【翡翠台】線路3\n'+'https://cdn.hkdtmb.com/hls/81/index.m3u8')
file.write('\n#EXTINF:0,【無線新聞台】\n'+m3u_URL2+'\n#EXTINF:0,【明珠台】\n'+'https://cdn.hkdtmb.com/hls/84/index.m3u8')
file.write('\n#EXTINF:0,【J2】線路1\n'+m3u_URL3+'\n#EXTINF:0,【J2】線路2\n'+'https://cdn.hkdtmb.com/hls/82/index.m3u8')
file.write('\n#EXTINF:0,【有線新聞台】線路1\n'+m3u_URL4+'\n#EXTINF:0,【有線新聞台】線路2\n'+'http://livetv.dnsfor.me/channel.5.m3u8')
file.write('\n#EXTINF:0,【HBO電影】\n'+m3u_URL5)
file.write('\n#EXTINF:0,【ViuTV】線路1\n'+m3u_URL6+'\n#EXTINF:0,【ViuTV】線路2\n'+'https://cdn.hkdtmb.com/hls/99/index.m3u8')
file.write('\n#EXTINF:0,【開電視】線路1\n'+m3u_URL7+'\n#EXTINF:0,【開電視】線路2\n'+'http://media.fantv.hk/m3u8/archive/channel2_stream1.m3u8')
file.write('\n#EXTINF:0,【亞洲電視ATV】\n'+m3u_URL8)
file.write('\n#EXTINF:0,【無線財經資訊台】\n'+m3u_URL9+'\n#EXTINF:0,【NOW新聞】\n'+m3u_URL10)
file.write('\n#EXTINF:0,【港台電視31】\n'+'https://rthklive1-lh.akamaihd.net/i/rthk31_1@167495/index_2052_av-b.m3u8'+'\n#EXTINF:0,【港台電視32】\n'+'https://rthklive2-lh.akamaihd.net/i/rthk32_1@168450/index_1080_av-b.m3u8')
file.write('\n#EXT-X-ENDLIST')
file.close()
