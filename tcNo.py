''' 
1- TC Kimlik no 11 haneli rakamdan oluşur.
2- İlk rakam 0 olamaz.
3- 1, 3, 5, 7 ve 9. hanelerin toplamının 7 katı ile 2, 4, 6 ve 8 hanelerin toplamı çıkarılır
    ve sonucun 10'a bölümünden kalanı 10. haneyi verir.
4- İlk 10 hanenin toplamının 10'a bölümünden kalan, son haneyi verir.
'''

def __tc10ve11Hane__(a = []): # 3. ve 4. adımları kontrol ediyor 
    tekToplam = 0
    ciftToplam = 0
    for i in range(0, 10):
        if i % 2 == 0 and i != 10:
            tekToplam += int(a[i])*7
        elif  i != 9:
            ciftToplam +=  int(a[i])
    if ((tekToplam - ciftToplam) % 10) != int(a[9]):
            print("Bu TC kimlik numarası hatalı..")
            exit()
    toplam = 0        
    for i in range(0, 10):         
        if i != 10:    
            toplam += int(a[i])
    if (toplam % 10) == int(a[10]):
        print("Girdiğiniz TC kimlik numarası doğru")
    else:
        print("Girdiğiniz TC kimlik numarası yanlış")
    exit()


if __name__ == "__main__":
    _input_ = input("Lütfen TC kimlik numaranızı giriniz = ")
    tcNo = list(_input_)
    if len(tcNo) != 11:
        print("TC kimlik numarası 11 haneden oluşmalıdır...")
        exit()

    if tcNo[0] == '0':
        print("Bu TC kimlik numarası hatalı...") 
        exit()
    
    __tc10ve11Hane__(tcNo)
