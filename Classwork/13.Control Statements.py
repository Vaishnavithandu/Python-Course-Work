# Control Statements

# Range Function
for i in range(1,20):
    print(i)
for i in range(1,20,2):
    print(i)
'''
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

1
3
5
7
9
11
13
15
17
19

'''
 # How to print a Table

num=int(input("Enter the Table number: "))
for i in range(1,21):
    print(f'{num} * {i} = {num*i}')

'''
Enter the Table number: 18
18 * 1 = 18
18 * 2 = 36
18 * 3 = 54
18 * 4 = 72
18 * 5 = 90
18 * 6 = 108
18 * 7 = 126
18 * 8 = 144
18 * 9 = 162
18 * 10 = 180
18 * 11 = 198
18 * 12 = 216
18 * 13 = 234
18 * 14 = 252
18 * 15 = 270
18 * 16 = 288
18 * 17 = 306
18 * 18 = 324
18 * 19 = 342
18 * 20 = 360

'''

# Count of a char in a string

s='Praveen Harshith Ramya Sudha Kalyani'
n=len(s)
ch=input("Enter the char: ").lower()
for i in range(n):
    if s[i]==ch:
        print(ch,i)

'''
Enter the char: a
a 2
a 9
a 18
a 21
a 27
a 30
a 33

'''

# Check whether item is present in the list or not

Products=['cycle','watch','mobile','laptop','mouse']
items=input("Enter the item: ").split()
for i in items:
    if i in Products:
        print(Products.index(i),i)
    else:
        print(f"{i} is not available! ")

'''
Enter the item: cycle mobile laptop watch
0 cycle
2 mobile
3 laptop
1 watch

Enter the item: airpods
airpods is not available!

'''

# While else loop exmpl

email,pswd= 'xyz@gmail.com','xyz@123'
max_attempts=5

while max_attempts>0:
    useremail=input("Enter the email id: ")
    password=input("Enter the password: ")
    if useremail==email and pswd==password:
        print("Login Successful")
        break
    else:
        print("Invalid Password")
    max_attempts-=1
else:
    print("Try after some time")

'''
Enter the email id: scvd@gmail.com
Enter the password: dadqw
Invalid Password
Enter the email id: scvd@gmail.com
Enter the password: dweq
Invalid Password
Enter the email id: scvd@gmail.com
Enter the password: dsdf
Invalid Password
Enter the email id: scvd@gmail.com
Enter the password: fewfe
Invalid Password
Enter the email id: scvd@gmail.com
Enter the password: fewfew

Invalid Password
Try after some time

Enter the email id: xyz@gmail.com
Enter the password: dbaj   
Invalid Password

Enter the email id: xyz@gmail.com
Enter the password: xyz@123

Login Successful

'''