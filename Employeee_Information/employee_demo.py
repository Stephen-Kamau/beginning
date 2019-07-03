#Here we will create objects to access the employee data from the class we created
#the objects will be used to return the data using the methods defined

#We need to import the classes from the modules we created
#We will import the employeedata class

import employeedata

#create the functions to be used for object definition and accessing
def main():
	#Enter the general data for the employee
	print("Please enter the data for the employee bellow: ")
	name=input("Enter the name of the employee: ")
	id_no=input("Enter his or her id number: ")
	department=input("DEpartment in which he is found: ")
	job_title=input("Enetr the title of the job he or she is specilised in: ")

#create an object emp to be used to access the methods from the employee class
	emp=employeedata.Employee(name,id_no,department,job_title)

	print()
	#output the data
	#Here you will call the methods used to get data
	print("Here is the details for the employee")
	print("Name: ", emp.get_name())
	print("ID number: ", emp.get_ID_NO())
	print("DEpartment: ",emp.get_department())
	print("Jon title: ", emp.get_job_title())
#call the main function
main()