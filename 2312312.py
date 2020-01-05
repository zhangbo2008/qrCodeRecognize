
import cv2
import numpy as np

# img = cv2.imread('23.png')
# img = cv2.imread('1.jpg')
img = cv2.imread('66.jpg')
img = cv2.imread('1.jpg')
img = cv2.imread('2.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img_gray.shape[1],img_gray.shape[0])
img2=cv2.resize(img_gray, (img_gray.shape[1],img_gray.shape[0],), interpolation = cv2.INTER_AREA)

#横竖每100个像素进行切分,然后每一次平移50.



#先得到所有小框的左上点的坐标(x,y),平移量是50

save=[]
x=0
while 1:
    if x in range (img_gray.shape[0]):
        save.append(x)
        x+=50
    else:
        break


save2=[]
x=0
while 1:
    if x in range (img_gray.shape[1]):
        save2.append(x)
        x+=50
    else:
        break
from itertools import product
save3=[]
for i, j in product(save, save2):
    save3.append((i,j))



print(save3)










# cv2.imshow('222',img2)
# cv2.waitKey()
result_detection = None
count_experiments = 2
transform = None
qrcode = cv2.QRCodeDetector()
save4=[100,150,200,250,300] #表示小框的大小
def main():
    for i in range(count_experiments):
        for j in save3:
            for kuang in save4:
                # 检测与识别
                a = qrcode.detect(img_gray[j[0]:j[0]+kuang,j[1]:j[1]+kuang])
                if a[0]:
                  return True
    return False

print(main())