from nsfw_detector import NSFWDetector
from IPython.display import display
import PIL
from PIL import Image

from resizeimage import resizeimage
#screenshot import
import time
import cv2
import mss
import numpy
import os
import sys
import random
#hotkey
from pyautogui import press, typewrite, hotkey
#sound
import playsound
# for screen resolution
import ctypes
import win32gui
from win32gui import GetWindowText, GetForegroundWindow




print('loading model')
detector = NSFWDetector('./nsfw.299x299.h5')
#detector_mobilenet = NSFWDetector('./nsfw_mobilenet2.224x224.h5')
print('model loaded')

os.system("sound.py")

#WERE THE FUN BEGIN
def punishment():
    hotkey('ctrl', 'w')
    os.system("sound.py")
    #for filename in os.listdir("punishment/"):
        #if filename.endswith(".jpg") or filename.endswith(".png"):
             # print(os.path.join(directory, filename))
             #im = Image.open("punishment/"+filename)
             #im.show()




def demo():

        i=0
        while (i<50):
            last_time = time.time()
            i=i+1



            with mss.mss() as sct:
                padding = 0
                screenshot_square_size=299
                #geting screen resolution
                print(GetWindowText(GetForegroundWindow()))

                left,top,max_left,max_top=win32gui.GetWindowRect(GetForegroundWindow())
                print(str(left)+' '+str(top)+' '+str(max_left)+' '+str(max_top))


                #top = 0
                #left = 0
                #user32 = ctypes.windll.user32
                #user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
                #max_top = user32.GetSystemMetrics(1)#get screen height
                #max_left = user32.GetSystemMetrics(0)


                while top < max_top :
                    #reinitialize left variable for each row
                    left = 0
                    while left < max_left :



                        # Part of the screen to capture
                        monitor = {'top': top, 'left': left, 'width': screenshot_square_size, 'height': screenshot_square_size}
                        # Get raw pixels from the screen, save it to a Numpy array
                        img = numpy.array(sct.grab(monitor))
                        #the 100 stand for the quality of the image (100%)
                        img = cv2.resize(img, (299, 299))
                        cv2.imwrite('data/'+str(top)+' '+str(left)+' '+str(max_left)+' '+str(max_top)+'.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 100])




                        # Predict single image
                        result = detector.predict('data/'+str(top)+' '+str(left)+' '+str(max_left)+' '+str(max_top)+'.jpg')
                        # {'2.jpg': {'sexy': 4.3454722e-05, 'neutral': 0.00026579265, 'porn': 0.0007733492, 'hentai': 0.14751932, 'drawings': 0.85139805}}

                        #get category that has the max value
                        final_cat = {k:max(v,key=v.get) for k,v in result.items()}
                        for key, value in final_cat.items():
                            final_cat = str.join("", value)

                        print(final_cat)
                        if(final_cat == "porn" or final_cat =="sexy"):
                            punishment()
                            id=random.randint(0, 200)
                            cv2.imwrite('data/triggered/'+final_cat+' '+str(id)+'.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 100])





                        left = left + screenshot_square_size + padding
                        #print(str(top)+' '+str(left))
                    top = top + screenshot_square_size + padding
             #print(result)

            # Display the picture in grayscale
            # cv2.imshow('OpenCV/Numpy grayscale',
            # cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

            #print('fps: {0}'.format(1 / (time.time()-last_time)))
demo()
