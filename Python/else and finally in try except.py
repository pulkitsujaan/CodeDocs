#try, except, finally and else
#try helps not to stop the execution
#except runs if there comes an error
#'finally' runs anyway after try and except
#else is printed only when except is not executed
#You should write 'finally' at the last
f1=open("new1.txt")
try:
    f=open("random.txt")
except Exception as e:
    print("This is except\n",e)
else:
    print("This is else")
finally:
    print("Run this anyway")
    f.close()
    f1.close()
print("Execution complete")