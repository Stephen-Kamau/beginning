booksfile=open("booksfile.txt","w+")
books=[]#define an empty list where books will be appended
print("Please enter the number of books you wish to borrow:")
#ask for the number of books to be borrowed
x=input()
print("Enter the the title of the books borrowered:")
while len(books)<int(x):#this line can also be written as for book in range(int(x)):
	title=input()
	books.append(title)#append is used for adding an item to the list 
for book in books:#for loop for iterating through the list and return ach each item from the list.
	print(book)
for book in books:
	booksfile.write('%s\n'% book)#this is formated so that each item from the list can be on its own line.
























