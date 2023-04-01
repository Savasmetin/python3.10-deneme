import pywhatkit as kit

try :              #Gönderilecek num #Yazı              #Gönderilecek saat

        kit.sendwhatmsg("+905380846522","'bu bir deneme mesajıdır' python botu",13,20)
        print("Gönderme başarılı.")
except :
    print("Beklenmeyen bir hata oluştu.")