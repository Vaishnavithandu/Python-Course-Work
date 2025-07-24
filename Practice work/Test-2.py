'''

# 1.Automated Salary Tax Calculator #

salary=int(input())
if 0 < salary <=250000:
    print("No Tax")
elif 250001<= salary <= 500000:
    print(salary*0.05)
elif 500001<= salary <= 1000000:
    print(salary*0.2)
elif salary>1000000:
    print(salary*0.3)
 
    
# 2.Movie Ticket Pricing System #

n=int(input())
total_price=0
for i in range(n):
    age=int(input())
    if age<5:
        continue
    elif 5<=age<=18:
        total_price+=100
    elif 19<=age<=60:
        total_price+=150
    elif age>60:
        total_price+=120

print(total_price)


# 3.Electricity Bill Generator #

units=int(input())

if units<=100:
    print(units*1.5)

elif 101<=units<=200:
    bill=(100*1.5)+(units-100)*2.5
    print(bill)

elif 201<=units<=500:
    bill=(100*1.5)+(100*2.5)+(units-200)*4
    print(bill)

elif units>500:
    bill=(100*1.5)+(100*2.5)+(300*4)+(units-500)*6
    print(bill)

    
# 4.Car Parking Fee Calculator #

hr=int(input())
if hr<=2:
    print(30)
elif 2<hr<24:
    print(30+(hr-2)*10)
elif hr==24:
    print(200)

    
# 5.Product Inventory Checker (Nested Conditionals) #

product=input()
qua=int(input())
if qua==0:
    print(f'{product}: Out of Stock')
elif 1<=qua<=10:
    print(f'{product}: Low Stock')
elif 11<=qua<=50:
    print(f'{product}: In Stock')
elif qua>50:
    print(f'{product}: Overstocked')

    
# 6.Pattern – Row-wise Alternating 0 and 1 (Nested Loops) #

  0 1 2 3 4 
0 0 1 0 1 0
1 1 0 1 0 1
2 0 1 0 1 0
3 1 0 1 0 1
4 0 1 0 1 0

00=0%2=0
02=2
04=4
11=2
13=4
20=2
22=4
24=6
31=4
33=6
40=4
42=6
44=8

n=int(input())
for row in range(n):
    for col in range(n):
        print((row+col)%2,end=' ')
    print()

    
# 7.Gym Subscription Billing (Menu Driven Program) #

while True:
    print("""1. Monthly – ₹500 
2. Quarterly – ₹1300 
3. Yearly – ₹5000
0.Exit
""")
    ch=int(input())
    if ch==0:
        break
    people=int(input())
    if ch==1:
        print(500*people)
    elif ch==2:
        print(1300*people)
    elif ch==3:
        print(5000*people)
    else:
        print("Invalid Choice")
    
        
# 8.Billing Bot – Apply Discount Based on Amount #

amount=float(input())
discount_acc=0
if 0<amount<=990:
    pass
elif 1000<=amount<=4999:
    discount_acc=amount*0.05
elif 5000<=amount<=9999:
    discount_acc=amount*0.1
elif amount>=10000:
    discount_acc=amount*0.15

print(amount-discount_acc)


# 9.ATM PIN Verification with Blocking Logic #

stored_pin=1234
for i in range(3):
    pin=int(input())
    if pin==stored_pin:
        print("Access Granted")
        break
else:
    print('ATM Blocked. Try Again Later')

    
# 10.Bus Booking System – Track Full and Empty Seats #

total_seat=int(input())
booked_seats=input().split()
print(f'Total Seats: {total_seat}')
print(f'Booked: {len(booked_seats)}')
print(f'Available: {total_seat-len(booked_seats)}')

'''
