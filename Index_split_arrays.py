import numpy as np

#Indexation
arr1 = np. arange(0,30,3)
print(arr1)
print(arr1[0])
print(arr1[1])
print(arr1[2])
print(arr1[3])
print(arr1[0:4])
arr1[0:3] = 100
print(arr1)
arr1 = np.arange(50).reshape((5,10))
print(arr1)

#Visualize shape
print(arr1.shape)

#Select items from array
arr2 = arr1[:3][:]
print(arr2)

arr2 = arr1[:3]
print(arr2)

#arr2 is only a pointer to arr1
arr2[:]=100
print(arr1)
print(arr2)

#Use copy to avoid misuse of this pointer
arr1 = np.arange(50).reshape((5,10))
print(arr1)
arr2 = arr1[:3].copy()
print(arr2)
arr2[:]=100 
print(arr1)
print(arr2)

#Index using ','
print(arr1[1:4,5:])

#Logic operations
bol = arr1 >25
print(bol)
print(arr1[bol])

#examples
arr3 = np.linspace(0,100,12)
print(arr3)
print('\n')
print(arr3.shape)
print('\n')
arr3 = arr3.reshape(3,4)
print(arr3)
print('\n')
print(arr3[1:,2:])