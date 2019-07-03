print("Please Enter the name of your file you wish to write on:")
x=input()
yourfile=open(x+".txt","w+")
names=[]#declare an empty list for the names to be filled.
prices=[]#declare an empty list for the prices to be filled.
x=input("Please enter the number of items you wish to purchse")
while len(names)<int(x):
	name=input("Enter the each element :")
	names.append(name)
	price=input("Enter the price for the item :")
	prices.append(price)
for name in names:
	yourfile.write('%s\n'% name+"%s:")+str(yourfile.write(price))#this is formated so that each item from the list can be on its own line.
'''y=0
while y<int(x):
	for name in names:
		print(names[y],":",prices[y])
		y+=1'''
	
