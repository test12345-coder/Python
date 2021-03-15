def armstrong(number):
  sayı = str(number)
  power = len(sayı)
  toplam = 0
  for eleman in sayı:
    toplam += int(eleman) ** power
  if toplam == number:
    print(number ,"bu sayı Armstrong sayısıdır")
  else:
    print(number, "bu sayı Armstrong sayısı değildir")


if __name__ == '__main__':
  armstrong(8208) # True
  armstrong(1234) # False
