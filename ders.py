import cv2
from gtts import gTTS
import os


# Kamera aç
cameraIndex = 156
video_capture = cv2.VideoCapture(0)

# Önceki çerçeve
prev_frame = None

# Yüz tespiti için Haar Cascade modelini yükle
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    # Kameradan bir çerçeve al
    ret, frame = video_capture.read()

    if not ret:
        break

    # Gri tonlamalı hale getir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if prev_frame is not None:
        # Kareler arasındaki farkı hesapla
        frame_diff = cv2.absdiff(prev_frame, gray)

        # Farkın ortalamasını hesapla
        frame_diff_mean = frame_diff.mean()

        if frame_diff_mean > 20:  # Eşik değeri, hareket algılamasının hassasiyetini ayarlar
            cv2.putText(frame, "Merhaba, Hoş Geldiniz!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Yüz tespiti yap
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Yüzleri çerçevele
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Kareyi görüntüle
            cv2.imshow('Motion Detection', frame)
            cv2.waitKey(1)



    prev_frame = gray

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı kapat
video_capture.release()

# Pencereleri kapat
cv2.destroyAllWindows()
