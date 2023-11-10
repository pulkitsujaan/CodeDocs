class A:
    def met(self):
        print("This is a method from class A")
class B(A):
    def met(self):
        print("This is a method from class B")
class C(A):
    def met(self):
        print("This is a method from class C")
class D(B, C):
    def met(self):
        print("This is a method from class D")
a=A()
b=B()
c=C()
d=D()
print(d.met())
#compiler confuse ho jaayega ki kahan jaana h, isliye multiple inheritence ko avoid krna chahiye
#kuch languages(java) multiple inheritance support hi ni krti
#iss problem ko diamond shape problem kehte hain...