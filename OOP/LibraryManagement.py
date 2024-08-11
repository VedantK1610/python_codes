class Library:
    def __init__(self,books,no_of_books):
        self.books=books
        self.no_of_books=no_of_books
    def check(self):

        if(len(self.books)!=self.no_of_books):
            print("Wrong")
        else:
            print("Right")

Flag=False
while Flag==False:
    books=[i for i in input("Enter Book names: ").split()]
    num=int(input("Enter number of books:"))
    a=Library(books,num)
    a.check()
    ui = input("Do you want to repeat: Y/N")
    if ui.lower()=="n":
        Flag=True
    else:
        Flag=False
