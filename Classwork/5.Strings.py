# 5. Strings.py

s='pravallika'
print(s)  # pravallika
print(s+'a')
print(s)  # pravallikaa
print(s=s+'a')
'''Traceback (most recent call last):
  File "D:/Users/laxma/Desktop/Python-course-work/Bitwise operator.py", line 11, in <module>
    print(s=s+'a')
TypeError: 's' is an invalid keyword argument for print()'''
l=[1,2,3]
print(l.append(4))
print(l)  #[1, 2, 3, 4]
print(l.remove(1))   #[2, 3, 4]
s='tarit'
s="tarit"
s='''tarit'''
s=' '
print(s)  #' '
fname='tarit'
lname='singh'
print(fname+lname)  # 'taritsingh'
print(fname*10)  # 'tarittarittarittarittarittarittarittarittarittarit'
print(fname)  # 'tarit'
s='Python Programming'
print(s[5])  # 'n'
print(s[1])  # 'y'
print(s[-3])  # 'i'
print(s[-1])# 'g'
print(s[5])  # 'n'
print(s[-2])  # 'n'
names='HarshithSowmyaKiranVarunMani'
print(names)  # 'HarshithSowmyaKiranVarunMani'

#[start:end+1:step]
print(names[0:8])  # 'Harshith'
print(names[8:14]) # 'Sowmya'
print(names[14:19])  # 'Kiran'
print(names[19:24]) # 'Varun'
print(names[24:28]) # 'Mani'
print(names[0:8:2])  # 'Hrht'
print(names[0:28:1])  # 'HarshithSowmyaKiranVarunMani'
print(names[0:28:2])  # 'HrhtSwyKrnauMn'
print(names[1:28:2])  # 'asihomaiaVrnai'
print(names[-5:-1])  # 'nMan'
print(names[-4:])  # 'Mani'
print(names[-9:-4]) # 'Varun'
print(names[-14:-9])  #'Kiran'
print(names[-22-14])
'''Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    names[-22-14]
IndexError: string index out of range'''
print(names[-20:-14])  # 'Sowmya'
print(names[-27:-20])  # 'arshith'
print(names[:-20])  # 'Harshith'
print(names[::-1]) # 'inaMnuraVnariKaymwoShtihsraH'
print(names)  # 'HarshithSowmyaKiranVarunMani'
print(names[-1:-4:-1])  # 'ina'
print(names[-1:-5:-1])  # 'inaM'
print(names[-5:-10:-1])  #'nuraV'
print(names[-10:-15:-1])  # 'nariK'
print(names) # 'HarshithSowmyaKiranVarunMani'
print('Kiran' in names) # True
print('Adithya' in names) # False
print('Hema' not in names) # True
print('mounika' not in names) # True
print(names) # 'HarshithSowmyaKiranVarunMani'
print(len(names))  # 28
print(max(names)) # 'y'
print(min(names)) # 'H'
print(sorted(names))  # ['H', 'K', 'M', 'S', 'V', 'a', 'a', 'a', 'a', 'a', 'h', 'h', 'i', 'i', 'i', 'm', 'n', 'n', 'n', 'o', 'r', 'r', 'r', 's', 't', 'u', 'w', 'y']
print(ord('H')) # 72
print(ord('K')) # 75
print(ord('S')) # 83
print(ord('a'))  # 97
print(chr(97)) # 'a'
print(chr(1)) # '\x01'
print(chr(30)) # '\x1e'
print(chr(101)) # 'e'
print(chr(120))  # 'x'
print(chr(130))  # '\x82'
print(ord('1')) # 49
print(ord('9'))  # 57
print(ord('@')) # 64
print(names)  # 'HarshithSowmyaKiranVarunMani'
print(names.upper())  # 'HARSHITHSOWMYAKIRANVARUNMANI'
print(names.lower())   # 'harshithsowmyakiranvarunmani'
print(names.capitalize()) # 'Harshithsowmyakiranvarunmani'

d='python programming lang'
print(d.title())  # 'Python Programming Lang'
print(d)  # 'python programming lang'
print(d.captilize())
'''Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    d.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?'''

print(d.capitalize())  # 'Python programming lang'
print(d)  # 'python programming lang'
print(d)  # 'python programming lang'
print(names)  # 'HarshithSowmyaKiranVarunMani'
print(names.swapcase())  # 'hARSHITHsOWMYAkIRANvARUNmANI'

k='नमते你好'
print(k.casefold())  # 'नमते你好'
k="🙂"
print(k)  # '🙂'
print("ß".casefold())  # 'ss'
print("ß".lower())  # 'ß'
print(d) # 'python programming lang'
print(d.center(50,'-'))  # '-------------python programming lang--------------'
print(d.center(50,'*'))  # '*************python programming lang**************'
print(d.center(50,' '))  # '             python programming lang              '
print(d.ljust(50,'_'))  # 'python programming lang___________________________'
print(d.rjust(50,'_'))  # '___________________________python programming lang'
print("name".ljust(10,' '))  # 'name      '
print('age'.ljust(10,' '))  # 'age       '
print('dob'.ljust(10,' '))  # 'dob       '
print('Address'.ljust(10,' '))  # 'Address   '
print("name".ljust(10,' ')+'sdfgyui')  # 'name      sdfgyui'
print('42'.zfill(5))  # '00042'
print('301'.zfill(2))  # '301'
print('301'.zfill(5))  # '00301'
print('4321'.zfill(5))  # '04321'
print(names)  # 'HarshithSowmyaKiranVarunMani'
print(names.find("kiran"))  # -1
print(names.find("Kiran"))  # 14
print(names.find(names[:8]))  # 0
print(names.find(names[14:19])) # 14
print(names.find('z'))  # -1
print(names.find('H'))  # 0
print(names.find('S'))  # 8
print(names.find('a'))  # 1
print(names.rfind('a'))  # 25
print(names.index('S'))  # 8
print(names.index('z'))
'''Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    names.index('z')
ValueError: substring not found'''
names
'HarshithSowmyaKiranVarunMani'
print(names.count('a'))  # 5
print(names.count('i'))  # 3
print(names.count('r'))  # 3



