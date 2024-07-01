# What will be the output of following statements
print({1, 2, 3, 5} - {3, 4, 7, 8})     #o/p:- {1,2,5}
#print({1, 2, 3, 5} + {3, 4, 7, 8})    #addition will not work on sets

# What will be the output of following programs
print('Hi ' + 'Anil')                #o/p:- Hi Anil
print([1, 2] + [3, 4])               #o/p:- [1,2,3,4]
#print('Hi' + [1, 2])                 #Error: concatination can work only on string type

# What will be the output of following programs
print((1, 2, 3) * 4)     #o/p:- (1,2,3,1,2,3,1,2,3,1,2,3)
print(8 // 3)            #O/p:-  2
print(21 % 6)            #o/p:- 3

# What will be the output of following programs
a = 7
a /= 2
print(a)  # 3.5
b = 5
print(b > 5 and b < 10)  # Also write the short form for this expression  o/p:-False
#print(5<b<10)           #short-hand
print(5 < b < 10)        #op:-False


# Write the output of following programs
print(4 and 6)      #o/p:- 6
print(1 or 5)       #o/p:- 1
print(not 7)        #o/p:- False

# what is the output of following programs
print(2 not in [3, 4, 5, 2, 9])        #o/p:- False
print([1, 2, 5, (1, 2)] in ['hi', 3, 4, 5, 2, 9, [1, 2, 5, (1, 2)]])  #o/p:- True

# what is the output of following programs
a = 400.30123
b = 400.30123
print(a is b)        #True

i = 23
j = 23
print(i is j)      #True
print(i == j)      #True

a1 = 999
b1 = 999
print(a1 is b1)   #false
print(a1 == b1)   #True

y = 4
z = -4
print(y == z)     #False

s1 = 4096 * 'a'
s2 = 4096 * 'a'
print(s1 is s2)     #True

# write the output of following programs
a = 2
b = 11
print(a & b)      # o/p:- 2
print(a | b)      # o/p:- 11
print(a ^ b)      # o/p:- 9
print(~b)         # o/p:- -12
print(a << 3)     # o/p:- 16
print(b >> 2)     # o/p:- 2

# write the output of following programs
print(+-4)        #o/p:- -4
print(--4)        #o/p:-  4
a = [1, 2, 3]
print(2 * a[1] << 2 > 8 and 9)        #o/p:- 9
print(2 * 3 - 3 ** 2 ** 1 & 5 // 2 + (4 + 2) or 5)    #o/p:- 8
