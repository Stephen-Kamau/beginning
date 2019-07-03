'''password validation for computer devives in an institution
It must meet the following conditions:
it must be made up of more than seven characters
it must be made up of atleast on digit
it must be made up of atleast on uppercase
it must be made up of atleast on lowercase
'''
def input_getting():
	password=input("Please Enter the password for the electronic devices :\n")


	correct_length = False
	has_digit = False
	has_uppercase = False
	has_lowercase = False

	#begin validation of the password

	if len(password) >= 7:
		correct_length = True
		for x in password:
			if x.isupper():
				has_uppercase = True
			if x.islower():
				has_lowercase = True
			if x.isdigit():
				has_digit = True


	if correct_length and has_digit and has_lowercase and has_uppercase:
		is_valid=True
		print("Your password has been created successfully \n \
			Please start using the following as your pasword : " ,password)

	else:
		is_valid = False
		print("The password does not reach the minimum requiremend! ")
		print("Do you want to try another one ? ....")
		response=input("Type y to try another option...")
		if response == Y or response == y:
			password=input("Try another option for another password...")




input_getting()