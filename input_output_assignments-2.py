"""
Write a Python program that asks the user to enter their name using the input() function,
and then prints a greeting message using the print() function. 
For example, if the user enters "Alice", the program should print "Hello, Alice!"
"""
name=input("Enter the name: ")
print("\""+"Hello,",name+'!'+"\"")
------------------------------------------------------------------------------------
"""
WAP to print the following output in single of code
'Hello' : dynamic using input()
'Anil' : dynamic using input()
Note: please use print() to combine the output
Final output format:
Hello Anil
Hi Anil
I Love Python
"""


a=input("Enter the Hello: ")
b=input("Enter the name: ")
print(a,b,sep=' ')
x=input("Enter the Hi:")
print(x,b)
y=input("Enter I Love Python:")
print(y)

"""
Write a script that asks the user for their name, age, and favorite color, 
and then prints a single sentence summarizing this information in a formatted string.
"""
name=input("Enter the name: ")
age=int(input("Enter the age: "))
fav_col=input("Enter the favorite color:")

print("My name is ",name,"My age is ",age,"My fovorite color is ",fav_col,sep='\t')
