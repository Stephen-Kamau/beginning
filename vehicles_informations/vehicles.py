#this is a module that contains general data for the vehicles
#It contains class for the vehicles

#This class is found in all vehicles
class Automobiles:
	def __init__(self,make,model,mileage,price):
		self.__make=make
		self.__model=model
		self.__mileage=mileage
		self.__price=price

	def set_make(self,make):
		self.__make=make
	def set_model(self,model):
		self.__model=model
	def set_mileage(self,mileage):
		self.__mileage=mileage
	def set_price(self,price):
		self.__mileage=mileage
	def get_make(self):
		return self.__make
	def get_model(self):
		return self.__model
	def get_mileage(self):
		return self.__mileage
	def get_price(self):
		return self.__price


#creating the second class for only cars 
#it will inherit general data from the automobiles class
class Car(Automobiles):
 	def __init__(self,make,model,mileage,price,doors):
 		Automobiles.__init__(self,make,model,mileage,price)
 		self.__doors=doors
 	def set_doors(self,doors):
 		self.__doors=doors
 	def get_doors(self):
 		return self.__doors

#creating another class that will be for tructs
#It will inherit general data from the automobile class

class Truck(Automobiles):
	def __init__(self,make,model,mileage,price,drive_type):
		Automobiles.__init__(self,make,model,mileage,price)
		self.__drive_type=drive_type
	def set_drive_type(self,drive_type):
		self.__drive_type=drive_type
	def get_drive_type(self):
		return self.__drive_type


#creating another class for a sporting vehicle called SUV
#this class will also inherit the methods from the automobile class
#here is the class definition

class SUV(Automobiles):
	def __init__(self,make,model,mileage,price,pass_cap):
		Automobiles.__init__(self,make,model,mileage,price)
		self.__pass_cap=pass_cap
	def set_pass_cap(self,pass_cap):
		self.__pass_cap=pass_cap
	def get_pass_cap(self):
		return self.__pass_cap
