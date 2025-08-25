'''

Regular Expressions: 

whenever we look for the patterns,search functionality we use reg exprsns

when ever we deal with reg exp we need to use

import re

'''
import re
res = re.match('Hello','Hello World') # ----- i want to check whether the partten is starting with Hello or not
print(res.group() if res else "No Pattrn" )

import re
res = re.match('re','Hello World') # ----- i want to check whether the partten is starting with 're' or not
print(res.group() if res else "No Pattrn" )

import re
res = re.match('re','Hello World') # ----- i want to check whether the pattern is starting with 're' or not
print(res.group() if res else "No Pattrn" )

import re
res = re.match(r'\d','Hello World') # ----- i want to check whether the partten is starting with 'number' or not
print(res.group() if res else "No Pattrn" )

import re
res = re.match(r'\d','22Hello World') # ----- i want to check whether the partten is starting with 'number' or not
print(res.group() if res else "No Pattrn" )

import re
res = re.match(r'\d{2}','Hello World') # ----- i want to check whether the partten is starting with 'number' or not and {2} gives me the staring 2 digits
print(res.group() if res else "No Pattrn" )

import re
res = re.match(r'\d{2}','2347Hello World') # ----- i want to check whether the partten is starting with 'number' or not
print(res.group() if res else "No Pattrn" )

import re
res = re.match(r'\d[a-z]','Hello World') # ----- i want to check whether the partten is starting with 'number' or not
print(res.group() if res else "No Pattrn" )

import re
res = re.search(r'[a-z]','hello World') # ----- i want to check whether the partten is starting with 'number' or not
print(res.group() if res else "No Pattrn" )

'''
'r' - we use infront of the string if we are dealing with digits/expressions
we no need to use 
match - is going to check whether the pattern is strating with the req word in the string
search - is going to search the pattern the entire string/element and gives the 1st occurance
findall - gives me all the search things/patterns that we are looking for. and give me list as output
{2} - is the length
[]- if i'm giving the pattern it checks whether it is present or not 
finditer - is going to give the index/the position when exactly it's staring of the pattern 
group - gives the position 
fullmatch - what patterns we have give the string need to match with my entire pattern 
* - its option if have /do not have pattern
+ - atleast i want my pattern in side once 
split - when i want to split the string we can use the patterns/characters (ex: , ; :) and split
sub - if i want to replace the string using patterns we use sub.
^ - staring with
$ - end with
( )- to check whether i have atleast one thing 
'''

import re
res = re.search(r'[0-9] {2}','ds-da-14-15') # ----- i want to check whether the partten is starting with 'number' or not
print(res.group() if res else "No Pattrn" )

import re
res = re.findall(r'[0-9] {2}','PES-10 & PFS-31 ds-da-14-15') 
# print(res.group() if res else "No Pattern" )
print(res)

import re
res = re.finditer(r'[0-9] {2,}','PES-10 & PFS-31 ds-da-14-15') 
# print(res.group() if res else "No Pattern" )
# print(res)
for i in res:
    print(i.group(),i.start())


import re
res = re.fullmatch(r'(aeiou)','aeiou')
print(res.group() if res else "No Pattern")

# validating Phone number: 
import re
res = re.fullmatch(r'\d{10}','6216573912')
print(res.group() if res else "No Pattern")

import re
res = re.fullmatch(r'\d{10}','62165739123')
print(res.group() if res else "No Pattern")

import re
res = re.fullmatch(r'^[6-9]\d{9}','92165739123')
print(res.group() if res else "No Pattern")

import re
res = re.fullmatch(r'DA-..','DA-15') # the two .. gives me the elements after the pattern
print(res.group() if res else "No Pattern")

import re
res = re.findall(r'P..h.n','Python python pythonx psthon psxhin') # shows me all kinds of patterns when we search 
print(res)

# I want all the words/characters in my sentencs - give \w
# \W - is for spaces
# all the spaces - \s
# \S is for words

import re
res = re.findall(r'\w','Python python pythonx psthon psxhin') 
print(res)

import re
res = re.findall(r'\w+','Python python pythonx psthon psxhin') 
print(res)


import re
res = re.findall(r'\W','Python python pythonx psthon psxhin') 
print(res)

import re
res = re.findall(r'\s','Python python pythonx psthon psxhin') 
print(res)

import re
res = re.findall(r'\S','Python python pythonx psthon psxhin') 
print(res)

import re
res = re.split(r'[, ; "-]','Python,python;pythonx"psthon-psxhin pthon') 
print(res)

import re
res = re.sub(r'[aeiouAEIOU]','*0*','Python Programming Language') 
print(res)

import re
res = re.sub(r'[A-Z]','_','Python Programming Language')  # if we find capital letters from A-Z replace it with '_'(pattern)
print(res)

import re
res = re.search(r'[a-z]*[0-9]$','Python Programming Language') # $ chech if the pattern is ending with no' or not
print(res)

import re
res = re.search(r'h?i','hii') # ? - is for optional data( it accepts even it ocuurs / doesn't occurs)
print(res.group() if res else "No Pattern" )

import re
res = re.search(r'h.i','hii')
print(res.group() if res else "No Pattern" )

import re
res = re.findall(r'\b\d{2}\b','32 45 47 37 23 37 43 43333 7832 483 342') # \b - setting the boundaries
print(res)

import re
res = re.findall(r'\b\d{4}\b','32 45 47 37 23 37 43 43333 7832 483 342')
print(res)

# validating Full Name:

pattern = r'^[A-Za-z]{2,25} ( [A-Za-z]{2,25})+$'

# validating Email:

pattern = r'[a-z-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$' # after @ it alows even if we have capital letters, i.e it stores the capital letters as small letters

# validating Phone Number: 

phone_no = r'(?:\+91\0)?[6-9]\d{9}$'

# validating Password :

pwd = r''