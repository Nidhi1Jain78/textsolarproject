import cv2
img=cv2.imread("solar-system.jpg")


#sun
cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(205,255,255))
#mercury
cv2.putText(img,"Mercury",(120,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(171,251,279))
#venus
cv2.putText(img,"Venus",(220,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(567,105,255))
#Earth
cv2.putText(img,"Earth",(320,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(562,255,5))
#Mars
cv2.putText(img,"Mars",(420,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,106,35))
#Jupiter
cv2.putText(img,"Jupiter",(520,350),cv2.FONT_HERSHEY_COMPLEX,0.5,(134,25,225))
#Saturn
cv2.putText(img,"Saturn",(770,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,245))
#Uranus
cv2.putText(img,"Uranus",(950,280),cv2.FONT_HERSHEY_COMPLEX,0.5,(195,255,255))
#Neptune
cv2.putText(img,"Neptune",(1070,280),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,25,255))
cv2.imshow("output",img)

cv2.waitKey(0)