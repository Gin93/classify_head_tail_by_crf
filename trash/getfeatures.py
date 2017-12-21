
from otherfunctions import * 

def get_features(row_data):
    '''
    输入：(list) ： 一行数据
    输入: （list）：由特征组成的list
    '''

    def str_ (row_data):
        str = 0
        num = 0		
        for i in row_data:
            if i != '':
                try:
                    aa = float(i)
                    num +=1
                except:
                    str += 1
        if str >= num: 
            return 'str'
        else:
            return 'num'
			
    def contain_decimals(row_data):
        for i in row_data:
            if type(i) == float:
                return 'decimals'
            elif type(i) == str:
                try:
                    aa = int(i)
                    if i.count('.') == 1:
                        return 'decimals'
                except:
                    pass
        return 'nodecimals'
		
    def decimals_num(row_data):
        count = 0
        total = len(row_data)
        space = 0
        for i in row_data:
            if i == '':
                space +=1
            if type(i) == float:
                count +=1
            elif type(i) == str:
                try:
                    aa = int(i)
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
			
    def spaces(row_data):
        count = 0
        total = len(row_data)	
        for i in row_data:
            if i == '':
                count += 1	
        if count/total > 0.8:
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
    output.append(str_(a))
    output.append(contain_decimals(a))
    output.append(decimals_num(a))
    output.append(spaces(a))
    output.append(var(a))
    
    return(output)
	
	
		
			
		





	