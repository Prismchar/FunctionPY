def toplama(x, y):
    return x + y
def cikarma(x, y):
    return x - y
def carpma(x, y):
    return x * y
def bolme(x, y):
    return x / y
print("islem seciniz(1,2,3,4")
while True:
        secim = input("secenek giriniz:")
        if secim in ('1', '2', '3', '4'):
            try:
                deger1 = float(input("birinci degeri giriniz:"))
                deger2 = float(input("ikinci degeri giriniz:"))
            except ValueError:
                print("gecersiz deger")
                continue

        if secim == '1':
            print(deger1,'+', deger2, "=", toplama(deger1,deger2))
        elif secim == '2':
            print(deger1,'-', deger2, "=", cikarma(deger1,deger2))
        elif secim == '3':
            print(deger1, '*', deger2, "=", carpma(deger1, deger2))
        elif secim == '4':
            print(deger1, '/', deger2, "=", bolme(deger1, deger2))
        sonraki_hesaplama = input("başka bir hesaplama yapmak istiyor musunuz? (E/h):")
        if sonraki_hesaplama == "h":
         break
else:
        print("gecersiz deger")


