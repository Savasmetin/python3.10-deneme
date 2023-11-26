import cv2

# Kamerayı aç
video_capture = cv2.VideoCapture(0)  # Varsayılan kamera (genellikle 0) veya bir video dosyası seçebilirsiniz.

# Önceki çerçeve
prev_frame = None

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
            cv2.putText(frame, "Merhaba, Hos Geldiniz!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    prev_frame = gray

    # Kareyi görüntüle
    cv2.imshow('Motion Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı kapat
video_capture.release()

# Pencereleri kapat
cv2.destroyAllWindows()
