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
    print("hahahah")
    
    




