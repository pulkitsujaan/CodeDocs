'''
string slicing and functions
'''
story="this is a very long string and you can perform any operation on this string."



# print(story[1:7])
# print(story[:6])#same as [0:6]
# print(story[6:])#same as [6:len(story)]

'''negative indices are given in the way...the last index is -1 and they decrease going from last to first index...for eg:
 s  t  r  i  n  g
 0  1  2  3  4  5  --> +ve indices
-6 -5 -4 -3 -2 -1 ---> -ve indices
'''
# print(story[-40:-1])

# print(story[0:11:2])#third index is used to skip charecters..2 means it will print the second charecter after the previous





# #String Functions
# print(len(story))#length of string
# print(story.endswith("ing."))#bool output...Tells whether provided ending is true or not.
# print(story.count("a"))#counts the specific iterations of given input
# print(story.capitalize())#capitalizes first letter of string
# print(story.find("this"))#finds and tells the first index of string...if not present, then returns -1..when input is repeated then it returns index of first iteration
# print(story.replace("this","It"))#replaces all iterations of 'this' with 'it'




#Escape Sequences
string="Pulkit said to her,\"So this is it?\""
print(string)
'''Escape sequences are used to print certain charecters which cannot be printed directly. For eg:\n-newline, \t-tab, \'-single quote, \"-double quote'''