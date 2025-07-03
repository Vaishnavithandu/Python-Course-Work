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
