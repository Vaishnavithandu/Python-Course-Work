# 6.Lists.py

l=[1,2,3,4,5,6,7]
print(l)  # [1, 2, 3, 4, 5, 6, 7]
print(l.append(8))
print(l)  # [1, 2, 3, 4, 5, 6, 7, 8]
print(l.remove(1))
print(l)  # [2, 3, 4, 5, 6, 7, 8]
print(l[2])  # 4
print(l[5])  # 7
print(l)  # [2, 3, 4, 5, 6, 7, 8]
print(l.append(2))
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2]
print(l.append(2.3))
print(l.append("string"))
print(l.append(True))
print(l.append((1,2,3)))
print(l.append({1,2,3}))
print(l.append({"course":"py"}))
print(l.append(2+5j))
print(l.append([1,2,3]))
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]
l=[]
l=list()
# [2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]
# [2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]

l=[2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]
print(l[-3:])  # [{'course': 'py'}, (2+5j), [1, 2, 3]]
print(l[:7])  # [2, 3, 4, 5, 6, 7, 8]
print(l[8:10])  # [2.3, 'string']
print(l[9:11])  # ['string', True]
print(len(l))  # 16
print(l[-7:-11])  # []
print(l[-7:-11:-1])  # ['string', 2.3, 2, 8]
print(l[-6:-10:-1])  # [True, 'string', 2.3, 2]
print(l[::-1])  #[[1, 2, 3], (2+5j), {'course': 'py'}, {1, 2, 3}, (1, 2, 3), True, 'string', 2.3, 2, 8, 7, 6, 5, 4, 3, 2]
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]
print(l[0])  # 2
print(l[0]=1)
print(l)  # [1, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]
print(l.append("append function"))
print(l)  # [1, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3], 'append function']
print(l.extend(["extend start",1,2,3,'extend end']))
print(l) # [1, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(l.insert(1,2))
print(l)  # [1, 2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(l.remove('string'))
print(l)  # [1, 2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(l.remove(True))
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(l.remove('True'))
'''Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>'''
print(l.remove('True'))  # ValueError: list.remove(x): x not in list
print(l.value({'course': 'py'}))
'''Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>'''
print(l.value({'course': 'py'}))  # AttributeError: 'list' object has no attribute 'value'
print(l.remove({'course': 'py'}))
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, (2+5j), [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(l.remove((2+5j)))
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(l.pop())  # 'extend end'
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3]
print(l.pop())  # 3
print(l.pop())  # 2
print(l.pop())
print(1)
l.pop()  # 'extend start'
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function']
print(l.pop(8))  # 2.3
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function']
print(l.pop(8))  # True
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function']
print(del l[-1])
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, (1, 2, 3), {1, 2, 3}, [1, 2, 3]]
print(del[-2])  # SyntaxError: incomplete input
print(del l[-2])
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, (1, 2, 3), [1, 2, 3]]
print(l.remove(2))
print(l)  # [3, 4, 5, 6, 7, 8, 2, (1, 2, 3), [1, 2, 3]]
print(pop(0))
'''Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>'''
print(pop(0)))  # NameError: name 'pop' is not defined. Did you mean: 'pow'?
print(l.pop(0))  # 3
print(l.pop(0))  # 4
print(l)  # [5, 6, 7, 8, 2, (1, 2, 3), [1, 2, 3]]
print(l.pop())  # [1, 2, 3]
print(l.pop())   # (1, 2, 3)
print(l.pop())  # 2
print(l.pop(0))  # 5
print(del l[0])  # l=[1,2,3]
print(l.clear())
print(l)  # []
l=[1,2,3]
print(del l)
print(l)
'''Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>'''
print(l)  # NameError: name 'l' is not defined
l=[1,2,3,5]
print(l.index(5)))  # 3
l=[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(l.index('append function'))  # 13
print(l.count(2))  # 3
l=[4,2,3,5,6,1,2,3,7,4,9,8,7,6,4,2]
print(sorted(l))  # [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 8, 9]
print(l)  # [4, 2, 3, 5, 6, 1, 2, 3, 7, 4, 9, 8, 7, 6, 4, 2]
print(l.sort())
print(l)  # [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 8, 9]
print(l.sort(reverse=True))
print(l)  # [9, 8, 7, 7, 6, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1]
l=[4,2,3,5,6,1,2,3,7,4,9,8,7,6,4,2]
print(l.reverse())
print(l)  # [2, 4, 6, 7, 8, 9, 4, 7, 3, 2, 1, 6, 5, 3, 2, 4]
print(l[::-1])  # [4, 2, 3, 5, 6, 1, 2, 3, 7, 4, 9, 8, 7, 6, 4, 2]
print(l)  # [2, 4, 6, 7, 8, 9, 4, 7, 3, 2, 1, 6, 5, 3, 2, 4]
print(l.reverse())
l=[1,2,3,4]
k=l.copy()
print(k.append(5))
print(l)  # [1, 2, 3, 4]
print(k)  #[1, 2, 3, 4, 5]
m=l
print(m.append(6))
print(m)  # [1, 2, 3, 4, 6]
print(l)  # [1, 2, 3, 4, 6]
print(l)  # [1, 2, 3, 4, 6]

'''

l.index(2,[0:3])
SyntaxError: invalid syntax
l.index(2,(0,3))
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    l.index(2,(0,3))
TypeError: slice indices must be integers or have an __index__ method
l.index(2,[1,3])
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    l.index(2,[1,3])
TypeError: slice indices must be integers or have an __index__ method

'''

print(l.index(2))
print(l)  # [1, 2, 3, 4, 6]
print(l)  # [1, 2, 3, 4, 6]
print(max(l))  # 6
print(min(l))  # 1
print(sum(l)  # 16
print(l=['name','age']))
print(sum(l))
'''Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>'''
print(sum(l))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'



l=[23.2,23.4]
print(l)  # [23.2, 23.4]
print(sum(l))  # 46.599999999999994
print(floor(46.599999999999994))
'''Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    floor(46.599999999999994
NameError: name 'floor' is not defined. Did you mean: 'float'?'''
print(len(l))  # 2
print(any(l))  # True
print(all(l))  # True
l=[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(l.index('append function'))  # SyntaxError: multiple statements found while compiling a single statement
l=[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(l)   # [2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(all))  # True
           
'False 0  [] () {} set() - It gives False'
print(l.append(0))
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end', 0]
print(all))  # False
print(l=[False,'',0,'username'])
print(all(l))  # False
print(any(l))  # True
print(l.pop())  # 'username'
print(l)  # [False, '', 0]
print(any(l))  # False
print(l)  # [False, '', 0]

l=[False,'',0,'username']
print(any(l))  # True
print(l.pop())  # 'username'
print(l)  # [False, '', 0]
print(any(l))  # False

l=[False,'',0,'username']
print(all(l))  # False

a=['uesrname','mobile','add','']
print(all(a))  # False
print(any(a))  # True
print(a.pop())  # ''
print(a)  # ['uesrname', 'mobile', 'add']
print(all(a))  # True

l=[1,2,3,4,5,6,7]
print(l)  # [1, 2, 3, 4, 5, 6, 7]
print(l.append(8))
print(l)   # [1, 2, 3, 4, 5, 6, 7, 8]
print(l.remove(1))
print(l)  # [2, 3, 4, 5, 6, 7, 8]
print(l[2])  # 4
print(l[5])  # 7
print(l)  # [2, 3, 4, 5, 6, 7, 8]
print(l.append(2))
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2]
print(l.append(2.3))
print(l.append("string"))
print(l.append(True))
print(l.append((1,2,3)))
print(l.append({1,2,3}))
print(l.append({"course":"py"}))
print(l.append(2+5j))
print(l.append([1,2,3]))
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]

