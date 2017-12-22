# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:25:01 2017

@author: cisdi
"""


##逐个文件进行处理

import xlrd
#from getfeatures import *
from getfeatures1 import *
from otherfunctions import * 

import pandas
import os 


num_features = 5
train_data_path = 'C:/Users/cisdi/Desktop/train_data/'
#test_data_path = 'C:/Users/cisdi/Desktop/test_data/'
test_data_path = 'C:/Users/cisdi/Desktop/testxxx/'
output_path = 'C:/Users/cisdi/Desktop/output/'
crf_path = 'C:/Users/cisdi/Desktop/crf++0.58/'
file_count = 0


 

'''
p=os.popen(cmd)
print (p.read())
'''

##### 可以作为一个function

all_files = dirlist(test_data_path,[])

classfication_results = []
actual = []
predict = []
sheet_count = 0;


for files in all_files: #读取逐个文件  

    try:
        data = xlrd.open_workbook(files)
        for eachsheet in data.sheets():  #逐个sheet读取
            sheet_count += 1 
            print('已处理' + str(sheet_count) + '个sheets')
            row_count = 0 # 相当于每一行的一个ID , 处理单位为sheet，所以ID对于每一个sheet中的每一行都是唯一的
            outputs = []
            nrows = eachsheet.nrows
    			
    			
            for eachrow in range(nrows): #逐行操作
                row_data = eachsheet.row_values(eachrow)
                #print(row_data)
                tem_list = []
    				
                label = labelling(row_data[0])
                
                if label != 'trash': 
                    
                    row_data.pop(0) #删除掉label，只保留数据
                    if  not empty (row_data):
    				
                        features = get_features(row_data)
                        tem_list.append(row_count)
                        tem_list.append(features)
                        tem_list.append(label)
                        tem_list.append(row_data)
                        row_count += 1
                        outputs.append(tem_list)
                        
                        
            ##把outputs[]输出到一个.data 文件中
    #        feature_file_name = 'features' + str(file_count) + '.data'
    
#            f1 = open( output_path + 'features.data' , 'w')
            f1 = open( output_path + 'features'+str(sheet_count)+'.data' , 'w')
            for i in outputs:
                f1.write(str(i[0]))
                f1.write(' ')
                for j in i[1]:
                    f1.write(str(j))
                    f1.write(' ')
                f1.write(i[2])
                f1.write('\n')
            f1.close()
            file_count += 1 
            
#            predict_cmd ='c: & ' 'cd '+ crf_path +' & '+ 'crf_test -m model1 '+ output_path + 'features.data > '+ output_path+'output.data'
            predict_cmd ='c: & ' 'cd '+ crf_path +' & '+ 'crf_test -m model1 '+ output_path + 'features'+str(sheet_count)+'.data > '+ output_path+'output'+str(sheet_count)+'.data'

            os.system(predict_cmd) 
#            subprocess.Popen(predict_cmd, shell=True)
            
            output_path = 'C:/Users/cisdi/Desktop/output/'
            
#            f2 = open(output_path + 'output.data' , 'r')
            f2 = open(output_path + 'output'+str(sheet_count)+'.data' , 'r')
            lines = f2.readlines()#读取全部内容 
            f = 0
            
            wrong_id = []
            for line in lines:
            
                line = line.strip('\n')
                data = line.split('\t') #倒数最后两个为label与分类结果
                if len(data) >3:
                    classfication_results.append(data)
                    actual.append(data[-2])
                    predict.append(data[-1])
                    if data[-2] != data[-1]:
                        
                        ID = int(data[0])
                        wrong_id.append(ID)
                        try:
                            
                            print('-------------------------')
                            print(ID)
                            print(outputs[ID][1])
                            print(outputs[ID][2])
                            print(outputs[ID][3])
                            print('预测结果为:' + data[-1])
                            print(files)
                            print(eachsheet.name)
                            print('-------------------------')
                        except:
                            print('++++++++++++++++++')
                            print(wrong_id)
                            print(data)

                            print('++++++++++++++++++')
                            
            f2.close()
    except:
        print('**********************')
        print(files)
        

confusion_matrix_plot_matplotlib(actual, predict)
df=pandas.DataFrame(classfication_results,columns=['ID','f1','f2','f3','f4','f5','actual','predict']) 
correct=df[df.actual==df.predict]
for i in ('1','2','4','5'):
    R=sum(correct.predict==i)/sum(df.actual==i)
    P=sum(correct.predict==i)/sum(df.predict==i)
    F=R*P*2/(R+P)
    print(i,':\n','R=',R,' P=',P,' F=',F)
    


'''
###### analyze the possibility 
output_path = 'C:/Users/cisdi/Desktop/output/'
f3 = open(output_path + 'output1.data' , 'r')
lines = f3.readlines()#读取全部内容 
classfication_results = []

count = 0 
for line in lines:
    line = line.strip('\n')
    data = line.split('\t') #倒数最后两个为label与分类结果
    if len(data) >3:
        tem = []
        for i in range(-5,0):
            modified_result = ''
            a = data[i].split('/')
            tem.append(float(a[1]))        
        if tem[0] < 0.33:
            
            x = max_index(tem)
            if  x == 1:
                modified_result = 'overview'
            elif x == 2:
                modified_result = 'attribute'
            elif x == 3:
                modified_result = 'data'
            elif x == 4:
                modified_result = 'tail'
            else:
                print('max_index错误')
                
        else:
            modified_result = data[-5].split('/')[0]
            
        if data[5] != modified_result:
            count += 1
print(count)             
'''               
                    


'''
classfication_results.append(data)

if data[5] not in data[6]:
    print(data[0])
    print(data[6])
'''
        

            
        
# =============================================================================
#         classfication_results.append(data)
#         actual.append(data[-2])
#         predict.append(data[-1])
#         if data[-2] != data[-1]:
#             
#             ID = int(data[0])
#             wrong_id.append(ID)
#             print('-------------------------')
#             print(ID)
#     #            print(data)
#     #            print(data[-2])
#     #            print(data[-1])
#             print(outputs[ID][1])
#             print(outputs[ID][2])
#             print(outputs[ID][3])
#             print('预测结果为:' + data[-1])
#             print('-------------------------')
# 
# =============================================================================


  
    
	






					
				
			