import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
import csv
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import time
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
for i in range(1, 13):
    time.sleep(5)
    # 把1转换为01
    # 获取2018年空气质量数据
    url = 'http://www.tianqihoubao.com/aqi/chengdu-2018' + str("%02d" % i) + '.html'
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    tr = soup.find_all('tr')
    # 去除标签栏


    for j in tr[1:]:
        td = j.find_all('td')
        #Date = td[0].get_text().strip()
        #Quality_grade = td[1].get_text().strip()
        AQI = td[2].get_text().strip()
        #AQI_rank = td[3].get_text().strip()
        PM = td[4].get_text()
        PM10=td[5].get_text()
        So2=td[6].get_text()
        No2=td[7].get_text()
        Co=td[8].get_text()
        O3=td[9].get_text()
        with open('air_chengdu_2018.csv', 'a+', encoding='utf-8-sig') as f:
            f.write(PM+','+PM10+','+So2+','+No2+','+Co+','+O3+','+AQI+'\n')


