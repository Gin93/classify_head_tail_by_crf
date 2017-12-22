# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:37:39 2017

@author: cisdi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:25:01 2017

@author: cisdi
"""


##逐个文件进行处理

from getfeatures1 import *
from otherfunctions import * 
import os 
import csv
import time 

def classify_csv(path_a,path_b):
	'''
	输入文件路径a,b
	输出 操作的文件路径list // 要根据分类结果,把b拆成多个文件或者不拆
	解析过的csv文件都不含有空行 其中a只对合并过得单元格进行了上限的填充,而b做了全部的填充
	'''
	output_path = 'C:/Users/cisdi/Desktop/output/'
	crf_path = 'C:/Users/cisdi/Desktop/crf++0.58/'
	units_path = 'C:/Users/cisdi/Desktop/单位.xlsx'
	test_data_path = 'C:/Users/cisdi/Desktop/test_data1/'
	sheet_count = 1
	outputs = []
	predict = []
	
	nrows = 0 # 相当于每一行的一个ID , 处理单位为sheet，所以ID对于每一个sheet中的每一行都是唯一的
	try:
		with open(path_a,"r",encoding="utf-8") as csvfile:
			data = csv.reader(csvfile)
			for i in data : #逐行操作    
				features = get_features(i)
				outputs.append([nrows,features,i])
				nrows += 1 
	except:
		with open(path_a,"r") as csvfile:
			data = csv.reader(csvfile)      
			for i in data : #逐行操作    
				features = get_features(i)
				outputs.append([nrows,features,i])
				nrows += 1           
	##把outputs[]（特征）输出到一个.data 文件中

	  
	f1 = open( output_path + 'features'+str(sheet_count)+'.data' , 'w')
	for i in outputs:
		f1.write(str(i[0]))
		f1.write(' ')
		for j in i[1]:
			f1.write(str(j))
			f1.write(' ')
		f1.write('\n')
	f1.close()

	######根据这个特征文件
	predict_cmd ='c: & ' 'cd '+ crf_path +' & '+ 'crf_test -m model1 '+ output_path + 'features'+str(sheet_count)+'.data > '+ output_path+'output'+str(sheet_count)+'.data'
	os.system(predict_cmd) 
	
	#########解析crf模型输出的文件
	f2 = open(output_path + 'output'+str(sheet_count)+'.data' , 'r')
	lines = f2.readlines()#读取全部内容 
	for line in lines:    
		line = line.strip('\n')
		data = line.split('\t') #倒数最后两个为label与分类结果
		if len(data) >3:             
			predict.append(data[-1])     
	f2.close()
	
	
	#####################搜索单位行
	units = get_units(units_path) #从字典中获取单位    
	for i in predict:
		if int(i) == 2: ####只从字段名里面找单位行
			data = outputs[int(i)][2]
			clean_data = []      
			for m in data:  #去除掉该行的空值，因为要计算比例，太多空值会影响结果
				if m != '':
					clean_data.append(m)     
			l = len(clean_data)
			count = 0 
			for n in clean_data:
				if n in units:
					count += 1
			if count / l > 0.8: ### 看起来像是单位行
				predict[int(i)] = 3 ### 把结果修改为单位行   
				
	predict_f = split1(predict)


	#####################操作b.csv文件##########################
	output = []
	with open(path_b,"r") as csvfile:
		r = csvfile.readlines()
		csvID = 0
		rows = 0
		for eachtable in predict_f:
			output_csv_name = path_b.replace('.csv','') + '_'+ str(csvID) + '.csv'
			output.append(output_csv_name)
			with open(output_csv_name ,"w",newline='' ) as outputcsv:
				writer = csv.writer(outputcsv)
				for label in eachtable:
					data = r[rows].split(",")
					data = [label] + data
					writer.writerow(data)
					rows += 1
				csvID += 1
			
	return output



a = classify_csv('炉体10515温度2012.6.csv','123.csv')

print(a)
