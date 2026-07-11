signal=input("enter the signal:")
if signal in "Ee":
    print("2G")
elif signal in "Hh":
    print("3G")
elif signal in ("H+,h+"):
    print("4G")
else:
    print("others")
    
