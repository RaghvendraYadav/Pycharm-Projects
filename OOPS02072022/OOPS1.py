class Person:
    def __init__(self,fname,lname,yob,email):
        self.fname=fname
        self.lname=lname

        self.email=email
        self.yob=yob
Anuj=Person('Anuj','Sharma',1998,'Anuj@123')
Ayush_var=Person('Ayush','Jain',2002,'Ayush@123')# self is just a reference variable
print(Anuj.fname,Anuj.email,end='\n')
print(Ayush_var.fname ,Ayush_var.email)
print(type(Anuj))



