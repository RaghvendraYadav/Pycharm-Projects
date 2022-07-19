class Person:
    def __init__(rg,fname,lname,yob,email):
        rg.fname=fname
        rg.lname=lname
        rg.email=email
        rg.yob=yob
    def cal_age(self,current_year):
        return current_year-self.yob
Anuj=Person('Anuj','Sharma',1998,'Anuj@123')
Ayush_var=Person('Ayush','Jain',2002,'Ayush@123')# self is just a reference variable
print(Anuj.fname,Anuj.email,end='\n')
print(Ayush_var.fname ,Ayush_var.email)
print(type(Anuj))
print(Anuj.fname+' '+Anuj.lname)
print(Anuj.cal_age(2022))
