class C2dVector():
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def __str__(self):
        return f'{self.i}i + {self.j}j'

class Vector3D(C2dVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k=k
    
    def __str__(self):
        return f'{self.i}i + {self.j}j + {self.k}k'
    
vec1=C2dVector(2,5)
vec2=Vector3D(3,4,6)

print(vec1)
print(vec2)