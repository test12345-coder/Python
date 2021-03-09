def __foo__(number):
    for i in range(2, number+1):
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            print(i)

if __name__ == '__main__':
    number = int(input("Lütfen sayıyı gir = "))
    __foo__(number)
