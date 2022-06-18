import numpy as np

#1 - Create what is asked for

#Create an array with 10 zeros
arr1_10_zeros = np.zeros(10)
print(arr1_10_zeros)

#Create an array with 10 ones
arr2_10_ones = np.ones(10)
print(arr2_10_ones)

#Create an array with 10 fives
arr3_10_fives = np.ones(10)
arr3_10_fives = arr3_10_fives*5
print(arr3_10_fives)

#Create an array of integers from 10 to 50
arr4_10_to_50 = np.arange(10,51)
print(arr4_10_to_50)

#Create an array of pairs integers from 10 to 50
arr5_pairs_10_to_50 = np.arange(10,51,2)
print(arr5_pairs_10_to_50)

#Create matrix 3x3 with random values from 0 to 8
mtx1_rand_0_to_8 = np.random.randint(0,9,9)
mtx1_rand_0_to_8 = mtx1_rand_0_to_8.reshape(3,3)
print(mtx1_rand_0_to_8)

#Create random numbers between 0 and 1
arr6_rand_0_to_1 = np.random.rand(10)
print(arr6_rand_0_to_1)

#Create 25 random array from normal distribution
arr7_normal_distr = np.random.randint(0,26,25)
print(arr7_normal_distr.reshape(5,5))

#Create 10x10 matrix with 0.01 step
mtx2_10x10_001_step = np.arange(0.01,1.01,0.01)
mtx2_10x10_001_step = mtx2_10x10_001_step.reshape(10,10)
print(mtx2_10x10_001_step)

#Create an array equaly distanced with 20 elements between 0 and 1
arr7_rand20_0_to_1 = np.linspace(0,1,20)
print(arr7_rand20_0_to_1)

#2 - Do what is asked with each the matrix you receive

#Display from line 3 and column 3 ahead
mat1 = np.arange(1,26).reshape(5,5)
print(mat1)
print(mat1[2:,1:])

#Display the item [3,4]
mat1 = np.arange(1,26).reshape(5,5)
print(mat1[3,4])

#Dysplay the first 3 items from column 1
mat1 = np.arange(1,26).reshape(5,5)
print(mat1[0:3,1].reshape(3,1))

#Dysplay line 4
mat1 = np.arange(1,26).reshape(5,5)
print(mat1[4,:])

#Dysplay line 3 and 4
mat1 = np.arange(1,26).reshape(5,5)
print(mat1[3:5,:])
print('\n')

