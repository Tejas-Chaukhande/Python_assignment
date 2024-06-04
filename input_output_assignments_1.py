"""
Assignment-1:
WAP to print the following output using print function
1 2 3 4 5
"""
a,b,c,d,e=1,2,3,4,5
print(a,b,c,d,e,sep=' ')

------------------------------------------------------
"""
Assignment-2:
# WAP to print the following output using print function
1 2 3 => Same line, one space between each value
4    5 => Same line, tab space between each value

"""
print(1,2,3,sep=' ')
print(4,5,sep='\t')

------------------------------------------------------
"""
Assignment-3:
WAP to print 'Hi' on the screen
and 'I Love Python' to the file using the print function
"""

fp=open("sample.txt",'w')
print("Hi",sep='\n')
print("I Love Python",file=fp)
