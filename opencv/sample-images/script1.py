import cv2
import glob2, os

os.chdir("sample-images")
images=glob2.glob("*.jpg", recursive=True)
print(images)
for img in images:
    current_img=cv2.imread(img, 0)
    resized_img=cv2.resize(current_img, (100,100))
    cv2.imwrite("resized_"+img,resized_img)