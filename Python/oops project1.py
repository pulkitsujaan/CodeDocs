class library:
    def __init__(self,listofbooks,libraryname):
        self.lend_data= {}
        self.listofbooks=listofbooks
        self.libraryname=libraryname
        for books in self.listofbooks:
            self.lend_data[books]=None
    def displaybook(self):
        print("Books in Library:\n")
        for book in (self.listofbooks):
                print(f"{book}")

    def borrowbook(self,book,readername):
        if book in self.listofbooks:
            if self.lend_data[book] is None:
                self.lend_data[book]=readername
                print("booklend")
            else:
                print(f"Sorry, this book is lend by {self.lend_data[book]}")
        else:
            print("Wrong Book Name\n")
    def returnbook(self,book,readername):
            if book in self.listofbooks:
                if self.lend_data[book] is not None:
                    if self.lend_data[book]==readername:
                        self.lend_data[book]=None
                        print("Thank You for returning this book\n")
                    else:
                        print("You have not borrowed this book....Try again\n")
                else:
                    print("This book is not lend....Try again\n")
            else:
                print("Wrong book name....Try again\n")
    def addbook(self,bookname):
        if bookname not in self.listofbooks:
            self.listofbooks.append(bookname)
            print("Book added")
        else:
            print("We already have this book...")
    def deletebook(self,bookname):
        if bookname in self.listofbooks:
            self.listofbooks.remove(bookname)
            print("Book deleted")
        else:
            print("Wrong Book Name\n")
# print(user1.borrowbook)
def main():
    defaultbooks=["Harry Potter and the Philosopher's stone","Harry Potter and the Chamber of Secrets","Harry Potter and the prisoner of askbaan"]
    _user=library(defaultbooks,"Pulkit")
    print(f"------Welcome to your library------\n\nTo lend book---l\nTo return book---re\nTo add book---a\nTo delete a book---d\nTo show all books----sh\n\nPress 'q' to exit\n\n")
    stop=False
    while(stop is not True):
        _choice=input("Enter your choice:")
        if(_choice=='q'):
            print("\nThanks for visiting, see you again....\n")
            stop=True
        elif (_choice=="sh"):
            print(_user.displaybook())
        elif(_choice=='l'):
            _lendername=input("What is your name?\n")
            _lenderbook=input("What is the name of the book?(Case Sensitive)\n")
            _user.borrowbook(_lenderbook,_lendername)
        elif(_choice=='a'):
            _bookname=input("What is the name of that book?\n")
            _user.addbook(_bookname)
        elif(_choice=='d'):
            _passkey=input("Enter the passkey to continue\n")
            if (_passkey=="456102"):
                _bookname=input("Which book do you want to delete?\n")
                _user.deletebook(_bookname)
            else:
                print("Couldn't process your request(Wrong passkey)")
        elif(_choice=="re"):
            _book=input("What is the name of that book?(Case Sensitive)\n")
            _username=input("What is your name?\n")
            _user.returnbook(_book,_username)

if __name__=="__main__":
    main()