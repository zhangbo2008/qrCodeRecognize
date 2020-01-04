
import cv2
import numpy as np

# img = cv2.imread('23.png')
# img = cv2.imread('1.jpg')
img = cv2.imread('999.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


result_detection = None
count_experiments = 10
transform = None
qrcode = cv2.QRCodeDetector()

for i in range(count_experiments):
    # 检测与识别
    a = qrcode.detect(img_gray)
    print(a)
