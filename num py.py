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
#array with numbers with range
a1 = np.arange(1,20,3)
print(a1)
#shuffleling items
print(np.random.permutation(a1))
print(np.random.permutation(a1))
print(np.random.permutation(a1))
#array of random numbers
print(np.random.randint(1,50,10))
a2 = np.random.randint(30,50,(3,4))
print(a2)
#reshaping an array
print(a2.reshape(2,6))
print(a2.reshape(1,12))
print(a2.reshape(12))
#sort arrays
a3 = np.random.randint(1,50,10)
print(a3)
print(np.sort(a3))
#slicing
print(a3[2:5])
print(a3[:7])
print(a3[1:])
print(a3[::2])
print(a3[::-1])
#slicing 2d array
print(a2)
print(a2[1:3,1:4])
#selecting indexes
print(a3[[2,3,6,2,9]])
print(a3)
#conditional slicing
print(a3[a3%2==0])
print(a3[a3>20])
#evaluating expressions(volume of cylinders)
r = np.random.randint(5,15,20)
h = np.random.randint(11,20,20)
v = r**2*h*np.pi
print(v)
