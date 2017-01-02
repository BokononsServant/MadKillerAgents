import operator
from operator import itemgetter
import copy


list1=[[1,2],[3,4]]

for a in list1:
    for b in a:
        

list1[0].remove(2)

list1[0].remove(1)

print id(list1)
print id(list2)
print list1 
print list2