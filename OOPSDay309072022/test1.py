#MultiLevel INheritenca
class Bank:
    def transaction(self):
        print('Total Transaction Value')
    def account_opening(self):
        print('This weill sow open status')
    def deposite(self):
        print('This wipp show you deposit avount')

class HDFC(Bank):
    def HDFC_TO_ICICI(self):
        print('This will you all trainsction happended to ICICI through HDFC')

class ICICI(HDFC):
    pass

i=ICICI()
i.HDFC_TO_ICICI()
i.deposite()
i.account_opening()
