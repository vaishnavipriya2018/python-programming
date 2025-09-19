class stud:
    def __init__(self,a,b,c,m1,m2,m3):
        self.sno=a
        self.sname=b
        self.sage=c
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    
    def calculate(self): 
        self.tot=m1+m2+m3
        self.avg=self.tot/3
        print('total marks=' ,self.tot)
        print('average=',self.avg)
        if m1>=40 and m2>40 and m3>40:
            self.result='pass'
        else:
            self.result='fail'
    def display(self):
        print('Student no:',self.sno)
        print('Student name:',self.sname)
        print('Student age:',self.sage)
        print('mark1=:',self.mark1)
        print('mark2=:',self.mark2)
        print('mark3=:',self.mark3)
        print('total=:',self.tot)
        print('average=:',self.avg)
        print('result=:',self.result)  
x=int(input('Enter roll no:'))
y=input('Enter name:')
z=int(input('Enter age:'))
m1=int(input('enter mark1:'))
m2=int(input('enter mark2:'))
m3=int(input('enter mark3:'))
obj=stud(x,y,z,m1,m2,m3)
obj.calculate()
obj.display()

              
