#using classes for a bank account demo


#Begginging with the saving accounts
class savingAccount:
        def __init__(self,acc_Num,int_rate,bal):
            self.__acc_Num=acc_Num
            self.__int_rate=int_rate
            self.__balance=bal


        #setting up the methods for the attributes declared
        def set_acc_Num(self,acc_Num):
            self.__acc_Num=acc_Num

        def set_int_rate(self,int_rate):
            self.__int_rate=int_rate

        def set_balance(self,bal):
            self.__balance=bal

        #definitions of methods that will be used to get the
        #methods declared above
        def get_acc_Num(self):
            return self.__acc_Num

        def get_int_rate(self):
            return self.__int_rate

        def get_balance(self):
            return self.__balance



  
  #creating a deposit account to inherit the
  #methods of the saving accoutnt
class depositAccount(savingAccount):
        ##create an init functions including all attributes
        def __init__(self,acc_Num,bal,int_rate,maturity_date):
            self.__maturity_date=maturity_date
            #inherit the methods from the saving account class
            savingAccount.__init__(self,acc_Num,int_rate,bal)
            #set the maturity date function
        def set_maturity_date(self,maturity_date):
            self.__maturity_date=maturity_date
        #define method to return maturity date
        def get_maturity_date(self):
            return self.__maturity_date
