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

# Built-in functions for Tuple

t=(1,2,3,45,56,76,34,545)
print(len(t)) # 8

t=(1,2,3,45,56,76,34,545)
print(max(t)) # 545

t=(1,2,3,45,56,76,34,545)
print(min(t)) # 1

t=(1,2,3,43,32)
print(sum(t)) # 81

