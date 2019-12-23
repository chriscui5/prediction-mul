import requests
import re
import json
def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def spyder(url):
    html = get_page(url)
    pattern=re.compile('<div class="left-col2" aqi="(.*?)">',re.S)
    AQI= re.findall(pattern, html)
    pattern1 = re.compile('<p class="num">(.*?)</p>', re.S)
    digits=re.findall(pattern1, html)
    components = [int(AQI[0]),int(digits[0]),int(digits[1]),int(digits[2]),int(digits[3]),int(digits[4]),int(digits[5])]
    return components

def spyder2(url):
    html = get_page(url)
    pattern=re.compile('<a href="/air/detail\?city_py=(.*?)" target="_blank" class="city">(.*?)</a>',re.S)
    city= re.findall(pattern, html)
    city_set = set(city)
    return city_set

if __name__ == '__main__':
    url='https://tianqi.sogou.com/air/detail?city_py=beijing'
    cities=spyder2(url)
    sum={}
    for city in cities:
        city_py=city[0]
        city_zw=city[1]
        url_city= 'https://tianqi.sogou.com/air/detail?city_py='+str(city_py)
        components=spyder(url_city)
        print(city_zw)
        print(components)
        sum[city_zw]=components

    with open('city_air_2019.json''', 'w',encoding='utf-8') as f:
        json.dump(sum, f)