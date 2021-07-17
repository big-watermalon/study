from selenium import webdriver
import pandas as py
from lxml import etree
import time
from pyecharts.charts import WordCloud

browser = webdriver.Chrome()

url = 'https://music.163.com/#/playlist?id=3027744993'
song_list=[]
singer_count = []

browser.get(url)
time.sleep(10)
browser.switch_to.frame('g_iframe')

song = browser.find_elements_by_xpath('//span[@class="txt"]/a/b')
singer = browser.find_elements_by_xpath('//div[@class="text"]/span')
album = browser.find_elements_by_xpath('//div[@class="text"]/a')
for i in range(0,len(song)):
    print(song[i].get_attribute('title'),' ',singer[i].get_attribute('title'),album[i].get_attribute('title'))
    box={}
    box["歌名"]= song[i].get_attribute('title')
    box["歌手"]= singer[i].get_attribute('title')
    box["专辑"]= album[i].get_attribute('title')
    song_list.append(box)

song_list_data = py.DataFrame(song_list)
song_list_data.columns=["歌名","歌手","专辑"]
song_list_data.to_csv('neteasecloud.csv',encoding='utf_8_sig')

browser.close()

