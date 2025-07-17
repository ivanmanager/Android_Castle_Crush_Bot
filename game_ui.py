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

class GameUI:
    time_delay=0.01
    gv = GameVals()
    gs = GameState()
    DecCount = 0
    lib = None
    Screenshot = None
    PageState = None

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
            
        self.Screenshot = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        match self.PageState:
            case 'StartPage':
                if self.findImgAndClick('battle_btn.png'):
                    self.PageState = 'BattlePage'
                    print('Click Battle button...')
            case 'BattlePage':
                cardPath =  os.path.join(os.getcwd(), self.gv.imageFolderName, 'Cards')
                cardFileNames = os.listdir(cardPath)
                for cardfilename in cardFileNames:
                    self.findImgAndDrag(cardfilename, [720, 300], 0.85)

                self.findImgAndClick('battle_btn.png')


    def findImgAndDrag(self,imageName, tgtPos, precision = 0.90):
        cardPath =  os.path.join(os.getcwd(), self.gv.imageFolderName, 'Cards')
        imfname = cardPath + '\\' + imageName
        pos = self.imagesearch(imfname, precision)
        if pos[0] != -1:
            self.swipe_image(imfname, pos, tgtPos, offset=5)
            return True
        return False


    def findImgAndClick(self,imageName, precision = 0.90):
        absolute_path = os.path.join(os.getcwd(), self.gv.imageFolderName, imageName)
        pos = self.imagesearch(absolute_path, precision)
        if pos[0] != -1:
            self.click_image(absolute_path, pos, offset=5)
            return True
        return False


    def click_image(self, image, pos, offset=5):
        img = cv2.imread(image)    
        height, width, channels = img.shape
        cmdstr = 'shell input tap ' + str(pos[0] + int(self.r(width / 2, offset))) + ' ' + str(pos[1] + int(self.r(height / 2, offset)))
        self.lib.android_bridge_cmd(cmdstr.encode('ASCII'))

        
    def swipe_image(self, image, pos, tgtPos, offset=5):
        img = cv2.imread(image)    
        height, width, channels = img.shape
        cmdstr = 'shell input swipe ' + str(pos[0] + int(self.r(width / 2, offset))) + ' ' + str(pos[1] + int(self.r(height / 2, offset))) + ' ' + str(tgtPos[0] + offset) + ' ' + str(tgtPos[1] + offset)
        self.lib.android_bridge_cmd(cmdstr.encode('ASCII'))


    def imagesearch(self, image, precision=0.8):
        im = self.Screenshot
        img_rgb = np.array(im)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(image, 0)
        template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(str(min_val)+','+str(max_val))
        if max_val < precision:
            return [-1, -1]
        return max_loc

    def r(self, num, rand):
        return num + rand * random.random()

    def log_info(self, str):
        print(str)
        logging.info(str)