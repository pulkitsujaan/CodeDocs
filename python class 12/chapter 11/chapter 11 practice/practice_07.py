class Vector:
    def __init__(self,vec) -> None:
        self.vec=vec
    def __str__(self):
        vector=''
        index=0
        for i in self.vec:
            vector +=f' {i}s{index} +'
            index+=1
        return vector[:-1]
    
    def __add__(self,vec2):
        newList=[]
        if len(self.vec)==len(vec2.vec):
            for i in range(len(self.vec)):
                newList.append(self.vec[i] + vec2.vec[i])
            return Vector(newList)
        else:
            return 'Addition failed. Vectors are of different dimensions'
    
    def __mul__(self,vec2):
        sum=0
        if len(self.vec)==len(vec2.vec):
            for i in range(len(self.vec)):
                sum+= self.vec[i]+ vec2.vec[i]
            return sum
        else:
            return 'Multiplication failed. Vectors are of different dimensions'
    
    # this code written for problem, else is copied from problem 5
    def __len__(self):
        return len(self.vec)

v1=Vector([1,2,3])
v2=Vector([2,3])
print(v1+v2)
print(len(v1))
print(len(v2))