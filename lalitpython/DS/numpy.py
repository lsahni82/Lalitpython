# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 01:49:13 2018

@author: Lalit
"""
import numpy as np
scores = [89,56.34, 76,89, 98]
first_arr =np.array(scores)
print (first_arr)
print (first_arr.dtype)
type(first_arr)
scores_1 = [[34,56,23,89], [11,45,76,34]]
second_arr = np.array(scores_1)
print (second_arr)
print (second_arr.ndim)  #.ndim gives you the dimensions of an array.
print (second_arr.shape) #(number of rows, number of columns)
print (second_arr.dtype)

x = np.zeros(10) # returns a array of zeros, the same applies for np.ones(10)
x
np.ones((4,3)) # you can also mention the shape of the array
np.arange(100)

#Batch operations on data can be performed without using for loops, this is called vectorization
scores = [89,56.34, 76,89, 98]
first_arr =np.array(scores)
print (first_arr)
print (first_arr * first_arr)
print (first_arr - first_arr)
print (1/(first_arr))
print (first_arr ** 0.5)

# you may want to select a subset of your data, for which Numpy array indexing is really useful
new_arr = np.arange(12)
print (new_arr)
print (new_arr[5])
print (new_arr[4:9])
new_arr[4:9] = 99 #assign sequence of values from 4 to 9 as 99
print (new_arr)

modi_arr = new_arr[4:9] 
modi_arr
modi_arr[1] = 123456
print (new_arr)                  # you can see the changes are refelected in main array. 
modi_arr[:]                  # the sliced variable
            

# arrays can be treated like matrices
matrix_arr =np.array([[3,4,5],[6,7,8],[9,5,1]])
print (matrix_arr)
print (matrix_arr[:][2])
print (matrix_arr[1][2]) #first row and third column
print (matrix_arr[0,2]) # This is same as the above operation

from IPython.display import Image  # importing a image from my computer.
i = Image(filename='download.png')
i # Blue print of a matrix 

if(5>10):
    print("false")
else:
    print("hahahahaaaa")
    
    

import numpy as np
numpy._version_
np.__all__

result = 0
for i in range(100):
    result +=i
    
L=list(range(10))
L
L2=[str(c)for c in L]
L2
   
L3 = [True, "2", 3.0, 4]
[type(item) for item in L3] 
a=[1,2,3,4,5]
[type(l)for l in a]
i=1
np.array([range(i, i + 5) for i in [2, 4, 6]])
x1 = np.random.randint(10, size=6)
x1
z=[1,2,3,4,5,6,7,8,9,0,9,8]
x2 = np.array(3,4,z)
x2
x3 = np.random.randint(10, size=(3, 4, 5))
shape(z)
z.dtype
a.shape
a=np.array([[0,1,2,3],[10,11,12,13]])
a.shape
a.size
a.shape
np.shape(a)
a[0,1:2]
a=np.array([[1,2,3],[4,5,6]],float)
a
print (a.shape,"\n",a.itemsize)
print (a.dtype,a.dtype.type)
a=np.arange(0,80,10)
a
y=a[[1,2,-3]]
y
y=np.take(a,[1,2,-3])
y
mask=np.array([0,1,1,0,0,0,0,0],dtype=bool)
y=a[mask]
y
y=np.compress(mask,a)
y
a=np.arange([(0, 30, (5,6)])
a=np.array(np.arange(0,56))
a=np.arange(0, 36).reshape((6, 6))
a[(0,1,2,3,4),(1,2,3,4,5)]
a
a[3:,[0,2,5]]
a=np.array([[1,2,3],[4,5,6]],float)
a.sum(axis=1)
np.amin(a)
a.argmin(axis=0)
import pandas as pd
df =pd.DataFrame(np.arange(9).reshape(3,3),[index["b","a","c"] columns["praxis","berlin","madrid"]])
df = pd.DataFrame(np.arange(9).reshape(3,3),['b','a','c'],['Paris','Berlin','Madrid'])
df
df2 = pd.DataFrame(np.arange(12).reshape(4,3),['b','e','c','a'],['Paris','lisbom','Madrid'])
df2
df[:2]
df[1:2]
s
a
s = pd.Series([3,7,4,4,0.3], ['a','b','c','d','e'])
s
s2=pd.Series([0,1,2],['a','c','f'])
s2
s+s2
s-s2
s2-s
df+df2
df.add(df2,fill_value=0)
df1 = pd.DataFrame(np.arange(14).reshape(7,2),['b','a','c'],['Paris','Berlin','Madrid'])

df1=pd.DataFrame({'data1':[0,1,2,3,4,5,6],'keyleft':['b','b','a','c','a','a','b']})
df1
df2=pd.DataFrame({'data2':[0,1,2],'key':['a','b','d']})
df2
pd.merge(df1,df2,left_on='keyleft',right_on='key',how='inner')
pd.merge(df1,df2,left_on='keyleft',right_on='key',how='outer')
s
s.rank(ascending = False)
s.order()
s.sort_index(ascending=False)
df1.max
df1
import math
lambda x:math.sqrt(x)

a
import numpy as np
a=np.arange(0,80,10)
a
y=a[[1,2,-3]]
y=a[[1]]
y 
y=a[1] 
y 
index=[1,2,3] 
index 
y=np.take(a,index) 
y 
 mask=np.array([0,1,1,0,0,1,0,0],dtype=bool)
y=a[mask] 
y 
y,a
#%%
a=np.array([[1,2,3],[4,5,6]],float)
a
a.sum
sum(a)
a.sum()
a.sum(axis=1)
% timeit sum(a)
% timeit a.sum
a.argmax(axis=0)
np.argmax(a,axis=0)
a.max(axis=None)
np.average(a,axis=0)
a
a.clip(3,5)
a
a.flat
a
a.flat
a.flatten
a
y=a.flatten()
yy
a.flaten()
y
a
id(a)
b=a
id(b)
c=a.copy
id(c)
a.size
a.swapaxes(0,1)
a=np.array([1,2,3,4,5,6]).reshape(1,6)
a
a.transpose()
a.T
a.squeeze().ndim
a.ndim
a.shape
a.squeeze().shape
a[0,2]=100
a
a.nonzero()
z=a.copy()
z
a
