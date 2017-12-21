# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:59:34 2017

@author: cisdi
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

s = pd.Series([1,3,4,5,np.nan,6,8])

dates = pd.date_range('20130301',periods = 6)


#Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns:
#创建dataframe  大小， X_index , y_index
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

#Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({ 'A' : 1., 'B' : pd.Timestamp('20130102'),'C' : pd.Series(1,index=list(range(4)),dtype='float32'),'D' : np.array([3] * 4,dtype='int32'),'E' : pd.Categorical(["test","train","test","train"]),'F' : 'foo' })