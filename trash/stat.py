# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 19:33:29 2017

@author: cisdi
"""

###############获取阈值


import xlrd
from getfeatures import *

from otherfunctions import * 



num_features = 4
train_data_path = 'C:/Users/cisdi/Desktop/train_data/'
test_data_path = 'C:/Users/cisdi/Desktop/test_data/'
output_path = 'C:/Users/cisdi/Desktop/output/'
crf_path = 'C:/Users/cisdi/Desktop/crf++0.58/'



##### 可以作为一个function

all_files = dirlist(train_data_path,[])

row_count = 0
outputs = []

A = []
B = [] 
C = [] 
D = []

for files in all_files: #读取逐个文件  

#    try:
    data = xlrd.open_workbook(files)
    for eachsheet in data.sheets():  #逐个sheet读取
        nrows = eachsheet.nrows
			
			
        for eachrow in range(nrows): #逐行操作
            row_data = eachsheet.row_values(eachrow)
            #print(row_data)
            tem_list = []
				
            label = labelling(row_data[0])
            
            if label != 'trash': 
                
                row_data.pop(0) #删除掉label，只保留数据
                if  empty (row_data):
                    
                    features = get_features(row_data)
                    tem_list.append(row_count)
                    tem_list.append(features)
                    tem_list.append(label)
                    tem_list.append(row_data)
                    row_count += 1
                    outputs.append(tem_list)
                    
                    var = variance(row_data)
                    if label == 'overview':
                        A.append(var)
                    elif label == 'attribute':
                        B.append(var)
                    elif label == 'data':
                        C.append(var)
                    elif label == 'tail':
                        D.append(var)
         
            
           

#    except:
#        print(files)
        



        
'''
#for循环之后得到一个list,包含了提取出的features -> outputs[i][1] 以及label -> outputs[i][2]
'''
##把outputs[]输出到一个.data 文件中
'''
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
'''
####### 得到一个标准格式的.data文件
					
##training#####
##用crf模型训练
##得到一个训练好的model
'''
training_cmd ='c: & ' 'cd '+ crf_path +' & '+ 'crf_learn template '+ output_path + 'features.data model1'
os.system(training_cmd) 
'''


'''
##分类####  ############投票方法时修改为输出概率

## 分类文件中可以带着label
##用训练好的model分类
##得到一个.data文件


predict_cmd ='c: & ' 'cd '+ crf_path +' & '+ 'crf_test -m model1 '+ output_path + 'features.data > '+ output_path+'output.data'
os.system(predict_cmd) 


###计算正确率
####所有输出都放到了一个文件里





output_path = 'C:/Users/cisdi/Desktop/output/'
f2 = open(output_path + 'output.data' , 'r')
lines = f2.readlines()#读取全部内容 
actual = []
predict = []
f = 0
classfication_results = []

for line in lines:

    line = line.strip('\n')
    data = line.split('\t') #倒数最后两个为label与分类结果
    if len(data) >3:
        classfication_results.append(data)
        actual.append(data[-2])
        predict.append(data[-1])
        
f2.close()

confusion_matrix_plot_matplotlib(actual, predict)
df=pandas.DataFrame(classfication_results,columns=['ID','f1','f2','f3','f4','actual','predict']) 
correct=df[df.actual==df.predict]
for i in ('overview','attribute','data','tail'):
    R=sum(correct.predict==i)/sum(df.actual==i)
    P=sum(correct.predict==i)/sum(df.predict==i)
    F=R*P*2/(R+P)
    print(i,':\n','R=',R,' P=',P,' F=',F)
'''

  
    
	






					
				
			