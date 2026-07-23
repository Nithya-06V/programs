count={'chunk':1,'annie':42,'jan':100}
lst=list(count.keys())
print(lst)
lst.sort()
for key in lst:
    print(key,count[key])
