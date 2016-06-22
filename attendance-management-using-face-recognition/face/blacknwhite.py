import cv2
for i in range(1,4):
    imgname="temp/"+str(i)+".png"
    imgray=cv2.imread(imgname,cv2.CV_LOAD_IMAGE_GRAYSCALE)
    (thres,im_bw)=cv2.threshold(imgray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imwrite(imgname,im_bw)
