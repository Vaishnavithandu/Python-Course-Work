# 7.Tuples.py

t=() # tuple can be declared in two ways 1. by parentheses, 2. by context tuple()
t=tuple()
t=(1,2,3,4,5)
print(t)  # (1, 2, 3, 4, 5)
      
t=(1,1,1,1,2,3) # it allows duplicates
print(t)  # (1, 1, 1, 1, 2, 3) (same in order)

t=(1,2,3,4)
t.add(12)  # it is immutable
print(t) # AttributeError: 'tuple' object has no attribute 'add'

# Accessing Tiple Elements

t=(10,20,30,40)
print(t[2]) # 30   

# Negative Indexing

t= (10, 20, 30, 40)
print(t[-1]) # 40

# Slicing

t= (10, 20, 30, 40, 50)
print(t[1:4]) # (20, 30, 40)

# Operations on Tuples
 # Concatenation
t1 = (1, 2)
t2 = (3, 4)
t= t1 + t2 # (1, 2, 3, 4)

# Repetition
t=(1, 2)
print(t * 3) # (1, 2, 1, 2, 1, 2)

# Membership Testing
t = (1, 2, 3)
print(2 in t) # True
print(5 not in t) # True

# Tuple Unpacking

t = (1, 2, 3) # Assign tuple elements to multiple variables.
a, b, c = t
print(a, b, c) #  1 2 3

# Tuple Methods
  # Count
t=(1,2,3,3,4)
print(t.count(3))  # 2

# Index
t=(1,2,3,4)
print(t.index(3)) # 2
print(t.index(4)) # 3
print(t.index(5)) # gives an error x not in tuple

# Built-in functions for Tuple

t=(1,2,3,45,56,76,34,545)
print(len(t)) # 8

t=(1,2,3,45,56,76,34,545)
print(max(t)) # 545

t=(1,2,3,45,56,76,34,545)
print(min(t)) # 1

t=(1,2,3,43,32)
print(sum(t)) # 81

# covertion of list into tuple

t=[1,2,3,4,5]
print(type(t)) # <class 'list'>
print(tuple(t)) # (1,2,3,4,5)

# how can we add elements into tuple

t=(1,2,3,4,5,[1,2,3,4])  
print(t.append(23)) 

'''Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t.append(23)
AttributeError: 'tuple' object has no attribute 'append' '''

t.extend([2,3]) 

''' Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t.extend([2,3])
AttributeError: 'tuple' object has no attribute 'extend' '''

t[5].append(8)
print(t)  # (1, 2, 3, 4, 5, [1, 2, 3, 4, 8])

# here we have a list in the index 5.
# we are adding the elements in list which is at index 5.

t.append(6) # we can append it gives an error
print(t[5].append(14)) # we can append
# (1, 2, 3, 4, 5, [1, 2, 3, 4, 8,14])

print(del t[3]) # 'tuple' object doesn't support item deletion
print(del t[5][2]) # (1, 2, 3, 4, 5, [1, 2, 4, 8, 14])

# we have list inside the tuple we are changing the list.
# we can make changes inside mutable (list,set,dic)
# we cann't change the structure of tuple.
# we cann't delete any object/element from tuple.
# we can del an object inside list in a tuple.

t=(1,2,{5,6})
print(t.add(3)) # 'tuple' object has no attribute 'append'
print(t[2].add(3)) # (1, 2, {3, 5, 6})

print(del[0]) # 'tuple' object doesn't support item deletion
print(del t[2]) # 'tuple' object doesn't support item deletion
print(del t[2][0]) # 'set' object doesn't support item deletion bcz it's immutable

t=(1,2,3,{"name":"vaish","branch":"CSE"})
print(t.add(4)) # AttributeError: 'tuple' object has no attribute 'add'
print(t[3]["age"] = "16")
print(t[3]["age"]) # 16
print(t) # (1, 2, 3, {'name': 'vaish', 'branch': 'CSE', 'age': '16'})




