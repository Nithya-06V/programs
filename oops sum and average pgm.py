class student:
    mark1=10
    mark2=20
    mark3=30
    def process(self):
        sum=student.mark1+student.mark2+student.mark3
        avg=sum/3
        print("totalmark:",sum)
        print("average of:",avg)
        return
r=student()
r.process()
