some_list=[1, 2, 1, 1]
res=set(some_list)
res2=[x for x in res if some_list.count(x)==1]
print(res2[0])


