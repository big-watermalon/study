import requests
from lxml import etree
import pandas as py
from plotly import offline
from plotly.graph_objs import Bar ,Layout

url="https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6"

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

f=open('weibo.txt','w')

def visual(pds):
    y_values=[]
    for i in range(0,50):
        str1=str(pds.loc[i,'热度'])
        str2=''.join(filter(str.isdigit,str1))
        y_values.append(int(str2))
    x_values =[]
    for i in range(0,50):
        str1=str(pds.loc[i,'标题'])
        x_values.append(str1)
    data = [Bar(x=x_values,y=y_values)]
    x_axis_config = {'title':'热度','dtick':1}
    y_axis_config = {'title':''}
    my_layout = Layout(title = '微博热搜前50', xaxis = x_axis_config , yaxis = y_axis_config)
    offline.plot({'data':data,'layout':my_layout},filename = 'visual.html')

def main():

  html=etree.HTML(requests.get(url,headers=header).text)
  rank=html.xpath('//td[@class="td-01 ranktop"]/text()')
  affair=html.xpath('//td[@class="td-02"]/a/text()')
  view = html.xpath('//td[@class="td-02"]/span/text()')
  href = html.xpath('//td[@class="td-02"]/a//@href')
  top=affair[0]
  affair=affair[1:]
  datas=[]
  for i in range(50):
      box = {}
      print(affair[i],href[i],view[i],'\n')
      box["热度"]=view[i]
      box["热搜"]=affair[i]
      box["链接"]=href[i]
      datas.append(box)
      f.write(affair[i]+'\n'+href[i]+'\n')
  dataf =py.DataFrame(datas)
  dataf.columns=["热度","标题","链接"]
  dataf.to_csv('dataf.csv',encoding='utf_8_sig')
  visual(dataf)
#  print('{0:<10}\t{1:<40}'.format("top",top))
#  for i in range(0, len(affair)):
#    print("{0:<10}\t{1:{3}<30}\t{2:{3}>20}".format(rank[i],affair[i],view[i],chr(12288)))
main()


