
import cv2
import numpy 
mycolor = [[107,0,0,179,255,255],#blue
          [51,179,93,179,255,130],#green
          [20,0,233,63,255,255],#yellow
          [18,159,176,21,255,255],#brown
          [0,135,176,0,255,255],#red
          [0,0,0,179,0,255]]#white
cnt=[[1],
    [2],
    [3],
    [4],
    [5],
    [6]]
points=[]


def findcolor(img,mycolor,colorval):
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    x,y,w,h=0,0,0,0
    for color in mycolor:
        lower = numpy.array(color[0:3])
        upper = numpy.array(color[3:6])
        mask  = cv2.inRange(imghsv,lower,upper)
        countour,h=cv2.findContours(mask ,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for con in countour:
            peri=cv2.arcLength(con,True)
            approx = cv2.approxPolyDP(con,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
            area=cv2.contourArea(con)
           
            if len(approx)==4 and area>1000:
                cv2.putText(imgcopy,str(cnt[count]),((x+w//2),(y+h//2)),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,0),2)
        count+=1
        

img =cv2.imread("cube-face.png")
imgcopy =img.copy()
findcolor(img,mycolor,cnt)
cv2.imshow("df",imgcopy)
cv2.waitKey(0)
    
    