l=[]
l=list()
[2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]
[2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]

l=[2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]
print(l[-3:])  # [{'course': 'py'}, (2+5j), [1, 2, 3]]
print(l[:7])  # [2, 3, 4, 5, 6, 7, 8]
print(l[8:10])  # [2.3, 'string']
print(l[9:11])  # ['string', True]
print(len(l))  # 16
print(l[-7:-11])  # []
print(l[-7:-11:-1])  # ['string', 2.3, 2, 8]
print(l[-6:-10:-1])  # [True, 'string', 2.3, 2]
print(l[::-1])  # [[1, 2, 3], (2+5j), {'course': 'py'}, {1, 2, 3}, (1, 2, 3), True, 'string', 2.3, 2, 8, 7, 6, 5, 4, 3, 2]
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]
print(l[0])  # 2
print(l[0]=1)
print(l)  # [1, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3]]

print(l.append("append function"))
print(l)  # [1, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3], 'append function']
print(l.extend(["extend start",1,2,3,'extend end']))
print(l)  # [1, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(l.insert(1,2))
print(l)  # [1, 2, 3, 4, 5, 6, 7, 8, 2, 2.3, 'string', True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(l.remove('string'))
print(l)  # [1, 2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(l.remove(True))
print(l)  # [2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, {'course': 'py'}, (2+5j), [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
print(l.remove('True'))
'''Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>'''
print(l.remove('True'))  # ValueError: list.remove(x): x not in list
print(l.value({'course': 'py'}))
'''Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>'''
    l.value({'course': 'py'})
