names=[]
marks=[]
print("Enter the number of student you want to input their data")
x=input()
while len(names)<int(x):
	name=input("Enter the name of the student\n")
	names.append(name)
	print("Enter the total marks scored in five subjects")
	mark=input()
	marks.append(mark)
	
print("The names and marks are: ",names,marks)