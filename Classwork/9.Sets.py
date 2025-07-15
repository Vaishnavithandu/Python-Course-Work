# set
s={1,1,1,1,1,2,2,3} # (sets are mutable)
print(s)  # {1, 2, 3}  (doesn't allow duplicates)
s={100,20,2,3,1,6,1,7,3,2,1786} 
print(s)  # {1, 2, 3, 100, 6, 7, 20, 1786} ( unordered collection of elements and it's mutable)

'''

# frozenset
s=frozenset({1,2,3,4})
print(type(s))  # <class 'frozenset'>
s.add(12) # immutable
   Traceback (most recent call last):
  File "D:/Users/laxma/Desktop/Python-course-work/3. Python Data Types.py", line 53, in <module>
    s.add(12)
AttributeError: 'frozenset' object has no attribute 'add'

'''


s=set()
print(s)  # set()
s=[1,2,3,4,5,7]
print(s)  # [1, 2, 3, 4, 5, 7]
s=[1,2.3]
print(s)  # [1, 2.3]
print(s.add(2+3j))
print(s)
'''Traceback (most recent call last):
  File "d:/Users/laxma/Desktop/Python-course-work/Python-Course-Work/Classwork/9.Sets.py", line 27, in <module>
    print(s.add(2+3j))
AttributeError: 'list' object has no attribute 'add'  '''

print(s.add("String"))
print(s) 
print(s.add([1,2,3]))
print(s)
print(s.add((1,2,3,4)))
print(s)
print(s.add({"key":"value"}))
print(s)
print(s.add(False))
print(s)
