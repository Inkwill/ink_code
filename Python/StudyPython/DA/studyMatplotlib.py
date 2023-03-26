# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlwings as xw
#import scipy.stats as sc

plt.rcParams['font.sans-serif']=['SimHei']

# 柱形图
def ex1():
	#book = xw.Book(r'E:/MyDoc/Python/Projects/StudyPython/DA/exData.xlsx')
	#data = book.sheets['ex1'].range('A1').expand().options(pd.DataFrame).value

	data = pd.read_excel('exData.xlsx', 'ex1')

	labels = data['大洲'].values
	values = data['销量(件)'].values
	extend = list(map(lambda x:2000 - x, values))

	plt.barh(range(len(values)), values, label = '已完成', tick_label = labels, color = 'g')
	plt.barh(range(len(values)), extend, left = values, label = ' 未完成', color = 'r')
	plt.legend()

# 直方图
def ex2():
	data = pd.read_excel('exData.xlsx', 'ex2')

	widthData = list(map(lambda x,y : y - x, data['时间min'].values, data['时间max'].values))
	hightData = list(map(lambda x,y : x/y, data['频数'].values, widthData))
	plt.bar(data['时间min'].values, hightData, width = widthData, label = '频数密度', tick_label = data['时间min'].values, align = 'edge')
	plt.legend()

# 堆积图 &　多项式似合
def ex3():
	data = pd.read_excel('exData.xlsx', 'ex3')
	x  = data['时间']
	d1 = data['频数']
	y = list(map(lambda x:d1[:x].sum(),range(1,len(d1)+1)))

	z1 = np.polyfit(x,y,4)
	p1 = np.poly1d(z1)

	print(p1)
	yvals = np.polyval(z1,x)

	plt.plot(x,y,'*',label='original values')
	plt.plot(x,yvals,'black',label='polyfit values')
	plt.plot([4,4], [0,p1(4)], color='r', linewidth= 2.5,linestyle='--')
	plt.scatter([4,],[p1(4),], 50, color ='black')
	plt.annotate('(4,%d)' % p1(4),xy=(4,p1(4)),xytext=(5,p1(4)))
	plt.legend()

# 确定坐标范围 & 均值 & 中位数
def ex4():
	data = pd.read_excel('exData.xlsx', 'ex4')

	x1 = data['数值1']
	y1 = data['频数1']

	x2 = data['数值2']
	y2 = data['频数2']

	# 坐标范围
	plt.axis([0,max(x1.max(),x2.max()),0,max(y1.max(),y2.max())])
	# x轴刻度
	plt.xticks(range(max(x1.max(),x2.max())+1))

	plt.plot(x1, y1, color ='blue', label = 'Data1')
	plt.plot(x2, y2, color ='green', label = 'Data2')
	plt.legend()

	# 均值
	plt.plot([0,x1[len(x1)-1]],[np.average(y1),np.average(y1)],color = 'blue')
	plt.plot([0,x2[len(x2)-1]],[np.mean(y2),np.mean(y2)],color = 'blue')

	# 中位数
	plt.plot([0,x1[len(x1)-1]],[np.median(y1),np.median(y1)],color = 'red')
	plt.plot([0,x2[len(x2)-1]],[np.median(y2),np.median(y2)],color = 'red')

	# 众数
	plt.plot([0,x1[len(x1)-1]],[sc.mode(y1),sc.mode(y1)],color = 'green')

ex3()
plt.show()
