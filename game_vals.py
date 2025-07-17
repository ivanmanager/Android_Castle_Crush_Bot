import os

class GameVals:
    cards = {}
    sliced_cards = {}
    borders = []

    # Variables related to screen size
    ScreenSize = "FullScreen"
    imageFolderName = 'Images'

    def __init__(self):

        if self.ScreenSize == "FullScreen":            
            #self.imageFolderName = 'FullScreenImages'
            self.imageFolderName = 'MobileImages'



 