# String Testing methods

print(32>>1)
16
print(16>>1)
8
print(8>>1)
4
print(32/2)
16.0

a=2
a=a<<2
print(a)  # 8
print(a<<1)  # 16

print('абвгдежзийкл'.casefold())  # 'абвгдежзийкл'
10
10
100
100
1000
1000
10000
10000
100000
100000
print(8>>1)  # 4
print(8>>3)  # 1

'''
DS-15
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
DS-15  # NameError: name 'DS' is not defined
DA-14
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>

DA-14  # NameError: name 'DA' is not defined
PFS-15
 # Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>

PFS-15  # NameError: name 'PFS' is not defined
'PFS15'.startwith('DS')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    'PFS15'.startwith('DS')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
print('PFS15'.startswith('DS'))  # False
print('JFS15'.startswith('DS'))  # False

print('DA15'.startswith('DS'))  # False
print('DS15'.startswith('DS'))  # True

'''

l=['PFS14','DS-11','DA-14','PFS-15','JS-12','DS-15','DS-14']
for i in l:
    if i.startswith('DS'):
        print(i)

        
'''DS-11
DS-15
DS-14'''

l=['hello.py','demo.png','resume.pdf','oper.py','python.py']
for i in l:
    if i.endswith('.py'):
        print(i)

'''hello.py
oper.py
python.py'''

s='sowmya'
print(s.isalpha())  # True
s='varun123'
print(s.isalpha())  # False
print(s.isalnum())  # True
print(s.islower())  # True
print(s.isupper())  # False
print(s.isspace())  # False
print(' '.isspace())  # True
print('     '.isspace())  # True
s='python prgrm'
print(s.istitle())  # False
s=s.title()
print(s)  # 'Python Prgrm'
print(s.istitle())  # True
print('@myvae'.isidentifier())  # False
print('my_var'.isidentifier())  # True

print('١٢٣'.isdigit())  # True
print('123'.isdigit())  #True
print('⓫'.isdigit())   # False
print('۵'.isdigit())  # True
print('五'.isnumeric())  # True
s='Tatik'
print(s.replace('i','ee'))  # 'Tateek'
s='python pgrm lang'
print(s.replace(' ',''))  # 'pythonpgrmlang'
print(s)  # 'python pgrm lang'
pwd='harshith@123'

'''
print(pwd.translate(str.maketrans("a13h", "@o#8")))  # '8@rs8it8@o2#'
print(pwd.translate(str.maketrans("@o#8", "a13h")))  # 'harshitha123'
print(maketrans("a13h", "@o#8"))
 Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
print(maketrans("a13h", "@o#8"))  # NameError: name 'maketrans' is not defined
print("harshit".maketrans("a13h", "@o#8"))  # {97: 64, 49: 111, 51: 35, 104: 56}
print(pwd.maketrans("a13h", "@o#8"))  # {97: 64, 49: 111, 51: 35, 104: 56}

'''
  
s='My name is Tarit'
print(s.split())  # ['My', 'name', 'is', 'Tarit']
print(s.split('a'))  # ['My n', 'me is T', 'rit']
i='Varun,Harshith,Hemanth'
print(i.split(','))  # ['Varun', 'Harshith', 'Hemanth']
print(s)  # 'My name is Tarit'
print(s.split())  # ['My', 'name', 'is', 'Tarit']
print(s.rsplit(' ',2))  # ['My name', 'is', 'Tarit']

file='''Hello
world
python
program
'''
print(file)  #  'Hello\nworld\npython\nprogram\n'
print(file.splitlines())  # ['Hello', 'world', 'python', 'program']
file=['Hello', 'world', 'python', 'program']
print(''.join(file))  # 'Helloworldpythonprogram'
print(' '.join(file))  # 'Hello world python program'
print('@'.join(file))  # 'Hello@world@python@program'
print(','.join(file))  # 'Hello,world,python,program'
print('pythonprgm.py'.partition('.'))  # ('pythonprgm', '.', 'py')
print('pythonprgm.file.py'.rpartition('.'))  # ('pythonprgm.file', '.', 'py')
print('1.pythonprgm.py'.rpartition('.'))  # ('1.pythonprgm', '.', 'py')
print(file)  # ['Hello', 'world', 'python', 'program']
file='''Hello
world
python
program
'''
print(file.split('\n'))  # ['Hello', 'world', 'python', 'program', '']
s='           python          '
print(s.strip())  # 'python'
print(s.lstrip())  # 'python          '
print(s.rstrip())  # '           python'
print(s)  # '           python          '

print(s.encode())  # b'           python          '

text = "Hello 🙂"
print(text.encode())  # b'Hello \xf0\x9f\x99\x82'
print(b'Hello \xf0\x9f\x99\x82'.decode())  # 'Hello 🙂'
text="नमते你好"
print(text.encode())  # b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd'
print(b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd'.decode())  # 'नमते你好'

print('banana'.count('na'))  # 2
print('abcbcbc'.count('cbc'))  # 1

print('tarit'.maketrans('a','@'))  # {97: 64}
  # print('tarit'.translate())
'''Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>'''

  # print('tarit'.translate())  # TypeError: str.translate() takes exactly one argument (0 given)
print('tarit'.translate('tarit'.maketrans('a','@')))  # 't@rit'
print('tarit'.translate(str.maketrans('a','@')))  # 't@rit'
