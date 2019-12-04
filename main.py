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
#hotkey
from pyautogui import press, typewrite, hotkey
# for screen resolution
import ctypes
import win32gui
from win32gui import GetWindowText, GetForegroundWindow
import time
# for archive function
import shutil

def punishment():
    """function for everything you want to trigger when porn is detected"""
    hotkey('ctrl', 'w')

def predict(img, top, left, max_left, max_top):
    # Predict single image
    result = detector.predict('data/'+str(top)+' '+str(left)+' '+str(max_left)+' '+str(max_top)+'.jpg')
    # {'2.jpg': {'sexy': 4.3454722e-05, 'neutral': 0.00026579265, 'porn': 0.0007733492, 'hentai': 0.14751932, 'drawings': 0.85139805}}

    #get category that has the max value
    final_cat = {k:max(v,key=v.get) for k,v in result.items()}
    for key, value in final_cat.items():
        final_cat = str.join("", value)


    if(final_cat == "porn" or final_cat =="sexy"):
        print(final_cat)
        punishment()
        id = time.strftime("%Y%m%d-%H%M%S")
        cv2.imwrite('data/triggered/'+final_cat+' '+str(id)+'.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 100])

def screenshot():
    """Function that take multiple squared screenshot of the active window. """
    with mss.mss() as sct:

        #geting position and size of the active window
        print(GetWindowText(GetForegroundWindow()))
        try:
            left,top,max_left,max_top=win32gui.GetWindowRect(GetForegroundWindow())
            #print(str(left)+' '+str(top)+' '+str(max_left)+' '+str(max_top))
        except Exception as e:
            raise e

        #increase padding for better performance / less accuracy
        padding = 40
        #299px is the size require for the model to analyse the picture
        screenshot_square_size=max_left

        while top < max_top :
            #reinitialize left variable for each row
            left = 0
            while left < max_left :
                try:
                    # Part of the screen to capture
                    monitor = {'top': top, 'left': left, 'width': max_left, 'height': max_left}
                    # Get raw pixels from the screen, save it to a Numpy array
                    img = numpy.array(sct.grab(monitor))
                    #the 100 stand for the quality of the image (100%)
                    img = cv2.resize(img, (299, 299))
                    cv2.imwrite('data/'+str(top)+' '+str(left)+' '+str(max_left)+' '+str(max_top)+'.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 100])
                    #predicting the image
                    predict(img,top, left, max_left, max_top)

                except Exception as e:
                    print(e)

                left = left + screenshot_square_size + padding
                #print(str(top)+' '+str(left))
            top = top + screenshot_square_size + padding

def archive_screenshot(source_path, destination_path):
    files_names = os.listdir(source_path)
    try:
        os.makedirs(destination_path); ## creates the destination folder
    except Exception as e:
        print(str(e),len(files_names))

    for name in files_names:
        if name.endswith('.jpg'):
            srcname = os.path.join(source_path, name)
            dstname = os.path.join(destination_path, name)
            shutil.move(srcname, dstname)

def loop():
    """Keep the script going."""
    #definine how long it will run
    i=0
    while (i<500):
        last_time = time.time()
        i=i+1
        time.sleep(0.5)
        screenshot()

print('loading model')
"""Loading the weight for the model."""
detector = NSFWDetector('./nsfw.299x299.h5')
print('model loaded')

loop()
archive_screenshot("data/","data/archive/")
archive_screenshot("data/triggered/","data/archive/triggered_arch/")


#def main():

#if __name__ == '__main__':
#    main()
