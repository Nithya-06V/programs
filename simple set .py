a={1,2,3}
b={3,4,5}
c={5,7,6}
d={7,8,9}
c=a.copy()
c |= b
print(c)
d=a.copy()
d &= b
print(d)
