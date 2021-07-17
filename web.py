import requests
from lxml import etree
import time

url="https://96.f.1ting.com/local_to_cube_202004121813/96kmp3/zzzzzmp3/2015cMar/30F/30gslp/08.mp3"

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

respone = requests.get(url,headers=header).content
with open('08.mp3','ab') as f:
    f.write(respone)

