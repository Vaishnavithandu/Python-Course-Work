'''
for i in range(5):  #(i=rows)
    for j in range(5):  #(j=col)
        print('*',end=' ')
    print()
'''

'''
for i in range(5):
    for j in range(5):
        print(i,end=' ')
    print()
'''
'''
for i in range(5):
    for j in range(5):
        print(j,end=' ')
    print()
'''
'''
for i in range(5):
    for j in range(i+1):
        print(i,end=' ')
    print()   
'''
'''
for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()
'''
'''
n= int(input("Enter the Size: "))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()
'''
'''
n= int(input("Enter the Size: "))
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()
'''
'''
n= int(input("Enter the Size: "))
for row in range(n):
    for spa in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print('*',end=' ')
    print()
'''
'''
n= int(input("Enter the Size: "))
for row in range(n):
    for spa in range(n-row-1):
        print('*',end=' ')
    print()
'''
'''
n= int(input("Enter the Size: "))
for row in range(n):
    for spc in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()
for row in range(n):
    print('  '*row,end=' ')
    print("*"*(n-row),end=' ')
    print()
 '''
'''
n= int(input("Enter the Size: "))
for row in range(n):
    if row<=n//2:
        print('*'*(row+1),end=' ')
    else:
        print('*'*(n-row),end=' ')
    print()


Enter the Size: 15
* 
** 
*** 
**** 
***** 
****** 
******* 
******** 
******* 
****** 
***** 
**** 
*** 
** 
*

'''

'''
n= int(input("Enter the Size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("*",end=' ')
        else:
            print("  ",end=' ')
    print()

Enter the Size: 8
* * * * * * * * * * *
*                   * 
*                   * 
*                   * 
*                   * 
*                   * 
*                   * 
* * * * * * * * * * *
'''
'''
n= int(input("Enter the Size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1: or row==n//2 or col==n//2:
            print("*",end=' ')
        else:
            print("  ",end=' ')
    print()
'''
    
'''
n= int(input("Enter the Size: "))
for row in range(n):
    for col in range(n):
        if row==col or row+col==n-1:
            print("*",end=' ')
        else:
            print("  ",end=' ')
    print()

Enter the Size: 8
*                   * 
   *             *    
      *       *       
         * *          
         * *          
      *       *       
   *             *    
*                   *
'''

n= int(input("Enter the Size: "))
for row in range(n):
    for col in range(n):
        if (row==0 and col!=0) or row==n-1 or row==n//2 or (col==0 and row<=n//2) or (col==n-1 and row>=n//2):
            print("*",end=' ')
        else:
            print("  ",end=' ')
    print()
