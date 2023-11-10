# def func_name(a,*x,**y):
def func_name(x):
    # print(type(y))
    for i in x:
        print(i)
    print("dictionary starts from here\n")
    # for key, value in y.items():
    #     print(f"{key} is {value}")
lst1=["pulkit", "gunjan", "ayushi", "dady", "mummy","me"]
normal=56
dct1={"Pulkit":"Junior","gunjan":"elder","ayushi":"older","Dady":"Senior"}
# func_name(normal,*lst1,**dct1)
func_name(lst1)