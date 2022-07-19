'''
The Value is Directly Updated
class Ineuron:
    def __init__(self):
        self.student='Data Science'

    def Students(self):
        print('The Name of the Student is,',self.student)

i=Ineuron()
i.student='Data Analytics'
i.Students()
'''


class Ineuron1:
    def __init__(self):
        self.__student_var='Data Science'#private Variable

    def Students(self):
        print('The Name of the Student is,',self.__student_var)
    def Student_Change(self):
        self.__student_var='Big  Data will get Updated'

i1=Ineuron1()
#i1._Ineuron1__student_var='Data Analytics' Here it will update
i1.Students()
i1.__student_var='Data Analytics'# hre it will not update
i1.Students()
i1.Student_Change()
i1.Students()