AttributeError: 'list' object has no attribute 'value'
l.remove({'course': 'py'})
l
[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, (2+5j), [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
l.remove((2+5j))
l
[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
l.pop()
'extend end'
l
[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3]
l.pop()
3
l.pop()
2
l.pop()
1
l.pop()
'extend start'
l
[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function']
l.pop(8)
2.3
l
[2, 3, 4, 5, 6, 7, 8, 2, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function']
l.pop(8)
True
l
[2, 3, 4, 5, 6, 7, 8, 2, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function']
del l[-1]
l
[2, 3, 4, 5, 6, 7, 8, 2, (1, 2, 3), {1, 2, 3}, [1, 2, 3]]
del[-2]
SyntaxError: incomplete input
del l[-2]
l
[2, 3, 4, 5, 6, 7, 8, 2, (1, 2, 3), [1, 2, 3]]
l.remove(2)
l
[3, 4, 5, 6, 7, 8, 2, (1, 2, 3), [1, 2, 3]]
pop(0)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    pop(0)
NameError: name 'pop' is not defined. Did you mean: 'pow'?
l.pop(0)
3
l.pop(0)
4
l
[5, 6, 7, 8, 2, (1, 2, 3), [1, 2, 3]]
l.pop()
[1, 2, 3]
l.pop()
(1, 2, 3)
l.pop()
2
l.pop(0)
5
del l[0]
l=[1,2,3]
l.clear()
l
[]
l=[1,2,3]
del l
l
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    l
NameError: name 'l' is not defined
l=[1,2,3,5]
l.index(5)
3
l=[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
l.index('append function')
13
l.count(2)
3
l=[4,2,3,5,6,1,2,3,7,4,9,8,7,6,4,2]
sorted(l)
[1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 8, 9]
l
[4, 2, 3, 5, 6, 1, 2, 3, 7, 4, 9, 8, 7, 6, 4, 2]
l.sort()
l
[1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 8, 9]
l.sort(reverse=True)
l
[9, 8, 7, 7, 6, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1]
l=[4,2,3,5,6,1,2,3,7,4,9,8,7,6,4,2]

l.reverse()
l
[2, 4, 6, 7, 8, 9, 4, 7, 3, 2, 1, 6, 5, 3, 2, 4]
l[::-1]
[4, 2, 3, 5, 6, 1, 2, 3, 7, 4, 9, 8, 7, 6, 4, 2]
l
[2, 4, 6, 7, 8, 9, 4, 7, 3, 2, 1, 6, 5, 3, 2, 4]
l.reverse()
l=[1,2,3,4]
k=l.copy()
k.append(5)
l
[1, 2, 3, 4]
k
[1, 2, 3, 4, 5]
m=l
m.append(6)
m
[1, 2, 3, 4, 6]
l
[1, 2, 3, 4, 6]
l
[1, 2, 3, 4, 6]
l.index(2,[0,3])
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    l.index(2,[0,3])
TypeError: slice indices must be integers or have an __index__ method
l.index(2,[0:3])
SyntaxError: invalid syntax
l.index(2,(0,3))
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    l.index(2,(0,3))
TypeError: slice indices must be integers or have an __index__ method
l.index(2,[1,3])
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    l.index(2,[1,3])
TypeError: slice indices must be integers or have an __index__ method


l.index(2)
1
l
[1, 2, 3, 4, 6]
l
[1, 2, 3, 4, 6]
max(l)
6
min(l)
1
sum(l)
16
l=['name','age']
sum(l)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    sum(l)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
l=[23.2,23.4]
l
[23.2, 23.4]
sum(l)
46.599999999999994
floor(46.599999999999994
)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    floor(46.599999999999994
NameError: name 'floor' is not defined. Did you mean: 'float'?
len(l)
          
2
any(l)
          
True
all(l)
          
True
l=[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
l.index('append function')
          
SyntaxError: multiple statements found while compiling a single statement
>>> l=[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
... 
>>> l
...           
[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end']
>>> all(l)
...           
True
>>> 'False 0 '' [] () {} set()'
...           
'False 0  [] () {} set()'
>>> l.append(0)
...           
>>> l
...           
[2, 3, 4, 5, 6, 7, 8, 2, 2.3, True, (1, 2, 3), {1, 2, 3}, [1, 2, 3], 'append function', 'extend start', 1, 2, 3, 'extend end', 0]
>>> all(l)
...           
False
>>> l=[False,'',0,'username']
          
all(l)
          
False
any(l)
          
True
l.pop()
          
'username'
l
          
[False, '', 0]
any(l)
          
False
l
          
[False, '', 0]
l=[False,'',0,'username']

any(l)
          
True
l.pop()
          
'username'
l
          
[False, '', 0]
any(l)
          
False
l=[False,'',0,'username']
all(l)
          
SyntaxError: multiple statements found while compiling a single statement
l=[False,'',0,'username']

all(l)

False
a=['uesrname','mobile','add','']
          
all(a)
          
False
any(a)
          
True
a.pop()
          
''
a
          
['uesrname', 'mobile', 'add']
all(a)
          
True
