# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x=5
x
l=[1,2,"a"]
sum(l[0:2])
l[2].upper()
l
type(l)
t=(1,2,"a")
type(t)
d={"a":1,"b":2,"d":1}
f=frozenset({3,4,5})
type(f)
b="nice"
b
a='ls'
a
my_list=['my','list',a,b]
my_list
my_list2=[[4,5,6,7],[3,4,5,6]]

my_list[1:]

my_list2[1][0]
my_list2[1][0]>4
my_list.index(a)
my_list.sort()
my_list
10**10
2**3
a,b,c=10,20,30
print("sum=",(a+b)*10)
a+=b
print(a)
a=10,b=10
a
a,b=10,10
a
b
a,b
print(a&b)
b=20
a,b
a|b

l2=[1,2,3,'a',True]
l3=[i for i in range(5)]

for i in range(len(l2)):
    print(type(l2[i]),end='')
l1=[1,2,3,4,5]
l1
sum(l1)
l
l[len(l)-1].upper()
l4=[1,2,[l2]]
l4
l4[1]
l4=[1,2,l2]
l4[0][1]
D1={1:'achal',2:'apporva',3:'hitesh','dean':'dhiraj'}
D1
D1.keys()
D1.items()
D1[1]
D1['dean']
l1
d2={'a':l1,'b':l3}
d3=d2
d2
#d3.pop('b')
d3['c']=d3.pop("b")
d3
d3
d3['c'][3]='lalit'
d3

for lalit in d2:
    print(lalit)
    print(d2[lalit],end='')

l1=[1,2,3,4,5,5]
s1=set(l1)
type(s1)
s1
s2=set()
s2[1]

a=set([1,2,3,4])
a
a1=set([1,2,3,a])
a1
type (a)
a3=set([1,2,l1])
a4=set([])


set1= set([1,2,3,4])
set2=set([4,5,6,7])
setc=set([1,2,4,5])
set1.intersection(set2)
set1-set2
set2-set1
set1|set2
set1^set2
len(set1)
any(set1)
set4=([1,2,None,5])
set4
any(set4)
all(set1)
set1.remove(1)
set1.discard(1)
set1.discard(2)
set1.pop(3)
set2
set3
set1.isdisjoint(set2)
setaaaaaaaaaaaaa
