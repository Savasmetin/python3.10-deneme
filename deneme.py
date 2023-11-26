while True:
    print("-------------------------------------")
    print("1. asal kontrol")
    print("2. çıkış")
    secim = int(input("lütfen yapmak istediğiniz seçimimn numarasını giriniz. "))

    if secim == 1:
        a = int(input("lütfen bir sayı giriniz: "))
        i = 2
        while i < a:
            if a % i == 0:
                print("bu say asal değildir")
                break
            i +=1
        else:
            print("bu sayı asaldır")
    elif secim == 2:
        break
    else:
        print("geçerli bir sayı giriniz.")
        continue
