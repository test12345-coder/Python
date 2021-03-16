class Human:
    name = ''
    surname = ''
    length =  0
     
    def printVar(self):
        print(f'{self.name} {self.surname} {self.length}')
 
class Student(Human):
    grade = 0   
    
    def printVar(self):
        print(f'{self.name} {self.surname} {self.length} {self.grade}')    

if __name__ == '__main__':
    Ahmet = Student()
    Ahmet.name = 'Ahmet'
    Ahmet.surname = 'Sezer'
    Ahmet.length = 1000000
    Ahmet.grade = 1000000
    Ahmet.printVar()   