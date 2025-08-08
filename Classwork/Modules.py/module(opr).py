# Modules - Group of relavent functions
#  User Defined 
# -- Methods to use/import the operatoions from another file-- #

#import Operators
import Operators as opr
#from Operators import *
#from Operators import add,sub,mul,div

a=int(input("Enter a: "))
b=int(input("Enter b: "))

op=input("Enter any Operator(+,-,*,/,%): ")

if op=='+':
    opr.add(a,b)
elif op=='-':
    opr.sub(a,b)
elif op=='*':
    opr.mul(a,b)
elif op=='/':
    opr.div(a,b)
elif op=='%':
    opr.mod(a,b)

