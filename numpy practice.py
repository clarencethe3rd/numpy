import numpy as np
print("1: linear expression")
print("2: quadratic expression")
num = int(input("choose 1 or 2: "))
if num == 1:
    print("ax + b")
    a = int(input("enter value for a: "))
    b = int(input("enter value for b: "))
    x = np.arange(1,11)
    a1 = a*x+b
    print(a1)
    
if num == 2:
    print("ax^2 + bx + c")
    a = int(input("enter value for a: "))
    b = int(input("enter value for b: "))
    c = int(input("enter value for c: "))
    x = np.arange(1,11)
    a1 = a*x**2+b*x + c
    print(a1)