import numpy as np

#Create lists
my_list = [1,2,3]
my_list2 = [[1,2,3],[4,5,6],[7,8,9]]
print(my_list)
print(my_list2)

#Create arrays
print(np.array(my_list))
print(np.array(my_list2))

#Creating arrays with range
print(np.arange(0,10))

#Create arrays with zeros
arr = np.zeros(3)
print(arr)
arr2 = np.zeros((5,5))
print(arr2)

#Create arrays with ones
arr3 = np.ones((3,3))
print(arr3)

#Create identity matrix
arr4 = np.eye(4)
print(arr4)

#Create with linspace
arr5 = np.linspace(0,10,2)
print(arr5)
arr6 = np.linspace(0,10,3)
print(arr6)
arr7 = np.linspace(0,10,5)
print(arr7)
arr8 = np.linspace(0,10,7)
print(arr8)

#Create using random.rand
arr9 = np.random.rand(5)
print(arr9)
arr10 = np.random.rand(5,4)
print(arr10)
arr11 = np.random.rand(2,2,2)
print(arr11)
arr12 = np.random.rand(2,2,2,2)
print(arr12)

#Create using random.randn
print(np.random.randn(4))

#Create using random.randint
print(np.random.randint(0,100,10))

#Exemple1: we can manipulate the methods
print(np.random.randint(0,100,10)*100)
print(np.round(np.random.rand(5)*100,0))

#Exemple2: using reshape
arr13 = np.random.rand(25)
print(arr13)
print(arr13.reshape((5,5)))
print(arr13)
arr13 = arr13.reshape((5,5))
print(arr13)

#Exemple2: max, argmax and argmin
print(arr13.max())
print(arr13.argmax())
print(arr13.argmin())