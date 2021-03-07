from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
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
ActionChains(driver).move_to_element(ac).click(ac).perform()
subpage = BeautifulSoup(driver.page_source, 'html.parser')
tvb = subpage.video.attrs['src']
driver.back()
ac = driver.find_element_by_link_text('TVB無線新聞台')
ActionChains(driver).move_to_element(ac).click(ac).perform()
subpage = BeautifulSoup(driver.page_source, 'html.parser')
tvbnews = subpage.video.attrs['src']
driver.back()
ac = driver.find_element_by_link_text('TVB J2台')
ActionChains(driver).move_to_element(ac).click(ac).perform()
subpage = BeautifulSoup(driver.page_source, 'html.parser')
j2 = subpage.video.attrs['src']
driver.back()
ac = driver.find_element_by_link_text('香港有線新聞台')
ActionChains(driver).move_to_element(ac).click(ac).perform()
subpage = BeautifulSoup(driver.page_source, 'html.parser')
cablenews = subpage.video.attrs['src']
driver.back()
ac = driver.find_element_by_link_text('HBO HD')
ActionChains(driver).move_to_element(ac).click(ac).perform()
subpage = BeautifulSoup(driver.page_source, 'html.parser')
hbo = subpage.video.attrs['src']
driver.back()
ac = driver.find_element_by_link_text('ViuTV')
ActionChains(driver).move_to_element(ac).click(ac).perform()
subpage = BeautifulSoup(driver.page_source, 'html.parser')
viutv = subpage.video.attrs['src']
driver.back()
ac = driver.find_element_by_link_text('香港開電視')
ActionChains(driver).move_to_element(ac).click(ac).perform()
subpage = BeautifulSoup(driver.page_source, 'html.parser')
kaitv = subpage.video.attrs['src']
driver.back()
ac = driver.find_element_by_link_text('亚洲电视ATV')
ActionChains(driver).move_to_element(ac).click(ac).perform()
subpage = BeautifulSoup(driver.page_source, 'html.parser')
asiatv = subpage.video.attrs['src']
driver.back()
ac = driver.find_element_by_link_text('TVB無線財經資訊台')
ActionChains(driver).move_to_element(ac).click(ac).perform()
subpage = BeautifulSoup(driver.page_source, 'html.parser')
tvbnewsinfo = subpage.video.attrs['src']
driver.back()
ac = driver.find_element_by_link_text('NOW新聞台')
ActionChains(driver).move_to_element(ac).click(ac).perform()
subpage = BeautifulSoup(driver.page_source, 'html.parser')
nownews = subpage.video.attrs['src']
driver.quit()
file = open(r'./tv.m3u', mode='w', encoding='utf-8')
file.write('#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-MEDIA-SEQUENCE:0\n#EXT-X-ALLOW-CACHE:YES\n#EXT-X-TARGETDURATION:20')
file.write('\n#EXTINF:0,【翡翠台】線路1\n')
file.write(tvb)
file.write('\n#EXTINF:0,【翡翠台】線路2\n')
file.write(tvb+'&p=2')
file.write('\n#EXTINF:0,【翡翠台】線路3\n')
file.write('https://cdn.hkdtmb.com/hls/81/index.m3u8')
file.write('\n#EXTINF:0,【無線新聞台】\n')
file.write(tvbnews)
file.write('\n#EXTINF:0,【明珠台】\n')
file.write('https://cdn.hkdtmb.com/hls/84/index.m3u8')
file.write('\n#EXTINF:0,【J2】線路1\n')
file.write(j2)
file.write('\n#EXTINF:0,【J2】線路2\n')
file.write('https://cdn.hkdtmb.com/hls/82/index.m3u8')
file.write('\n#EXTINF:0,【有線新聞台】線路1\n')
file.write(cablenews)
file.write('\n#EXTINF:0,【有線新聞台】線路2\n')
file.write('http://livetv.dnsfor.me/channel.5.m3u8')
file.write('\n#EXTINF:0,【HBO電影】\n')
file.write(hbo)
file.write('\n#EXTINF:0,【ViuTV】線路1\n')
file.write(viutv)
file.write('\n#EXTINF:0,【ViuTV】線路2\n')
file.write('https://cdn.hkdtmb.com/hls/99/index.m3u8')
file.write('\n#EXTINF:0,【亞洲電視ATV】\n')
file.write(asiatv)
file.write('\n#EXTINF:0,【開電視】線路1\n')
file.write('http://media.fantv.hk/m3u8/archive/channel2_stream1.m3u8')
file.write('\n#EXTINF:0,【開電視】線路2\n')
file.write(kaitv)
file.write('\n#EXTINF:0,【無線財經資訊台】\n')
file.write(tvbnewsinfo)
file.write('\n#EXTINF:0,【NOW新聞】\n')
file.write(nownews)
file.write('\n#EXTINF:0,【港台電視31】\n')
file.write('https://rthklive1-lh.akamaihd.net/i/rthk31_1@167495/index_2052_av-b.m3u8')
file.write('\n#EXTINF:0,【港台電視32】\n')
file.write('https://rthklive2-lh.akamaihd.net/i/rthk32_1@168450/index_1080_av-b.m3u8')
file.write('\n#EXT-X-ENDLIST')
file.close()
