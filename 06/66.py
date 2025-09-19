import copy
sn1=[1,2,3,[2,3,4],4,4]
b=sn1.copy()
c=copy.deepcopy(sn1)
b.append(8)
c[3].append("33333")
print(c)
print(sn1)
print(b)
print(id(sn1))
print(id(b))
a=(1,24,3)
d=a



print(a)
print(d)

print(id(a))
print(id(d))
print("-"*40)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)