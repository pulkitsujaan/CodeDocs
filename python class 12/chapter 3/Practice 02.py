'''Use of Replace'''
choice='''Dear <NAME>
You are selected for this exam.
Please contact before date <DATE>
Regards,
'''
name=input("Enter the name: ")
date=input("Enter the date: ")
choice=choice.replace("<NAME>",name)
choice=choice.replace("<DATE>",date)

print(choice)