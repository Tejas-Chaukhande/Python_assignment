""" Assignment-1:
 WAP to assign 3 values (string, int, float)
 to 3 variables (Student_name, Roll_Number, Percentage_of_marks).
 print the values using print function.
 """
Student_name=input("Enter the student name: ")
Roll_Number=int(input("Enter the Roll number: "))
Percentage=float(input("Enter the Percentage: "))

print(Student_name,Roll_Number,Percentage,sep='\n')
 

-------------------------------------------------------------------

"""Assignment-2:
WAP to assign value 6 to two different variables (example: a1, b1)
using single line of code.
Check the variable values and memory address"""


a,b=6,6
print(id(a),id(b),sep='\t')

-----------------------------------------------------------------

"""
Assignment-3:
WAP to assign multiple values to multiple variables
in single line of code
"""
a,b,c,d,e,f=10,20,30,40,50,60
print(a,b,c,d,e,f,sep='\t')
