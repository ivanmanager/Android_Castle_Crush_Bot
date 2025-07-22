import time
import os
import sys
import random
from Card import Card
from GameState import GameState
from Action import Action
from datetime import datetime
from game_vals import GameVals
import cv2
import numpy as np
import platform
from  ctypes import *
from PIL import Image
import logging
import random

class GameUI:
    time_delay=0.01
    gv = GameVals()
    gs = GameState()
    DecCount = 0
    lib = None
    Screenshot = None
    PageState = None
    Width = 0
    Height = 0
    LaneCoef = [0.64, 0.42, 0.24]

    current_directory = os.getcwd()
    AndroidBridgePath = current_directory + '/platform-tools'
    AndroidBridgeLib = AndroidBridgePath + '/android_bridge.dll'

    def __init__(self):
        logfilename = 'castle_crush_bot_log.txt'
        logging.basicConfig(filename=logfilename, encoding='utf-8', format='%(asctime)s : %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
        print('Wait for few seconds connecting phone...')
        logging.info('Wait for few seconds connecting phone...')
        self.lib = cdll.LoadLibrary(self.AndroidBridgeLib)
        readyFlag = self.lib.android_bridge_init(self.AndroidBridgePath.encode('ASCII'))
        if not readyFlag:
            print('No devices connected.')
            logging.error('No devices connected.')
            exit(0)
        
        cmdstr = ' shell monkey -p com.tfgco.games.strategy.free.castlecrush -c android.intent.category.LAUNCHER 1'
        self.lib.android_bridge_cmd(cmdstr.encode('ASCII'))
        self.PageState = 'StartPage'
    
     
    #######################################
    ### Main Functions
    #######################################

    def UpdateGameState(self):

        ret = self.lib.android_screen_capture()
        if not ret:
            print('Cannot capture screenshot of the phone.')
            logging.error('Cannot capture screenshot of the phone.')

        imgfile = self.AndroidBridgePath + '/screenshot.png'

        img = cv2.imread(imgfile)
        self.Screenshot = img    
        ##self.Screenshot = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        match self.PageState:
            case 'StartPage':
                if self.findBattleBtnClick():
                    self.PageState = 'BattlePage'
                    print('Click Battle button...')
                if self.ClickYesOkBtn():
                    self.PageState = 'BattlePage'
                    print('Click Yes button...')

            case 'BattlePage':
                cardPath =  os.path.join(os.getcwd(), self.gv.imageFolderName, 'Cards')
                cardFileNames = os.listdir(cardPath)
                #for cardfilename in cardFileNames:
                #    self.findImgAndDrag(cardfilename, [720, 300], 0.85)

                pts = self.FindCardReady()
                random_lane = random.randint(1, 3) - 1
                if pts != []:
                    LaneY = int(self.LaneCoef[random_lane] * self.Width)
                    cmdstr = 'shell input swipe ' + str(pts[0][0]) + ' ' + str(pts[0][1]) + ' ' + str(int(self.Height/2)) + ' ' + str(LaneY)
                    print(cmdstr)
                    self.lib.android_bridge_cmd(cmdstr.encode('ASCII'))


                self.ClickYesOkBtn()
                self.findBattleBtnClick()

    def log_info(self, str):
        print(str)
        logging.info(str)

    def findBattleBtnClick(self):
        img = self.Screenshot
        imdim = img.shape
        width = imdim[0]
        height = imdim[1]
        self.Width = width
        self.Height = height
        subimg = img[:,int(height/3):int(2*height/3),:]
        BlueTextColor = [60, 3, 125]
        tol = 15
        blue_thresh = cv2.inRange(subimg, np.array([BlueTextColor[2] - tol, BlueTextColor[1] - tol, BlueTextColor[0] - tol]), np.array([BlueTextColor[2] + tol, BlueTextColor[1] + tol, BlueTextColor[0] + tol]))
        contours,hirachy = cv2.findContours(blue_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        count = 0
        ObjArea = []
        for cnt in contours:
            count = count + 1
            ObjArea.append(cv2.contourArea(cnt))

        maxv = 0
        if count != 0:
            maxv = max(ObjArea)
                
        if maxv > 7000:
            max_idx = ObjArea.index(maxv)
            M = cv2.moments(contours[max_idx])
            x,y,w,h = cv2.boundingRect(contours[max_idx])

        else:
            return False

        cropImg = subimg[y:y+h*2,x:x+w,:]
        WhiteTextColor = [250, 250, 250]
        white_thresh = 255 - cv2.inRange(subimg, np.array([WhiteTextColor[2] - tol, WhiteTextColor[1] - tol, WhiteTextColor[0] - tol]), np.array([WhiteTextColor[2] + tol, WhiteTextColor[1] + tol, WhiteTextColor[0] + tol]))

        pos = [x+int(w/2)+int(height/3), y+h]
        cmdstr = 'shell input tap ' + str(pos[0]) + ' ' + str(pos[1])
        self.lib.android_bridge_cmd(cmdstr.encode('ASCII'))

        return True

    def FindCardReady(self):
        img = self.Screenshot

        imdim = img.shape
        width = imdim[0]
        height = imdim[1]
        self.Width = width
        self.Height = height
        totalS = width * height        
        subimg = img[int(2*imdim[0]/3):imdim[0],0:int(height*0.9375),:]
        hsv_img = cv2.cvtColor(subimg, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_img)
        ##ret,bw = cv2.threshold(s, 0, 55, cv2.THRESH_BINARY)
        pts = []
        
        mask = cv2.inRange(s, 0, 10)
        contours,hirachy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        NumOfPreparingCards = 0
        ylist = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > totalS*0.01 and area < totalS*0.1:
                NumOfPreparingCards = NumOfPreparingCards + 1
                x,y,w,h = cv2.boundingRect(cnt)
                ylist.append(y)

        if NumOfPreparingCards == 0:
            print('No cards ready.')
            return []
        detectArea = subimg[ylist[0]:ylist[0]+int(height*0.03),:,:]
        DiodColor = [20, 150, 220]
        tol = 50
        blue_thresh = cv2.inRange(detectArea, np.array([DiodColor[2] - tol, DiodColor[1] - tol, DiodColor[0] - tol]), np.array([DiodColor[2] + tol, DiodColor[1] + tol, DiodColor[0] + tol]))
        kernel = np.ones((3,3), np.uint8) 
        cleaned_image = cv2.morphologyEx(blue_thresh, cv2.MORPH_OPEN, kernel)

        kernelSize = int(height * 0.02)
        kernel = np.ones((kernelSize,kernelSize), np.uint8)
        dilated_image = cv2.dilate(cleaned_image, kernel, iterations=1)
        
        contours,hirachy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        NumOfAvailableCards = len(contours)

        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            pt = [x + w, y + ylist[0] + h + int(2*imdim[0]/3)]
            pts.append(pt)
            ##cv2.rectangle(subimg, (x,y+ylist[0]),(x+w, y+ylist[0]+h), (0,255,0), 3)
            
        print('Preparing Cards Number = ' + str(NumOfPreparingCards))
        print('Available Cards Number = ' + str(NumOfAvailableCards))
        return pts


    def ClickYesOkBtn(self):
        img = self.Screenshot
        imdim = img.shape
        width = imdim[0]
        height = imdim[1]
        self.Width = width
        self.Height = height
        totalS = width * height
        subimg = img[:,int(height/3):int(2*height/3),:]
        tol = 20
        GreenColor = [0, 150, 50]
        green_thresh = cv2.inRange(subimg, np.array([GreenColor[2] - tol, GreenColor[1] - tol, GreenColor[0] - tol]), np.array([GreenColor[2] + tol, GreenColor[1] + tol, GreenColor[0] + tol]))
        contours,hirachy = cv2.findContours(green_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        DetectYesOkBtn = False
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > totalS*0.003 and area < totalS*0.01:
                DetectYesOkBtn = True
                x,y,w,h = cv2.boundingRect(cnt)
                cmdstr = 'shell input tap ' + str(int(x + w/2 + height/3)) + ' ' + str(int(y + h/2))
                self.lib.android_bridge_cmd(cmdstr.encode('ASCII'))
                break
                
        return DetectYesOkBtn
