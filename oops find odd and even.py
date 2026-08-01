class number:
    def check(self,a):
        if a%2==0:
            print("the number is even")
        else:
            print("the number is odd:")
t=number()
x=int(input("enter the value"))
t.check(x)
