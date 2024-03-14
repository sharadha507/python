import array
a=array.array('i',[1,2,3,4,5,6])
a
array('i', [1, 2, 3, 4, 5, 6])
import array as arr
a=arr.array('i',[1,2,3,4,5,6])
a
array('i', [1, 2, 3, 4, 5, 6])
from array import *
a=array('i',[1,2,3,4,5,6])
a
array('i', [1, 2, 3, 4, 5, 6])
#Accessing Elements
a[2]
3
#Finding Length of an Array
len(a)
6
#Adding Elements
a
array('i', [1, 2, 3, 4, 5, 6])
a.append(8)
a
array('i', [1, 2, 3, 4, 5, 6, 8])
a.append(2.4)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.append(2.4)
TypeError: 'float' object cannot be interpreted as an integer
a.extend([9,3,5,6])
a
array('i', [1, 2, 3, 4, 5, 6, 8, 9, 3, 5, 6])
a.insert(2,6)
a
array('i', [1, 2, 6, 3, 4, 5, 6, 8, 9, 3, 5, 6])
#Removing Elements
a
array('i', [1, 2, 6, 3, 4, 5, 6, 8, 9, 3, 5, 6])
a.pop()
6
a.pop(-2)
3
a
array('i', [1, 2, 6, 3, 4, 5, 6, 8, 9, 5])
a.pop(2)
6
a.pop(-1)
5
a
array('i', [1, 2, 3, 4, 5, 6, 8, 9])
a.remove(8)
a
array('i', [1, 2, 3, 4, 5, 6, 9])
#Array Concantenation
b=arr.array('i',[1,2,3,4,5,6])
c=arr.array('i',[3,4,5,7,9])
d=arr.array('i')
d=b+c
d
array('i', [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 9])
#Slicing an Array
d
array('i', [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 9])
d[0:5]
array('i', [1, 2, 3, 4, 5])
d[0:-2]
array('i', [1, 2, 3, 4, 5, 6, 3, 4, 5])
d[::-1]
array('i', [9, 7, 5, 4, 3, 6, 5, 4, 3, 2, 1])
d
array('i', [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 9])
#
#Looping in Array
d
array('i', [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 9])
temp=0
while temp<d[2]:
    print(d[temp])
    temp=temp+1
    print(temp)

    
1
1
2
2
3
3


a
array('i', [1, 2, 3, 4, 5, 6, 9])
temp=0
while temp<len(a):
    print(a[temp])
    temp+=1

    
1
2
3
4
5
6
9
