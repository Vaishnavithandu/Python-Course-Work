# 2.Variable rules and Assignments

myvar=10   #valid var
myVar=10   #valid var
my_var=10  #valid var
myvar1=10  #valid var
# my@var=10 (SyntaxError: cannot assign to expression here. Maybe you "==" or ":=" insteead of

myvar=10  # valid Var
Myvar=10  # valid Var
#1myvar=10  (SyntaxError: invalid decimal literal)
_myvar=10  # valid Var
#@myvar=10  (invalid syntax)
#my var=10  # SyntaxError: invalid syntax.

myvar=10  #case-sensitive
Myvar=20  #case-sensitive
print(myvar,Myvar) # 10  20

a=10 #Assignment
a,b,c=10,20,30 #Multiple Assignment
print(a,b,c) # 10  20  30

a=b=c=10   # Same Value Assignment
print(a,b,c)

a=10
b=20
print("Before Swapping(a,b):",a,b) # 10 20
a,b=b,a
print("After Swapping(a,b):",a,b)  # 20 10

del a
'''Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    del a
NameError: name 'a' is not defined'''

b=20 # Reassignment
print(b) # 20


