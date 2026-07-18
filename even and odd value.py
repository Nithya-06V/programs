l=[]
for i in range(10):
    a=int(input("enter the value"))
    l.append(a)
print(l)
for i in l:
    if i%2==0:
        print("even:",i)
    else:
        print("odd:",i)
