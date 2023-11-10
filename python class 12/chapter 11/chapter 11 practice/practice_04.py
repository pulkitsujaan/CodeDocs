class Complex():
    def __init__(self,real,imaginary) -> None:
        self.real=real
        self.image=imaginary

    def __str__(self):
        if self.image<0:
            return f'{self.real} - {-self.image}i'
        else:
            return f'{self.real} + {self.image}i'

    def __add__(self,another):
        sum_real=self.real+another.real
        sum_image=self.image+another.image
        if sum_image<0:
            return f'{sum_real} - {-sum_image}i'
        else:
            return f'{sum_real} + {sum_image}i'
        
    
    def __mul__(self,another):
        mul_real=(self.real*another.real)-(self.image*another.image)
        mul_image=(self.real*another.image)+(self.image*another.real)
        if mul_image<0:
            return f'{mul_real} - {-mul_image}i'    
        else:
            return f'{mul_real} + {mul_image}i'
    

com1=Complex(3,2)
com2=Complex(1,-70)
print(com1)
print(com2)

print(f'sum= {com1+com2}')
print(f'Multiplication={com1*com2}')