class Human:
    name = ''
    surname = ''
    length =  0
    
    def __init__(self, __name__ , __surname__ , __length__):
        self.name = __name__
        self.surname = __surname__
        self.length = __length__
        
    def printVar(self):
        print(f'{self.name} {self.surname} {self.length}')
        
if __name__ == '__main__':
    S4d0 = Human('Saadettin','Atay',100)
    S4d0.printVar()
    