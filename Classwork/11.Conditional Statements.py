# Conditional Statements
'''
** Simple if **

if condition :
	# if-True-statements

** if-else **

if condition :
	# if-True-stmt
else:
	# flase-stmt

**  if-elif-else  **

if condition:
	#if-True-stmt
elif conditon-1:
	#cond stmts-1
elif condtion-2:
	#cond stmts-2
.
.
.
elif condtion-n:
	#cond-n stmts
else:
	#flase stmts

** Nested if **

if condition-outer:
	if condition inner:
		#if-True stmts
	else:
		#if-True stmts
else:
# Flase stmts

'''
# Simple if example #

s=input("Enter the status(R O G): ")
if s=='R':
    print("Stop")
if s=='O':
    print("Get Ready")
if s=='G':
    print("Gooo")

# if-else example #

items=['shoes','Smart Watch','Phone','airpods','toycar']
print('Welcome to Amazon store'.center(50,'*'))
searchinput=input("Enter the item:").lower()

if searchinput in items:
    print(f"{searchinput} found. Buy now.!!!")
else:
    print(f'{searchinput} is out of stock now. we will notify you.')

'''  # Output #
*************Welcome to Amazon store**************
Enter the item:shoes
shoes found. Buy now.!!!

Enter the item:airpods
airpods found. Buy now.!!!

Enter the item:toycar
toycar found. Buy now.!!!

Enter the item:tv
tv is out of stock now. we will notify you.

Enter the item:pendrive
pendrive is out of stock now. we will notify you.

'''

#  if-elif-else example #

# weekend Budget Plan

amount= int(input("Enter the amount you can spend on the weekend: "))
if amount>20000:
    print("Go to Goa")
elif amount>15000:
    print("Go for Shopping")
elif amount>10000:
    print("Clubbing")
elif amount>5000:
    print("Maintenance")
elif amount>2000:
    print("Cafe/Dinner")
elif amount>100:
    print("Go to a movie")
else:
    print("save the money & sleep at home")

'''  # Output #

Enter the amount you can spend on the weekend: 15000
Clubbing

Enter the amount you can spend on the weekend: 20000
Go for Shopping

Enter the amount you can spend on the weekend: 2500
Cafe/Dinner

Enter the amount you can spend on the weekend: 100
save the money & sleep at home

'''


# Nested if Example #
 
 # Grading  System

data={
    1:{'name':'praveen','attempt_status':False,'Python':0,'sql':0,'powerbi':0},
    2:{'name':'Harshith','attempt_status':True,'Python':80,'sql':60,'powerbi':71},
    3:{'name':'Varun','attempt_status':True,'Python':100,'sql':95,'powerbi':80},
    4:{'name':'Tarit','attempt_status':True,'Python':60,'sql':30,'powerbi':65},
    5:{'name':'Sheshu','attempt_status':True,'Python':90,'sql':80,'powerbi':96}
}

stu_id=int(input("Enter the student id: "))
if data[stu_id]['attempt_status']:
           total=data[stu_id]['python']+data[stu_id]['sql']+data[stu_id]['powerbi']
           print(f"Total Marks: {total}")
else:
    print(f'{data[stu_id]["name"] }is not attemptd the exam.')

'''
Enter the student id: 1
praveenis not attemptd the exam.

Enter the student id: 2
Total Marks: 211

Enter the student id: 3
Total Marks: 275

Enter the student id: 4
Total Marks: 155

Enter the student id: 5
Total Marks: 266

# total=(data[stu_id]['python']+data[stu_id]['sql']+data[stu_id]['powerbi'])/3

Enter the student id: 3
Total Marks: 91.66666666666667 (avg)

'''