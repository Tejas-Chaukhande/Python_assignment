"""
WAP to assign 75 and 3.14 values to the variable and constant.
Check the values and type of those after the assignment.
"""
x=75
PI=3.14
print("x=",x,"PI=",PI)
print(type(x),type(PI))

----------------------------------------------------------------------
'''
WAP to define one complex number with lower case 'j' and
another one with the upper case 'J'.
Check the values and type of the variables after the assignment.
'''
x=2+3j
y=4+5J
print(x,y)
print(type(x),type(y))

---------------------------------------------------------------------
'''
WAP to assign 99 digits integer number to a variable.
Check the value, size and type of the variable after the assignment.
'''
import sys
num=12345678901234567890123456789012345678902345678901234567890123456789012345678901234567890123456789
print("num=",num)
print("size of num=",sys.getsizeof(num),"\ntype of num=",type(num))
