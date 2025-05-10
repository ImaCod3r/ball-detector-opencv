import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Nao foi possivel abrir a webcam.")
    exit()
    
while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar imagem.")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.medianBlur(gray, 5)
    
    circles = cv2.HoughCircles(
        gray_blurred,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=100,
        param1=100,
        param2=50,
        minRadius=10,
        maxRadius=100
    )
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for x, y, r in circles[0, :]:
            # draw circle
            cv2.circle(frame, (x, y), r, (0, 255, 255), 2) 
            # center
            cv2.circle(frame, (x, y), 2, (0, 255, 255), 3) 
            # write "ball"
            cv2.putText(frame, "Ball", (x - 20, y - r - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
    cv2.imshow("Ball detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()