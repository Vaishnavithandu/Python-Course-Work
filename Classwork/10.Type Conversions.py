# 10.Type Conversions

 # coverting int to other data types

a=2
print(type(a)) # <class 'int'>
print(float(a)) # 2.0
print(complex(a)) # (2+0j)
print(str(a)) # '2'
print(bool(a)) # True
# print(list(a)) # 'int' object is not iterable
# print(set(a)) # 'int' object is not iterable
# print(tuple(a)) # 'int' object is not iterable
# print(dict(a)) # 'int' object is not iterable

# coverting float to other data types

b=1.3
print(type(b)) # <class 'float'>
print(int(b)) # 1
print(complex(b)) # (1.3+0j)
print(str(b)) # '3.1'
print(bool(b)) # True
# print(list(b)) # 'float' object is not iterable
# print(set(b)) # 'float' object is not iterable
# print(tuple(b)) # 'float' object is not iterable
# print(dict(b)) # 'float' object is not iterable


# Converting str to other data types

s='Power'
print(type(s)) # <class 'str'>
# print(int(s)) # invalid literal for int() with base 10: 'Power'
# print(float(s)) # Error
print(bool(s)) # True
print(list(s)) # ['P', 'o', 'w', 'e', 'r']
print(tuple(s)) # ('P', 'o', 'w', 'e', 'r')
print(set(s)) # {'e', 'o', 'w', 'P', 'r'}
# print(dict(s)) # Error - needs key-value pair structure
# s='10.9'
# print(int(s)) # ValueError:invalid literal for int() with base 10: '10.9'

s='10'
print(type(s)) # <class 'str'> (only numeric strings can be converted)
print(int(s)) #  10
print(float(s)) # 10.0
print(complex(s)) # (10+0j)
print(bool(s)) # True
print(list(s)) # ['1', '0']
print(tuple(s)) # ('1', '0')
print(set(s)) # {'0', '1'}
# print(dict(s)) # valueError : needs key-value pair structure


# Converting List to other data types

l=[1,2,3,4,5] 
# print(int(l)) # Error
# print(float(l)) # Error
# print(complex(l)) # Error
print(str(l)) # '[1, 2, 3, 4, 5]' 
    # we cann't convert list into string directly using str(l)
l1= ['xyz','abc','pqr']
print(''.join(l1)) # 'xyzabcpqr'
   # we can convert list into string by using .join(l)
   # .join() only works when we have string in list
l2=[1,2,3]
# print(''.join(l2)) # TypeError: sequence item 0: expected str instance, int found

print(bool(l)) # True
print(tuple(l)) # (1, 2, 3, 4, 5)
print(set(l)) # {1, 2, 3, 4, 5} (removes duplicates if any)
# print(dict(l)) # Error - needs list of key-value pairs 


# Converting Tuple to other data types

t=[1,2,3,4]
# print(int(t)) # Error
# print(float(t)) # Error
# print(complex(t))
print(str(t)) # '[1, 2, 3, 4]'
print(bool(t)) # True
print(list(t)) # [1, 2, 3, 4]
print(set(t)) # {1, 2, 3, 4}
# print(dict(t)) # Error - Must be tuple of key-value pairs
t=[(1,2),(3,4),(5,6)] # in this case we can convert tuple into dict
print(dict(t))  # {'a': '1', 'b': '2', 'c': '3'}


# Converting Set to other data types

c={2,3,4,4,5,6}
# print(int(set)) # Error
# print(float(set)) # Error
# print(complex(set)) # Error
print(str(c)) # '{2, 3, 4, 5, 6}'
print(bool(c)) # True
print(list(c)) # [2, 3, 4, 5, 6] (Order may vary)
print(tuple(c)) # (2, 3, 4, 5, 6) (Order may vary)
# print(dict(set)) # Error - Must be iterable of key-value pairs


# Converting dict to other datda types

dict={"a":"1","b":"2","c":"3"}
print(type(dict)) # <class 'dict'>
# print(int(dict)) # Error
# print(float(dict)) # Error
# print(complex(dict)) # Error
print(str(dict)) # {'a': '1', 'b': '2', 'c': '3'}
print(list(dict)) # ['a', 'b', 'c'] - we get list of keys
print(tuple(dict)) # ('a', 'b', 'c') - we get list of keys
print(set(dict)) # {'b', 'a', 'c'}


# Converting Bool to other data types




