#This is a demonstration module
#it is used to get classes from vehicles module
#We are going to create our objects here and call the functions available in the vehilcles ,odule
#We will create objects for the SUV.car and truck

import vehicles
#import the module of the classes for the car
def main():
	#create a main function for storing the objects
	#start with the car by entering its input
	print("Please enter the data for the car :")
	make=input("Make type of the car: ")
	model=input("The Model of your car: ")
	mileage=input("Its Mileage: ")
	price=input("Its price: ")
	doors=input("Number of doors: ")
	#create the object cars to be used to access the car data
	cars=vehicles.Car(make,model,mileage,price,doors)

	print()
	#enter details for the suv vehicle
	print('SUV details')
	make=input("Make type of the SUV: ")
	model=input("The Model of your SUV: ")
	mileage=input("Its Mileage: ")
	price=input("Its price: ")
	pass_cap=input("Passenger capacity: ")
	#create aan object suv to be used to acces the suv data
	suv=vehicles.SUV(make,model,mileage,price,pass_cap)

	print()
	#Enter the details for the truck
	print("Trucks details ")
	make=input("Make type of the car: ")
	model=input("The Model of your car: ")
	mileage=input("Its Mileage: ")
	price=input("Its price: ")
	drive_type=input("Drve type i.e 4WD or 2WD: ")
	#cretae the object truct to be used to access the data for the truck
	trucks=vehicles.Truck(make,model,mileage,price,drive_type)
#Dispaly the data you entered
#We are using the fumctions plus the objects we have to display the data 
	print("Here is the details for the cars in the inventory!!: ")
	print("CAR DETAILS: ")
	print("CAR Make type :",cars.get_make())
	print("Car Model: ",cars.get_model())
	print("Car Mileage: ", cars.get_mileage())
	print("Car cost: ", cars.get_price())
	print("Number of doors of the car: ", cars.get_doors())

	print("Here is the details for the suv vehicles in the inventory!!: ")
	print("SUV DETAILS: ")
	print("SUV Make type :",suv.get_make())
	print("SUV Model: ",suv.get_model())
	print("SUV Mileage: ",suv.get_mileage())
	print("SUV cost: ", suv.get_price())
	print("Total SUV capacity: ", suv.get_pass_cap())


	print("Here is the details for the trucks in the inventory!!: ")
	print("TRUCK DETAILS: ")
	print("SUV Make type :",trucks.get_make())
	print("Truck Model: ",trucks.get_model())
	print("Truck Mileage: ", trucks.get_mileage())
	print("Truck cost: ", trucks.get_price())
	print("Truck drive type: ", trucks.get_drive_type())
#Call the function 
main()

