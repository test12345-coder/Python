class Human:
    name = ''
    surname = ''
    length =  0
    
    def printVar(self):
        print(f'{self.name} {self.surname} {self.length}')
        
if __name__ == '__main__':
    S4d0 = Human()
    S4d0.name = 'Saadettin'
    S4d0.surname = 'Atay'
    S4d0.length = 100
    S4d0.printVar()
    