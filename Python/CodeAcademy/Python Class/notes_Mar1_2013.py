"""
CODE ACADEMY NOTES - MAR 1
"""

#string notes
str()
len()
string.upper()
string.lower()

---

#date and time
from datetime import datetime

#creates a datetime object
now = datetime.now()

#can use dot notaion to access data in the object easily
print "%d/%d/%d" % (now.month,now.day,now.year) \
    + " %d:%d:%d" % (now.hour,now.minute,now.second)

---

#for bools
1 = True
0 = False

#bool order of ops
not then and then or

---
import math
#for functions such as sqrt(), and all of math
#then
math.sqrt()


from math import sqrt
#instead, only import the sqrt() function
#then
sqrt()

from math import *
#import all functions from math with no need of math.func calling
#then
sqrt()
pi()
etc

import math
everything = dir(math)
print everything
#prints out a list of all functions in the module
---
