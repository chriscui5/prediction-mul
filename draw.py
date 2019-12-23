import json
filename = 'city_air_2019.json'
with open(filename,encoding="utf-8") as f:
    city_air = json.load(f)

filename_1 = 'city.json'
with open(filename_1,encoding="utf-8") as f:
    gpd_list = json.load(f)
cities=[]
for i in gpd_list:
    for j in (i['children']):
        #print(j)
        city=[]
        name = 'error' # 默认值
        for key in city_air:
            if j['name'] == key:
                name = j['name']
                j['aqi'] = str(city_air[key][0])
                break
        log = j['log']
        lat = j['lat']
        if(name != 'error'):
            AQI = j['aqi']
            city.append(name)
            city.append(log)
            city.append(lat)
            city.append(AQI)
            cities.append(city)
print(cities)

import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Map, Page
from pyecharts.faker import Collector, Faker
from pyecharts.charts import Geo
import pandas as pd
from pyecharts.faker import Collector, Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType
c = Geo()
for i in cities:
    (c
    .add_schema(maptype="china")
    # 加入自定义的点，格式为
    .add_coordinate(i[0],float(i[1]),float(i[2]))

    # 为自定义的点添加属性
    #.add(i[0])
    .add("AQI", [(i[0],int(i[3]))])
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="全国空气质量"))
     .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(range_color=Faker.visual_color),
            title_opts=opts.TitleOpts(title="全国空气质量"),
        )
    )
# 在 Jupyter Notebook 中渲染图表
#c.render_notebook()
#在jupyter
c.render("china_today_air.html")# 在本地
#二选一
