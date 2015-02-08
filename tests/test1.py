import cv2

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return d1
    return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(0)  

winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    
while True:
    img = diffImg(t_minus, t, t_plus)
    ret,th1 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                        cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                        cv2.THRESH_BINARY,11,2)
    contours,hierarchy = cv2.findContours(th1, 1, 2)
    #cv2.drawContours(img, contours, -1, (255,0,0), 5)
    if contours:
        cnt = contours[0]
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00']) if M['m00'] else 0
        cy = int(M['m01']/M['m00']) if M['m00'] else 0
        #if not cx or not cy:
        #  continue
        cv2.rectangle(img,(cx-5,cy-5),(cx+5,cy+5),(255,0,0),2)
        print cx, cy
    cv2.imshow( winName, img )

    # Read next image
    t_minus = t
    t = t_plus
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    key = cv2.waitKey(45)
    if key == 27:
       cv2.destroyWindow(winName)
       break
    
print "Goodbye"




