
import os 
import xlrd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy

def labelling(a):
    '''
    输入单个值 (string)
    输出 label (string)
    '''
    if a == 'a':
        return '1' #文字描述性表头
    elif a =='b':
        return '2' #字段名
    elif a == 'c':
        return '4' #表身、数据
    elif a == 'd':
        return '5'#表尾
    else:
        return 'trash'#防止标错或者是标记了空行
		

def dirlist(path, allfile):  
    '''
    dirlist("/home/yuan/testdir", [])   
    输入路径 (string)
    输出该目录下所有文件的路径 (list)
    '''
    filelist =  os.listdir(path)  

    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            dirlist(filepath, allfile)  
        else:  
            allfile.append(filepath)  
    return allfile  


def empty(row_data):
    for i in row_data:
        if i != '':
            return False
    return True
  
def confusion_matrix_plot_matplotlib(y_truth, y_predict, cmap=plt.cm.Blues):
    """Matplotlib绘制混淆矩阵图
    parameters
    ----------
        y_truth: 真实的y的值, 1d array
        y_predict: 预测的y的值, 1d array
        cmap: 画混淆矩阵图的配色风格, 使用cm.Blues
    """
    cm = confusion_matrix(y_truth, y_predict)
    plt.matshow(cm, cmap=cmap)  # 混淆矩阵图
    plt.colorbar()  # 颜色标签
     
    for x in range(len(cm)):  # 数据标签
        for y in range(len(cm)):
            plt.annotate(cm[x, y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
     
    plt.xlabel('True label')  # 坐标轴标签
    plt.ylabel('Predicted label')  # 坐标轴标签
    plt.show()  # 显示作图结果
    
    
def max_index (l):
    '''
    输入 list
    输出 最大值的坐标
    '''
    m = l[0]
    max_index = 0
    for i in range(len(l)):
        if l[i] > m:
            m = l[i]
            max_index = i
    return max_index





def variance (l):
    '''
    输入 list
    输出 看每个单元格
    '''
    char_list = []
    N = len(l)
    for i in range(N):
        char_list.append(len(str(l[i])))
        
    
    narray=numpy.array(char_list)
    sum1=narray.sum()
    narray2=narray*narray
    sum2=narray2.sum()
    mean=sum1/N
    var=sum2/N-mean**2
    
    return var

def get_units (path): 
    data = xlrd.open_workbook(path) # 读取该excel/表的信息
    a = []   
    for eachsheet in data.sheets():  #逐个sheet读取
        nrows = eachsheet.nrows
        for eachrow in range(nrows): #逐行操作           
            row_data = eachsheet.row_values(eachrow) #获取该行的数据
            for data in row_data:
                a.append(data)
                
    return (list(set(a)))        

def split(l):
    '''
    输入为一个二维list [[a1,b2],[a2,b2],[a3,b3],.......]
    输出为拆分过后的表 [ [ [a1,b1],[a2,b2] ], [a3,b3]] 即 a1,a2行数据属于同一个表,a3行属于另一个表
    '''
    output = []
    tem_list = []    
    
    max = 0
    for i,j in l:
        a = int(i)
        b = int(j)
        
        if b >= max:
            tem_list.append([i,j])
            max = b
        else:
            output.append(tem_list)
            tem_list = []
            tem_list.append([i,j])
            max = 0
    output.append(tem_list)
    
    if len (output)> 1:
        if final_check(output[-1]):
            print('final_check_issues')
            #设置为最后一个表的最后一个分类结果 4 or 5
            last = output[-2][-1][1]
            last = '5'
            for a1,a2 in output[-1]:
                print(a1,a2)
                output[-2] = output[-2] + [[a1,last]]
            output.pop(-1)

    
    return output

def split1(l):
    '''
    输入为一个一维list [label1,l2,l2,l3]
    输出为拆分过后的表,一个二维数组 即[[l1,l2,l3],[l4,l5,l6]] l1,l2,l3 是一个表, 其余三个为另一个表
    '''
    output = []
    tem_list = []    
    
    max = 0
    for i in l:
        b = int(i)
        
        if b >= max:
            tem_list.append(i)
            max = b
        else: #出现第二个表，把第一个表存起来,清空list,并且存入当前的label
            output.append(tem_list)
            tem_list = []
            tem_list.append(i)
            max = 0
    output.append(tem_list)
    
    if len (output)> 1:
        if '4' not in output[-1]:  #可以做一波修改
            print('final_check_issues')
            #设置为最后一个表的最后一个分类结果 4 or 5
            last = output[-2][-1]
            last = '5'
            for a1 in output[-1]:
                output[-2].append(last)
            output.pop(-1)

    
    return output


def final_check(l):
    '''
    对分割后的最后一个表做处理判断其是否是分类错误
    输入为一个二维list
    True为分类错误，需要进行合并
    '''
    for i,j in l:
        if j == '4':
            return False 
    return True        
    

