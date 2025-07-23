data={'current_balance':46578,'history':[]}
def check_balance():
    print(f"Current Balance: {data['current_balance']}")
def deposit():
    amount=int(input("Enter the amount: "))
    data['current_balance']+=amount
    data['history'].append(f'Deposited - ${amount}')
    print(f'Deposited Successfully - ${amount}')
def withdraw():
    amount=int(input("Enter the amount: "))
    if data['current_balance']>=amount:
        data['current_balance']-=amount
        data['history'].append(f'withdraw - ${amount}')
        print(f'Withdraw Successfully - ${amount}')
    else:
        print("Ins blnc")
def history():
    print("Transactions")
    for i in data['history']:
        print(i)
while True:
    print('Welcome to ATM'.center(30,'*'))
    print('1.Check Balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.History')
    print('0.Exit')

    op=int(input("Enter your choice: "))
    if op==0:
        print("======Thankyou======")
        break
    elif op==1:
        check_balance()
    elif op==2:
        deposit()
    elif op==3:
        withdraw()
    elif op==4:
        history()
    else:
        print("Invalid choice. Try Again")

'''
********Welcome to ATM********
1.Check Balance
2.Deposit
3.Withdraw
4.History
0.Exit
Enter your choice: 2
Enter the amount: 56476
Deposited Successfully - $56476
********Welcome to ATM********
1.Check Balance
2.Deposit
3.Withdraw
4.History
0.Exit
Enter your choice: 2
Enter the amount: 21334
Deposited Successfully - $21334

********Welcome to ATM********
1.Check Balance
2.Deposit
3.Withdraw
4.History
0.Exit
Enter your choice: 2
Enter the amount: 67869
Deposited Successfully - $67869

********Welcome to ATM********
1.Check Balance
2.Deposit
3.Withdraw
4.History
0.Exit
Enter your choice: 3
Enter the amount: 66543
Withdraw Successfully - $66543

********Welcome to ATM********
1.Check Balance
2.Deposit
3.Withdraw
4.History
0.Exit
Enter your choice: 3
Enter the amount: 7609
Withdraw Successfully - $7609

********Welcome to ATM********
1.Check Balance
2.Deposit
3.Withdraw
4.History
0.Exit
Enter your choice: 2
Enter the amount: 87659
Deposited Successfully - $87659

********Welcome to ATM********
1.Check Balance
2.Deposit
3.Withdraw
4.History
0.Exit
Enter your choice: 3
Enter the amount: 8768
Withdraw Successfully - $8768

********Welcome to ATM********
1.Check Balance
2.Deposit
3.Withdraw
4.History
0.Exit
Enter your choice: 1
Current Balance: 196996

********Welcome to ATM********
1.Check Balance
2.Deposit
3.Withdraw
4.History
0.Exit
Enter your choice: 4
Transactions
Deposited - $56476
Deposited - $21334
Deposited - $67869
withdraw - $66543
withdraw - $7609
Deposited - $87659
withdraw - $8768

********Welcome to ATM********
1.Check Balance
2.Deposit
3.Withdraw
4.History
0.Exit
Enter your choice: 0
======Thankyou======


'''