
# Single Inheritance
class car:
    def __init__(self,body,engine,tyre):
        self.body=body
        self.engine=engine
        self.tyre=tyre

    def milage(self):
        print('The Milage of the Car is:')

class TATA(car):
    pass

#  t=TATA() here we need to pass three Variable same as the Parent Arguments
c=car('sold','v6','Radial')
print(c)
t=TATA('sold','v8','Radial1')
print(t)