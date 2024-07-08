# Assignment-1: if condition
# Check if a person is eligible to vote based on their age
# Input: Age of the person
age=int(input("Enter the age of the Person: "))
# Check if the person is eligible to vote
if(age>=18):
    print("Person is Eligible to vote")
else:
    print("Person is not Eligible to vote")


# Assignment-2: if else condition
# WAP that checks whether a number is positive or negative

num=int(input("Enter the number: "))
if(num<0):
    print("Number is negative")
else:
    print("Number is Positive")

# Assignment-3: if else condition
# WAP that Checks if a given number is even or odd
num1=int(input("Enter the number: "))
if(num1%2==0):
    print("Number is Even")
else:
    print("Number is Odd")

# Assignment-4: nested if condition
# WAP to find the greatest of 3 numbers
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))

if(a>b and a>c):
    print(f"{a} is greatest")
elif(b>c):
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")


# Assignment-5: nested if else condition
"""

Movie Ticket Pricing
Imagine a movie theater that offers different ticket prices based on the age of the customer and the time of the day.
The rules might be as follows:

Regular price: $10
Children under 12 and seniors over 65 get a 50% discount.
Matinee show (before 5 PM) offers a 25% discount to all.
"""
age=int(input("Enter the age: "))
time=int(input("Enter the time in: "))
zone=input("Input time zone am/pm: ")
amt=10
if(age<12 or age>65):
    amt=amt*0.5
    if(time<5 and zone=="pm" or zone=="PM"):
        amt=amt*0.75

print("your ticket price is: $",amt)



# Assignment-6: nested if else condition
# WAP to find the biggest country among 3 based on the population

country_1_pop=int(input("Enter the population for country1: "))
country_2_pop=int(input("Enter the population for country2: "))
country_3_pop=int(input("Enter the population for country3: "))

if(country_1_pop > country_2_pop and country_1_pop > country_3_pop):
    print("Country_1 population is biggest")
elif(country_2_pop > country_3_pop):
    print("Country_2 population is biggest")
else:
    print("Country_3 population is biggest")
