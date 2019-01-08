import cv2  
  
img = cv2.imread('./test3.png')  
# w, h, c = img.shape
# img = cv2.resize(img, (w*3, h*3), c)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,130,255,cv2.THRESH_BINARY)  
  
rsImg, contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(rsImg,contours,-1,(0,0,255),3)  

cv2.imshow("img", rsImg)  
cv2.waitKey(0)  
