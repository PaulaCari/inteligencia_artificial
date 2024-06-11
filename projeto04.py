'''Projeto 4
Inteligencia artificial     vision computacional'''

import cv2
import mediapipe as mp

from cvzone.HandTrackingModule import HandDetector    #modulo de rastarmento de mãos  *

webcam = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8, maxHands=2) #modelo IA detectionCon=0.8 é a confiança minima vai utilizar 80% 2 mãos ou 4*

while True:
    sucesso, imagem = webcam.read()

    coodenadas, imagem_maos = rastreador.findHands(imagem) # chamo o modelo de IA   *

    #print(coodenadas)   #pega os dados da mao no terminal as cordenada e posso fazer uma  aplicações aumentar o diminui o volumen, pausar o video,voltar,adiantar, para jogo

    cv2.imshow("pojeto 4 - IA", imagem)

    if cv2.waitKey(1) != -1:   # ele retorna -1 internamente
        break
    
webcam.release()
cv2.destroyAllWindows()
