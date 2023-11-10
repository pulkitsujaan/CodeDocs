# f= open("new1.txt", "w")
# a = f.write("Pulkit op")
# print(a)#to check charecters wrote
# f.close

f= open("new2.txt", "r+")
# f.write("Pulkit op")
print(f.read())
f.write("\nCodie")
f.close

