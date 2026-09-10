import array as my_array
a=my_array.array("i",[10,20,30,40,50])

print(a[1:3])
print(a)
print(a[3])

a.append(60)
print(a)

a.pop()
print(a)

a.insert(3,35)
print(a)

a.remove(35)
print(a)

a[1]=25
print(a)

print(a.index(40))

b=my_array.array("u",'tridev')
print(b)

c=my_array.array('d',[1.1,2.2,3.3,4.4,5.5])
print(type(c))
