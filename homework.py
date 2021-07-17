import requests
from bs4 import BeautifulSoup
import pandas
from plotly import offline
from plotly.graph_objs import Bar ,Layout

def get_html(url):
    try:
        res = requests.get(url, timeout=30)
        res.encoding = 'gbk'
        return res.text
    except:
        return ''


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    tr_list = soup.find_all('tr', attrs={"bgcolor": "#FFFFFF"})
    houses = []
    for tr in tr_list:
        house = {}
        house["详细地址"] = tr.find_all('a', attrs={"target": "_blank"})[0].string
        house["详情链接"] = "https://www.lgfdcw.com/cs/" + tr.find_all('a', attrs={"target": "_blank"})[0].attrs["href"]
        house["房型"] = tr.find_all("td")[2].string
        house["户型"] = tr.find_all("td")[3].string
        house["面积"] = tr.find_all("td")[4].string
        house["出售价格"] = tr.find_all("td")[5].string.strip() if tr.find_all("td")[5].string != None else '面议'
        house["登记时间"] = tr.find_all("td")[6].string
        houses.append(house)
    return houses


def save_file(dic):
    df = pandas.DataFrame(dic)
    df.columns = ["详细地址", "详情链接", "房型", "户型", "面积", "出售价格", "登记时间"]
    return df

def visual(pds):
    y_values=[]
    for i in range(0,30):
        str1=str(pds.loc[i,'面积'])
        str2=''.join(filter(str.isdigit,str1))
        y_values.append(int(str2))
    x_values =list(range(1,30))
    data = [Bar(x=x_values,y=y_values)]
    x_axis_config = {'title':'面积/m²','dtick':1}
    y_axis_config = {'title':''}
    my_layout = Layout(title = '龙港房地产网房型面积', xaxis = x_axis_config , yaxis = y_axis_config)
    offline.plot({'data':data,'layout':my_layout},filename = 'visual.html')

def main():
    url = 'https://www.lgfdcw.com/cs/index.php?userid=&infotype=&dq=&fwtype=&hx=&price01=&price02=&pricetype=&fabuday=&addr=&PageNo=1'
    html = get_html( url)
    res = parse_html( html )
    pds= save_file(res)
    print(pds)
    visual(pds)
main()




