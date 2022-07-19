
from Util.Util import Person2

obj6 = Person2('Rag','Sharma',1992)
print(obj6.yob)

class Person1 :
    def __init__(self,name,surname,yob):
         self._name1= name#here _name is protected
         self.__surname1= surname#Here__Surname is private
         self.yob=yob


sudh = Person1('SUdhanshu','Kumar',1990)
print(sudh._name1)
#print(sudh.__surname here we will get error bcoz __surname is private variable
print(sudh._Person1__surname1)# here for calling Private varialbe we wil use object._classname__variableName