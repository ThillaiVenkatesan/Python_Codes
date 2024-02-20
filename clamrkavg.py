#class mark calc and avg calc
class Student:
    mark1,mark2,mark3=100,100,100
    def process(self):
        sum=Student.mark1+Student.mark2+Student.mark3
        avg=sum/3
        print("total marks=",sum)
        print("average marks=",avg)
S=Student()
S.process()
