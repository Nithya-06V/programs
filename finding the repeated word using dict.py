words='brontosaurus'
d=dict()
for c in words:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)        
