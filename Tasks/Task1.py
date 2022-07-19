# Eg 1 for Constructor
import logging as lg
lg.basicConfig(filename='Task1.log',level=lg.DEBUG,format='%(asctime)s  %(levelname)s  %(message)s')

class Ineuron:
    lg.info('Inside the Class Ineuron')
    def __init__(self,no_of_courses):
        self.no_of_courses=no_of_courses
        lg.info('Inside the Constructor')
    def total_courses(self):
        print('The no of courses in Ineuron are:-',self.no_of_courses)
        lg.info('Inside the total_courses function')

try:
    lg.info('Inside the try Block')
    i=Ineuron(30)
    i.total_courses()
    lg.info('Try Block executed successfully')
except Exception as e:
    lg.error(e)

# Eg 2
class Students:
    lg.info('Inside the Students Class ')
    def __init__(self):
        self.__total_no_of_Students=2000
        lg.info('Inside the Constructor')
    def Student_Enrolled(self):
        lg.info('Total Students Enrolled are :-',Students.__total_no_of_Students)

s=Students()
lg.info(s._Students__total_no_of_Students)



# Eg 3
class Internship:
    def __init__(self,level1,subject,no_of_months,Industry):
        self.level1=level1
        self.subject=subject
        self.no_of_months=no_of_months
        self.Industry=Industry

    def Internship_Level(self):
        lg.info(str(self.level1))
''' def  Internship_Time(self):
        lg.info('the Duration for internship is',self.no_of_months)
    def Internship_Subject(self):
        lg.info('The Subject Knowledge requiered is ',self.subject)

    def Internship_Industry(self):
        lg.info('The Industu=ry for the Internship is  ',self.Industry)'''


inter=Internship('Medium','Data Science','9','Agriculture')
inter.Internship_Level()






