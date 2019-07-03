#we are going to define methods and attributes for an employee
#From a certain company
#This class will hold the general data for the employee
#create the employee class
class Employee:
	#create the constructor or initializer for the class
	def __init__(self,name,ID_NO,department,job_title):
		self.__name=name
		self.__ID_NO=ID_NO
		self.__department=department
		self.__job_title=job_title
	#create the methods that will be used to define the functions
	def set_name(self,name):
		self.__name=name
	def set_ID_NO(self,ID_NO):
		self.__ID_NO=ID_NO
	def set_department(self,department):
		self.__department=department
	def set_job_title(self,job_title):
		self.job_title=job_title
	#create the methods to set data to them
	#these methods will return the employee data once called
	def get_name(self):
		return self.__name
	def get_ID_NO(self):
		return self.__ID_NO
	def get_department(self):
		return self.__department
	def get_job_title(self):
		return self.__job_title

