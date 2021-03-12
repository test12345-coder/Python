'''
Mükemmel sayı, sayılar teorisinde, kendisi hariç pozitif tam bölenlerinin toplamı 
kendisine eşit olan sayı. Diğer bir ifadeyle, bir mükemmel sayı, bütün pozitif tam 
bölenlerinin toplamının yarısına eşittir. (Wikipedia)
'''

def perfectNum(number):
    count= 0
    for i in range(number-1,  0, -1):
        if number % i == 0:
            count += i
        if i == 1 and count == number:
            print("True")
        elif i == 1:
            print("False")

if __name__ == '__main__':
    perfectNum(6) # True
    perfectNum(3) # False
