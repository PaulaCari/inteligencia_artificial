import cv2
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(0)

while True:
    sucesso, imagem = webcam.read()
    cv2.imshow("pojeto 4 - IA", imagem)

    if cv2.waitKey(1) != -1:   # ele retorna -1
        break
    
webcam.release()
cv2.destroyAllWindows()