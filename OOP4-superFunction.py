class Human():
    def __init__(self, name__ , surname__ , length__):
        self.name = name__
        self.surname = surname__
        self.length = length__
        
    def printVar(self):
        print(f'{self.name} {self.surname} {self.length}')
 
class Student(Human):
    def __init__(self , name__, surname__, length__, grade__):
        super().__init__(name__, surname__, length__)
        self.grade = grade__
    
    def printVar(self):
        print(f'{self.name} {self.surname} {self.length} {self.grade}')

if __name__ == '__main__':
    Ahmet = Student('Ahmet','Necdet',100000,100000)
    Ahmet.printVar()   