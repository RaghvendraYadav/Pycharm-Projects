import test2
print(test2)
obj3=test2.Person1('Ragh','Yadav',1998)
print(obj3.yob)
print(obj3._name1)
class Person:
    _name= "sudh"
    __surname="Kumar"
    yob=1990

    def _age(self, current_year):
        return current_year- self.yob
    def __age1(self, current_year):
        return current_year- self.yob

obj=Person()
print(obj._age(2022))
print(obj._Person__age1(2022))
class employee(Person) :
      _name="Sudhanshu"
      __surname='Singh'
      yob=1991


obj1=employee()
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._Person__surname)
print(obj1._employee__surname)
print(obj1._age(2022))
print(obj1._Person__age1(2023))