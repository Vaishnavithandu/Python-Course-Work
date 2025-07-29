'''
var = lambda arg: expr
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