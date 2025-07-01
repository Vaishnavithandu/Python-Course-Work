# 3. Python Data Types

# int
a=10
print(type(a)) # <class 'int'>

# float
a=10.0
print(type(a)) # <class 'float'>

# complex
a=3+3j
print(type(a)) # <class 'complex'>

# String
name='vaishnavi'
print(type(name)) # <class 'str'> 

name="vaishnavi"
print(type(name)) # <class 'str'>

name='''vaishnavi''' # string can be in single, double and triple quotes
print(name)  # vaishnavi

print("vaishnavi and sahithi")   # vaishnavi and sahithi
print(" 'vaishnavi' and 'sahithi' ")  #  'vaishnavi' and 'sahithi' 

# list
fav=[] # declaration of string can be done in two ways 1. square brackets, 2. context list()
fav=list()
fav=[1, 2.3, 3+5j, "string",[] ]  # lists can contain heterogeneous data types or objects
print(fav)   # [1, 2.3, (3+5j), 'string', []]  

fav.append("hello")  # it is mutable
print(fav)   # [1, 2.3, (3+5j), 'string', [], 'hello']

fav=[1,2,3,4,5]  
print(fav)  # [1, 2, 3, 4, 5] 
print(type(fav)) # <class 'list'>

l=[1,2,3,4,4,4]
print(l)  # [1, 2, 3, 4, 4, 4]  (it is a ordered collection of elements) 

# tuple
t=() # tuple can be declared in two ways 1. by parentheses, 2. by context tuple()
t=tuple()
t=(1,2,3,4,5)
print(t)  # (1, 2, 3, 4, 5)
      
t=(1,1,1,1,2,3) # it allows duplicates
print(t)  # (1, 1, 1, 1, 2, 3) (same in order)

t=(1,2,3,4)
t.add(12)  # it is immutable
print(t) # AttributeError: 'tuple' object has no attribute 'add'

# set
s={1,1,1,1,1,2,2,3}
print(s)  # {1, 2, 3}  (doesn't allow duplicates)
s={100,20,2,3,1,6,1,7,3,2,1786}
print(s)  # {1, 2, 3, 100, 6, 7, 20, 1786} ( unordered collection of elements na it's mutable)

# frozenset
s=frozenset({1,2,3,4})
print(type(s))  # <class 'frozenset'>
s.add(12) # immutable
''' Traceback (most recent call last):
  File "D:/Users/laxma/Desktop/Python-course-work/3. Python Data Types.py", line 53, in <module>
    s.add(12)
AttributeError: 'frozenset' object has no attribute 'add' '''

# Dictionary
d={'name': 'vaishnavi', 'course': 'DS', 'batch': '15', 'skills': ['py', 'sql', 'bowerbi']}
print(d)  # {'name': 'vaishnavi', 'course': 'DS', 'batch': '15', 'skills': ['py', 'sql', 'bowerbi']} 
print(d['name'])  # vaishnavi    (dic stores data in key-value pairs,where each unique key maps to a specific value)
print(d['course'])  # DS         (keys are immutable,only values are mutable ) 
print(d['skills'])  # ['py', 'sql', 'bowerbi']

# Boolean
is_logged_in=True
is_payment_succesful= False # check conditions T/F
print(type(is_logged_in))  # <class 'bool'>

# None
randomvar=None
tracking_number=None  # represents a null or missing value and can be updated later
print(type(randomvar))  # <class 'NoneType'>

randomvar='vaish'
print(randomvar)  # vaish
print(type(randomvar))  # <class 'str'>





      





