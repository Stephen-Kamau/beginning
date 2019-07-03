#Here we will import our module (accountclass.py)
#this module is used to put objects to the classes in the accountclass
#import the accountclass module which contains other classes

import accountclass

def main():
	#Enter details for the saving account
	print("Enter details for saving account")

	acc_Num=input("Account Number for saving: ")
	bal=input("Account balance: ")
	int_rate=input("Intrest Rate: ")

	#create an object i.e savings that will be used to acces data typed
	print()
	savings=accountclass.savingAccount(acc_Num,bal,int_rate)
	print("Enter details for the deposit account")
	print()

    
    #Enter details for the deposit account
	acc_Num=input("Account Number for deposit: ")
	bal=input("Account balance: ")
	int_rate=input("Intrest Rate: ")
	maturity=input("Maturity Date: ")
#create the object i.e deposit to access details from the depositaccount classs
	deposit=accountclass.depositAccount(acc_Num,bal,int_rate,maturity)

#print the details for the saving accounts using the functions defined

	print()
	print("Detailss you enterd for your saving account are: ")
	print("Account Number: ", savings.get_acc_Num())
	print("Account Balance: ",savings.get_balance())
	print("Intrest Rate: ",savings.get_int_rate())
#print the details for the saving accounts using the functions defined
	print()
	print("Details for deposit account are the following:")
    

	print("Account Number: ", deposit.get_acc_Num())
	print("Account Balance: ", deposit.get_balance())
	print("Intrest Rate: ", deposit.get_int_rate())
	print("Maturity date: ", deposit.get_maturity_date())
#finally call the function
main()