class sample:
    num=0
    def __init__(self,var):
        sample.num+=1
        self.var=var
        print("the object value is=",self.var)
        print("the count of object created:",sample.num)
    def __del__(self):
        sample.num-=1
        print("object with value %d is exit from the scope"%self.var)
s1=sample(15)
s2=sample(35)
s3=sample(45)
del s1,s2,s3
