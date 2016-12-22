import operator
from operator import itemgetter

list=[]

list.append([20,'Jaap'])
list.append([10,'Gabriel'])
list.append([30,'Barabrian'])

print sorted(list,reverse=True)
