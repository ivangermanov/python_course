import cv2

#show captured video in window
#keep the frames high
#quit it by pressing 'q' and release everything
#count the number of frames

video=cv2.VideoCapture(0)
a=1

while True:
    a=a+1
    check, frame=video.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(check)
    print(frame)

    cv2.imshow("Capturing..", frame)

    if cv2.waitKey(1) == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()