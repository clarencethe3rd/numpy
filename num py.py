import numpy as np
num = [1,2,3,4,5]
print(num)
print(type(num))
num_array = np.array(num)
print(num_array)
print(type(num_array))

double_num = []
for i in num:
    double_num.append(i*2)
print(double_num)
double_array = num_array*2
print(double_array)
#array of 0s
zero = np.zeros(5,int)
print(zero)
zero_2d = np.zeros((3,4),int)
print(zero_2d)
#array of 1s
one_2d = np.ones((2,3,5),int)
print(one_2d)
#find the dimention
print(zero.ndim)
print(zero_2d.ndim)
print(one_2d.ndim)
#shape
print(zero.shape)
print(zero_2d.shape)
print(one_2d.shape)
print(zero_2d.shape[0])
#total items
print(zero.size)
print(zero_2d.size)
print(one_2d.size)