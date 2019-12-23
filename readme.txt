基于多元线性回归的空气质量预测
1.spyder_train.py是我爬虫训练集的文件，air_chengdu_2018.csv是爬出来的文件
（自变量：PM,PM10,SO2,NO2,CO,O3）
(因变量：AQI)
2.spyder_yuce.py是爬虫预测集的文件，运行此文件可以得到全国城市今日的PM,PM10,SO2,NO2,CO,O3的浓度
3.mul2.py是建立多元线性回归的文件，并且得到基于多元线性回归的全国城市的AQI指数文件
4.China_today_air.html是全国城市的AQI指数的显示网页,这个draw.py文件画出来的HTML文件
5.filename1.png是PM,PM10,SO2,NO2,CO,O3分别随着AQI变化的图片
6.prediction.png是我建立模型的偏离真实值的评级图
操作：
1.运行 spyder_yuce.py//得到近日全国城市的PM,PM10,SO2,NO2,CO,O3的浓度
2.运行 mul2.py//建立模型得到今日全国城市的AQI指数
3.运行 draw.py//显示全国城市的AQI指数
4.打卡China_today_air.html文件就是显示出来的画面