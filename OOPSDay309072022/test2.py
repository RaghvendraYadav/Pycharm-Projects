#Mutlple Inheritance
# Multiple Inheritance can inherit more classes at a Time and for mthof overloading sequnece maters
class Bank:
    def transaction(self):
        print('Total Transaction Value')
    def account_opening(self):
        print('This weill sow open status')
    def deposite(self):
        print('This wipp show you deposit avount')
    def test(self):
        print('This is a test Method from Bank ')

class HDFC:
    def HDFC_TO_ICICI(self):
        print('This will you all trainsction happended to ICICI through HDFC')
    def test(self):
        print('This is a test Method from HDFC Bank ')
class Ineuron_Bank:
    def account_status(self):
        print('Account status in neuron')
class ICICI(HDFC,Bank,Ineuron_Bank):# here the order depend on the sequence of the class for method over loading
    pass

i=ICICI()
i.HDFC_TO_ICICI()
i.deposite()
i.account_opening()
i.test()
i.account_status()