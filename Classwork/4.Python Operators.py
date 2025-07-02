#4. Python Operators.py

#1. Arthmetic operators

a=30
b=20
print("Addition(+):",a+b)   #Addition(+): 50
print("Subtraction(-):",a-b)  #Subtraction(-): -10
print("Multiplication(*):",a*b)  # Multiplication(*): 600
print("Division(/):",a/b)  #Division(/): 1.5
print("Floor Divison(//):",a//b)  #Floor Divison(//): 1
print("Modulus(%):",a%b)  #Modulus(%): 10
print("Exponentiation(**):",a**b)  # Exponentiation(**): 348678440100000000000000000000

#2.Comparision Operators

print("Equals to(==):",a==b)  #Equals to(==): False
print("Not Equals to(!=):",a!=b)  #Not Equals to(!=): True
print("Greater than(>):",a>b)  # Greater than(>): True
print("Less than(<):",a<b)  #Less than(<): False
print("Greater than or Equals to(>=):",a>=b)  #Greater than or Equals to(>=): True
print("Less than or Equals to(<=):",a<=b)  #Less than or Equals to(<=): False

#3.Assignment Operators

a=10
print(a)  # 10
a=a+10
print(a)  # 20
a=a-10
print(a)  # 10

''' var = va (operator) val
var (opr) = val'''

a=a+10
a+=10
print(a)  # 30

a=a+10
print(a) # 40

a+=10
print(a)  # 50.

a=a-10
a-=10
print(a)  # 30

a=a*10
a*=10
print(a)  # 3000

a=a//10
a//=10
print(a)  # 30

a=a**2
a**=2
print(a)  # 810000

a=a%10
a%=10
print(a)  # 0

a%7==0
a%=7
print(a)  # 0

# Logical Operators

6%2==0 and 6%3==0 and 6%4==0 and 6%6==0  # True
6%2==0 and 6%3==0 and 6%4!=0 and 6%6==0   # True
6%2==0 and 6%3==0 and 6%4==0 or 6%6==0   # True
6%2!=0 or 6%3!=0 or 6%4==0 or 6%6!=0   # False
6%2==0  # True
not 6%2==0  # True

# Membership Operators

s='vaishnavi'
print('a' in s) # True
print('v' in s) # True
print('h' in s) #True
print('e' in s) # False

# 
l=['apple','pineapple','tomato','carrot','pumpkin']  
print(l)  # ['apple', 'pineapple', 'tomato', 'carrot', 'pumpkin']
print('apple' in l)  # True
print('carrot' in l)  # True
print('tomato' in l)  # True
print('egg' in l)  # Flase

t=(1,2,3,4)
print(3 in t)  # True
print(4 in t)  # True
print(10 not in t)  # True

s={8,9,10,14,26,67}
print(8 in s) # True
print(14 in s)  # True
print(25 in s)  # Flase
print(100 not in s) # True

d={'name': 'vaishnavi','batch':15,'course':'DS'}
print('age' in d) # False 
print(30 in d) # False
print('dob' not in d) # True

a=[1,2,3,4,5]
b=[1,2,3,4,5]
a==b
print(a in b)  # False

# Identity Operator

c=a
a==c
print(a is c)  # True
print(id(a))  # 1431181312776
print(id(b))  # 1431150127368
print(id(c))  # 1431181312776
print(a is not b)  # True









