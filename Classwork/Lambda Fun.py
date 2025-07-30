'''
map:when ever we need to iterate we need map 
var = lambda arg: expr
eval-when they ask with syntax

'''

evenorodd_lambda=lambda n: "Even" if n%2==0 else "Odd"
print("evenorodd_lambda",evenorodd_lambda(3))

v='aeiou'
squl_lambda=list(map(lambda i: '*' if i in v else i,"python"))
print("squl_lambda",''.join(squl_lambda))

# Get maxximum num of two numbers

maxnum=lambda a,b: a if a>b else b
print(maxnum(45,67))

# Multiply two numbers

mulnum=lambda a,b: a*b
print(mulnum(4,5))

# sort a list of tuples by 2nd element

s=sorted([(1,2),(3,5),(2,1)],key=lambda i:i[1])
print(s)

l=["vaish","lasya","Keer"]
s=sorted(l,key=lambda i:i[-1])
print(s)

l=["vaish","lasya","Keer"]
s=sorted(l,key=lambda i:i[-2])
print(s)

# Filter function
  
  #filter even

l=[1,2,3,4,5,6]
even=list(filter(lambda i: i%2==0,l))
print(even)

 # remove all zeroes
l=[1,2,0,0,0,3,0,0,4,5,0,6,0,0]
e=list(filter(lambda i:i!=0,l))
print(e)

# real time ex:

data ={
    'laptopA':{'available':True,'price':40000},

}
l=list(filter(lambda i: data[i]['available'],data))
k=list(filter(lambda i: data[i]['price']<50000,data))
print(l,k)

# general list comprehension 

# when we are dealing with list and for loop,append we can use this to shorten the code
#1
n=int(input("Enter a number: "))
l=[]
for i in range(1,n+1):
    if i%2==0:
       l.append()
print(l)

k=[i for i in range(1,n+1) if i%2==0] #--append elements to be mentioned
print(l)

#2
for i in range(10):
    if i%2==0:
       l.append()
print(l)

k=[i for i in range(10) if i%2==0] #--append elements to be mentioned
print(l)

#3
d=[]
for i in range(5):
       d.append(i*i)
print(l)

d=[i*i for i in range(5)]

#4
j='python'
vol='aeiouAEIOU'
o=[]
for i in j:
    if i in v:
        o.append(i)

o=[i for i in j if i in v]

#5
l=[]
for i in s:
    if i.islower():
        l.append(i)

l=[i for i in s if i.islower()]

#6
l=[1,2,3,4.0,0,0,8,0]
res=[]
for i in l:
    if i!=0:
        res.append(i)

res=[i for i in l if i!=0]

# append 0 - if it is alp 
s='123576hdsg73kh'
l=[]
for i in s:
    if i.isdigit():
        l.append(i)
    else:
        l.append(0)

# SET

s= {i for i in range(5)}
print(s)

# Dict

s={i:i**2 for i in range(5)}
print(s)
        
# Tuple:
s= (i for i in range(5))
print(s) # Error

s= tuple(i for i in range(5)) # if we want to do it with tuple.but generally don't go with tuple as we don't do any operations on it(append,...)
print(s)

l={key:val for key in seq} # dict
l=[val for val in seq] # list
l={val for val in seq} # set

names=['vaish','lasya','sahithi','lakshmi']
d={i:'Abesnt' for i in names}
print(d)

{1:1,2:4,3:6,4:16}

d={i:i**2 for i in range(1,5)}
print(d)