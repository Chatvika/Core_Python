s = {2,3,4,5,6}
b = {7,5,9}
print(s,type(s))
s.add(9)
print(s)
s.remove(4)
print(s)
s.discard(999)
print(s)
s.update(s)
print(s)
'''s.clear()
print(s)'''
print(s.union(b))

print(s.intersection(b))
print(s.difference(b))