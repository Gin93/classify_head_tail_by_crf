# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:31:17 2017

@author: cisdi
"""


from otherfunctions import * 

def get_features(row_data):
    '''
    输入：(list) ： 一行数据
    输入: （list）：由特征组成的list
    '''
    l = len(row_data)
    def numbers (row_data,total):
        num = 0		
        for i in row_data:
            if i != '':
                try:
                    aa = float(i)
                    num +=1
                except:
                    pass
        if num == 0: 
            return 'str'
        elif num / total < 0.3:
            return 'fewnum'
        elif num / total < 0.6:
            return 'halfnum'
        else:
            return 'manynum'
			
    def neg_num (row_data,total):
        count = 0 
        for i in row_data:
            a = 1
            try:
                a = float(i)
                if a < 0:
                    count += 1
            except:
                pass
        if count == 0:
            return 'noneneg'
        elif count / total < 0.3:
            return 'fewneg'
        else:
            return 'manyneg'

		
    def decimals_num(row_data,total):
        count = 0
        space = 0
        for i in row_data:
            if i == '':
                space +=1
            if type(i) == float:
                count +=1
            elif type(i) == str:
                try:
                    aa = float(i)
                    if i.count('.') == 1:
                        count +=1
                except:
                    pass
        total = total - space 
        if count == 0:
            return 'none'
        if count / total > 0.7:
            return 'many'
        elif count / total > 0.3:  #############  阈值可以再调整
            return 'some'
        else:
            return  'few' 
			
    def spaces(row_data,total):
        count = 0
        for i in row_data:
            if i == '':
                count += 1	
        if count/total > 0.8 and (total - count) < 5:
            return 'sparse'
        elif count/total > 0.4:
            return 'normal'
        else:
            return 'full'
			
    def var (row_data):
        a = variance(row_data)
        if a < 100:
            return 'lowvar'
        elif a < 200:
            return 'midvar'
        else:
            return 'highvar'
		
    output = []
    a = row_data
    output.append(numbers(a,l))
    output.append(neg_num(a,l))
    output.append(decimals_num(a,l))
    output.append(spaces(a,l))
    output.append(var(a))
    
    return(output)
	
	
		
			
		





	