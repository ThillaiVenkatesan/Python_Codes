n=int(input("ENTER THE NO. OF STUDENTS IN CLASS:"))
class std:
    name=[]
    tmarks=[]
    total=[]
    
    def getinf(self):
        for i in range(n):
             self.mark=[]
             self.name.append(input("ENTER THE NAME OF STUDENT:"))
             for j in range(0,6):
                 self.mark.append(int(input("ENTER THE MARK IN SUBJECT:")))
             self.tmarks.append(list(self.mark))
    def tot(self):
        for i in range(n):
            self.total.append(sum(self.tmarks[i]))
    def  print(self):
        for i in range(n):
            print("\n\nTHE NAME OF STUDENT:",self.name[i],"\n", "THE MARKS SCORED:",self.tmarks[i],"\n","THE TOTAL:",self.total[i])
s=std()
s.getinf()
s.tot()
s.print()
            
