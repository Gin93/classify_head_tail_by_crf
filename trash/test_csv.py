# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:34:27 2017

@author: cisdi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:25:01 2017

@author: cisdi
"""



'''
csv
''' 
##逐个文件进行处理

import xlrd
#from getfeatures import *
from getfeatures1 import *
from otherfunctions import * 
import os 
import csv

import time


num_features = 5
test_data_path = 'C:/Users/cisdi/Desktop/test_data1/'
file_count = 0

################输入为不含空行的数据文件


def classify(data,sheetcount):
    time_start=time.time()

    output_path = 'C:/Users/cisdi/Desktop/output1/'
    crf_path = 'C:/Users/cisdi/Desktop/crf++0.58/'
    units_path = 'C:/Users/cisdi/Desktop/单位.xlsx'
    predict = []
    print('已处理' + str(sheet_count) + '个sheets')
    nrows = 0 # 相当于每一行的一个ID , 处理单位为sheet，所以ID对于每一个sheet中的每一行都是唯一的
    outputs = []


    for i in data : #逐行操作
        
        row_data = i
        tem_list = []
        tem_list.append(nrows)			
        features = get_features(row_data)                
        tem_list.append(features)
        tem_list.append(row_data)
        outputs.append(tem_list)
        nrows += 1
        
        
                
                
    ##把outputs[]（特征）输出到一个.data 文件中
    print('特征提取完毕')
    time_end=time.time()
      
    f1 = open( output_path + 'features'+str(sheet_count)+'.data' , 'w')
    for i in outputs:
        f1.write(str(i[0]))
        f1.write(' ')
        for j in i[1]:
            f1.write(str(j))
            f1.write(' ')
        f1.write('\n')
    f1.close()
    print (time_end-time_start)
    ######根据这个特征文件
    predict_cmd ='c: & ' 'cd '+ crf_path +' & '+ 'crf_test -m model1 '+ output_path + 'features'+str(sheet_count)+'.data > '+ output_path+'output'+str(sheet_count)+'.csv'
    os.system(predict_cmd) 
    
    #########解析crf模型输出的文件
    f2 = open(output_path + 'output'+str(sheet_count)+'.csv' , 'r')
    lines = f2.readlines()#读取全部内容 
    for line in lines:    
        line = line.strip('\n')
        data = line.split('\t') #倒数最后两个为label与分类结果
        if len(data) >3:             
            predict = predict  + [[data[0],data[-1] ]]      
    f2.close()
    
    
    #####################搜索单位行
    units = get_units(units_path) #从字典中获取单位
    for i,j in predict:
        if int(j) == 2: ####只从字段名里面找单位行
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
                predict[int(i)][1] = 3 ### 把结果修改为单位行      
    return predict 


all_files = dirlist(test_data_path,[])
sheet_count = 0;


for files in all_files: #读取逐个文件  aa
    print(files)
    b = []  #,encoding="utf-8"
    try:
        with open(files,"r",encoding="utf-8") as csvfile:
            data = csv.reader(csvfile)
            
            a = classify(data,1)        
            print('分类完毕')
            b = split(a)
        csvfile.close()
    except:
        with open(files,"r") as csvfile:
            data = csv.reader(csvfile)
            
            a = classify(data,1)        
            print('分类完毕')
            b = split(a)
        csvfile.close()       
        

   
      
