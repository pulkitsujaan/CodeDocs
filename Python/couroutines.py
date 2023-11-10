"""Couroutines"""
import time
def search():
    #some 4 second time consuming task
    book=open("names(couroutines).txt")
    time.sleep(4)
    try:    
        while True:
            text= (yield)
            if text in book:
                print("Your text is in the book\n")
            else:
                print("Your text is not in the book\n")
    except Exception as f:
        print(f)
    finally:
        book.close()
searcH=search()
next(searcH)
texttocheck=input("Enter a text to check in the list\n")
searcH.send(texttocheck)