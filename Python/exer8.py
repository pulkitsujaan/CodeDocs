"""Oh! soldier, pretify my folder"""
import os
# input path
# input dictionary file
# capitalize the word---string.capitalize
# to check the extension---m.endswith()

def soldier(path,dictfile,format,format2):
    try:
        os.chdir(path)
        
        #define some important lists and variables
        files=os.listdir()
        i=1
        
        # make a list of objects from the given dictonary file of restricted file names
        with open(dictfile) as f:
            lst1=f.read().split("\n")
        
        # capitalize names of files
        for items in files:
            if items not in lst1:
                os.rename(items,items.capitalize())
        
        # change images name to serial numbers
            if os.path.splitext(items)[1] == format or os.path.splitext(items)[1] == format2:
                os.rename(items,f"{i}.{format}")
                i+=1
        # print(os.listdir(),"\n")
    except Exception as p:
        print(p)
soldier(r"C:\Users\HP\Desktop\exer8\Endgame charector posters","D:\Code docs\Python\dictfile.txt",".png",".jpeg")