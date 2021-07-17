import requests
from lxml import etree
import pandas as py
from plotly import offline
from plotly.graph_objs import Bar ,Layout
from pyecharts.charts import Bar
from pyecharts import options as opts
import os

url = 'https://www.zhihu.com/billboard'

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

response = requests.get(url, headers=header)
text = response.text
html = etree.HTML(text)
title = html.xpath("//div[@class='HotList-itemTitle']/text()")
href = html.xpath("//div[@class='HotList-itemMetrics']/text()")

hot_list = []
title_data = []
message = []

for i in range(0,50):

 print(i+1,'\n',title[i],'\n',href[i])
 box ={}
 box["标题"] = title[i]
 box["热度"] = href[i]
 hot_list.append(box)
 title_data.append(title[i])
 str2=''.join(filter(str.isdigit,href[i]))
 message.append(int(str2))

hot_list_data = py.DataFrame(hot_list)
hot_list_data.columns=["标题","热度"]
hot_list_data.to_csv('zhihu.csv',encoding='utf_8_sig')

bar =Bar()
bar.add_xaxis(title_data)
bar.add_yaxis("热度",message)
bar.set_global_opts(title_opts=opts.TitleOpts(title="知乎热搜榜"),
                    xaxis_opts=opts.AxisOpts(name_rotate=60,axislabel_opts={"rotate":45})
                    )

bar.render()
os.system("render.html")





