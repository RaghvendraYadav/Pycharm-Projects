class Person:
    def age(self,current_year,birth_year):
        return current_year-birth_year
    def email(self,email_id):
        print(email_id)
    def ask_name(self):
        name=input('Enter your name')
        return name

    def ask_dob(self):
        dob=input('tell me the date of birth')
        return dob

sudh=Person()
anuj=Person()
Ayush=Person()
print(sudh.ask_name())
sudh.email('sudh@gmail.com')
print(Ayush.ask_dob())
