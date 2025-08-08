#--- Builtin modules ---#
import sys
print(sys.argv)   # store the arguments
print(sys.path)  # the path where the python files are stored
print(sys.version) 
print(sys.exit) # exit from the prgm or to terminate from the prgn we use this
print(sys.exit(0)) # terminating the prgm ubnormally
print(sys.exit(1)) # terminating the prngm normally

import platform            # to know the system details we use this
print(platform.system())
print(platform.release())  # os release version
print(platform.processor()) #  

import math
print(math.sqrt(25))  # to check the sqrt root # O/P -5.0

import math  # it give the next no' or the upper value when we use ceil
print(math.ceil(12.3))  # 13
print(math.ceil(12.8))  # 13
print(math.ceil(12.1))  # 13

# math(floor) - # it give the previous no' or the lower value when we use floor
print(math.floor(12.3)) # 12
print(math.floor(12.8)) # 12
print(math.floor(12.1)) # 12
      
# math.gcd(x,y) -- gives the highest factor in both

print(math.gcd(8,24)) # 8
print(math.log(2))
print(math.sin(45))
print(math.cos(0))
print(math.tan(45))
print(math.degrees(45))
print(math.radians(30))

import random
print(random.random())  # gives any value b/w 0 to 1
print(random.randint(1,6))
print(random.uniform(1,6))

names = ['Vaishnavi', 'Lakshmi', 'Kalyani', 'Janani'] 
print(choice(names))
print(random.chocies(names,k=3))  # to generate more than 1 values ex: upto 3 values

random.shuffle(names)
print(names)

print(random.seed) # without seed we get different outputs of random no's so to avoid that we use random.seed(n)




# Collections

  # counter - counts the frequency of each and every letter(how many times it is repeating)
import collections
w='Hello world Program'.split()
d= collection.counter(w)
print(d)

import collections
w='Hello world Program'
d= collection.counter(w)
print(d)

import collections
w=(1,2,3,4,6,5,3,4,5,2,4,5,6) # for tuple
d= collection.counter(w)
print(d)

# Default Dictionary

import collections
s='abcdef'
d= collection.defaultdict(str) # it initializes all the key values the default value i.e initialised with 0
for i in range(1,7)
    d[i]+=s[i-1]
print(d)

# Deque - we use this whenever we need to deal with queue and stack

# Stack - have append and pop from only one direction
# Queue - append and remove in two diff directions 

from collections import deque
l=deque()
l.append(12)
l.append(1)
l.pop()
l.append(12)
l.pop()
l.pop()

from collections import deque
l=deque()
l.appendleft(12)
l.appendleft(1)
l.popleft()
l.appendleft(12)
l.popleft()
l.popleft() # appendleft and pop left /appendright or popright is used for the direction from where to append and pop

# iterals #

