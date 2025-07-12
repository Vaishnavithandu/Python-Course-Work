# Person has vowels in index[0] the print covid +ve

name=input("Enter the name: ")
vowels='AEIOUaeiou'
if name[0] in vowels:
    print("Covid +ve.Take Care")
else:
    print("Congrats!! You are Safe")

'''
Enter the name: Abhi  
Covid +ve.Take Care

Enter the name: vaishnavi
Congrats!! You are Safe

'''

# Ticket Booking System

seats={
    'L1':True,
    'L2':True,
    'U1':True,
    'U2':False
    }
print("Bus Seats:", seats.keys())
seatid=input("Enter the seat number to book: ").upper()
if seatid in seats:
    if seats[seatid]:
        print("seat is avaliable.You can book")
    else:
        print("seat is not avaliable.Pick other one")
else:
    print("Choose the seat number properly")

'''
Enter the seat number to book: L1
seat is avaliable.You can book

Enter the seat number to book: U2
seat is not avaliable.Pick other one

Enter the seat number to book: S1
Choose the seat number properly

'''

# Positive or Negative

num=int(input("Enter the number: "))
if num>0:
    print("Positive number")
elif num<0:
    print("Negative number")
else:
    print("Zero")

'''
Enter the number: 5
Positive number

Enter the number: 20
Positive number

Enter the number: -15
Negative number

'''

# Odd or Even

num=int(input("Enter a number: "))
if num%2==0:
    print(f'num is even number')
else:
    print(f'num is odd number')

'''
Enter a number: 20
(num) is even number

Enter a number: 21
num is odd number

Enter a number: 34
num is even number

'''

# Year is a Leap Year or Not

year=int(input("Enter the year: "))
if year%400==0 or year%4==0 and year%100!=0:
    print(f'year is leap year')
else:
    print(f'year is non leap year')

'''
Enter the year: 2004
year is leap year

Enter the year: 2009
year is non leap year

Enter the year: 2024
year is leap year

Enter the year: 2029
year is non leap year

Enter the year: 3035
year is non leap year

'''

