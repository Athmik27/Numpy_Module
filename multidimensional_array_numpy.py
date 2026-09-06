#MULTIDIMENSIONAL ARRAY
import numpy as np

# print(np.__version__)

# this is an Zero dimension array
#A NumPy array is designed to store data in a regular, structured layout, especially numerical data so we use array for numpy.
array=np.array('A')
print(array.ndim) 
print(array.shape)
# #ndim=number of dimension in an variable_name
# we get output a '0' because its an zero dimension array(only 1 letter is there)

#this is an one dimension array

array=np.array(['A','B','C'])
print(array.ndim)
print(array.shape)
#output is one as all the elements are in a single sequence.

#this is an 2 dimension array

array=np.array([['A','B','C'],['D','E'],['F','G','H']])
print(array.ndim)

# this gives an error as in list there are 3 element where-as in 2nd list there are only 2 elements
#ValueError: setting an array element with a sequence.

array=np.array([['A','B','C'],
                 ['D','E','I'],
                 ['F','G','H']])
print(array.ndim)
print(array.shape)

# this is an 3 dimension array

array=np.array([[['A','B','C'],['D','E','I'],['F','G','H']],
                [['J','K','L'],['M','N','O'],['F','G','H']],
                [['Y','X','Q'],['Z','U','W'],['S','R','T']]])
print(array.ndim)
print(array.shape)

#CHAIN INDEXING
print(array[0][0][0])# this is 1st column,1st row,1st element  this gives letter 'A'
#we can write the above in MULTIDIMENSIONAL INDEXING 

#MULTIDIMENSIONAL INDEXING
print(array[0,0,0])


word=array[0,0,0]+ array[2,0,0]+array[2,0,0]
print(word)
#array[layer,row,column] format

# # remember this below 

    #   np.array('A') → 0D array
    #   np.array(['A']) → 1D array
    #   np.array([['A']]) → 2D array

# np.array('A')
# ndim  → 0
# shape → ()

# np.array(['A'])
# ndim  → 1
# shape → (1,)

# np.array([['A']])
# ndim  → 2
# shape → (1, 1)

 #Indexing a 2D array

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

 # Syntax: arr[row, column]
print(arr[1, 2])


# Getting an entire row

print(arr[0])

# Getting an entire column

print(arr[:, 1])