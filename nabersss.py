import cv2
import pyttsx3

# Yüz tanıma için OpenCV'nin Cascade Sınıflandırıcı kullanılacak
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Sesli yanıt için pyttsx3 kullanılacak
engine = pyttsx3.init()

def recognize_face():
    # Kamera yakalamasını başlat
    cap = cv2.VideoCapture(0)

    # İsimi saklamak için boş bir değişken tanımla
    isim = None

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            # Yüz algılandıysa, kullanıcıdan isim al
            if isim is None:
                isim = input("Yüz tanındı! Lütfen isminizi girin: ")
                engine.say(f"Merhaba, {isim}!")
                engine.runAndWait()

            # Yüzü çerçeve içine al
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Yüz Tanıma', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_face()
