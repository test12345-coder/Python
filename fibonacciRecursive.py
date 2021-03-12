def fibo(x):
    if x == 0 or x == 1:
        return x 
    else:
        return fibo(x-1) + fibo(x-2) 

if __name__ == '__main__':
    print(fibo(15)) 
