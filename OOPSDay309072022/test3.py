# Method Overriding

class Ineuron:
    def Student(self):
        print('The Details of the Students')
    def Achievers(self):
        print('List of all the Acheivers')
    def Hall_of_Fame(self):
        print('Print everyone from HALL OF Fame')
class Ineuron_VISION(Ineuron):
    def Student(self):
        print('Thesr are the Filter Students')


iv= Ineuron_VISION()
iv.Student()


