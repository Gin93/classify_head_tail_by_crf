# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:28:28 2017

@author: cisdi
"""

import xlrd
from getfeatures import *

from otherfunctions import * 

import pandas
import os 

num_features = 5
train_data_path = 'C:/Users/cisdi/Desktop/train_data/'
test_data_path = 'C:/Users/cisdi/Desktop/test_data/'
output_path = 'C:/Users/cisdi/Desktop/output/'
crf_path = 'C:/Users/cisdi/Desktop/crf++0.58/'


all_files = dirlist(train_data_path,[])#获取文件夹下所有文件的路径

row_count = 0 #用于对每一列数据进行标识
outputs = [] #保存提取出的特征

for files in all_files: #读取逐个文件  

    try:
        data = xlrd.open_workbook(files) # 读取该excel/表的信息
        for eachsheet in data.sheets():  #逐个sheet读取
            nrows = eachsheet.nrows

            for eachrow in range(nrows): #逐行操作
                row_data = eachsheet.row_values(eachrow) #获取该行的数据
                tem_list = [] 
                label = labelling(row_data[0]) #解析手工标记的abcd，对于abcd以外的，一律标记为...
                #...'trash'来忽略掉该行数据      
                if label != 'trash':         # 只对有abcd标记的行进行操作          
                    row_data.pop(0) # 删除掉label（abcd），只保留数据
                    if  empty (row_data):    #只对非空数据进行操作	
                        features = get_features(row_data) #获取特征值
                        tem_list.append(row_count) #记录行数，主要用于CRF中训练表示数据，需要唯一性
                        tem_list.append(features) #获取的特征
                        tem_list.append(label) #解析过的标签
                        row_count += 1
                        outputs.append(tem_list)
    except:
        print(files)
        
'''
#for循环之后得到一个list,包含了提取出的features -> outputs[i][1] 以及label -> outputs[i][2]
'''
##把outputs[]输出到一个.data 文件中
f1 = open( output_path + 'features.data' , 'w')
for i in outputs:
    f1.write(str(i[0]))
    f1.write(' ')
    for j in i[1]:
        f1.write(str(j))
        f1.write(' ')
    f1.write(i[2])
    f1.write('\n')
f1.close()

####### 得到一个标准格式的.data文件
					
##training#####
##用crf模型训练
##得到一个训练好的model
training_cmd ='c: & ' 'cd '+ crf_path +' & '+ 'crf_learn template '+ output_path + 'features.data model1'
os.system(training_cmd) 




    
	






					
				
			