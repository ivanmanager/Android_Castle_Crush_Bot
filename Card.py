class Card:
    name = ''
    path = ''
    cost = 1
    pos = []
    cardsInfo1 = []
    cardsInfo2 = []
    XSTEP = 0
    YSTEP = 0

    def __init__(self):
        self.XSTEP = 254
        self.YSTEP = 302

        self.cardsInfo1 = [{'name':'Angel', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':1, 'Yid':6},
                     {'name':'Archerqueen', 'nickname':'RangedsKing', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':1, 'Yid':5},
                     {'name':'Archerstribe', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':1, 'Yid':4},
                     {'name':'Blackknight', 'nickname':'MegaOrc', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':1, 'Yid':3},
                     {'name':'Catapult', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':1, 'Yid':2},
                     {'name':'Demon', 'Attack':178, 'Health':516, 'Range':0, 'Speed':6, 'Damage':886, 'Xid':1, 'Yid':1},
                     {'name':'Dragon', 'Attack':178, 'Health':516, 'Range':0, 'Speed':6, 'Damage':886, 'Xid':2, 'Yid':6},
                     {'name':'Executioner', 'nickname':'BigSplash', 'Attack':178, 'Health':516, 'Range':0, 'Speed':6, 'Damage':886, 'Xid':2, 'Yid':5},
                     {'name':'Jester', 'Attack':81, 'Health':484, 'Range':0, 'Speed':4, 'Xid':2, 'Yid':4},
                     {'name':'Lotsofskeltons', 'Attack':81, 'Health':484, 'Range':0, 'Speed':4, 'Xid':2, 'Yid':3},
                     {'name':'Mage', 'Attack':145, 'Health':355, 'Range':25, 'Speed':4, 'Xid':2, 'Yid':2},
                     {'name':'MiniArchers', 'Attack':25, 'Health':97, 'Troops':2, 'Range':25, 'Speed':6, 'Xid':2, 'Yid':1},
                     {'name':'Minionsking', 'Attack':25, 'Health':97, 'Troops':2, 'Range':25, 'Speed':6, 'Xid':3, 'Yid':6},
                     {'name':'Minitank', 'Attack':25, 'Health':97, 'Troops':2, 'Range':25, 'Speed':6, 'Xid':3, 'Yid':5},
                     {'name':'Mudelemental', 'Attack':25, 'Health':97, 'Troops':2, 'Range':25, 'Speed':6, 'Xid':3, 'Yid':4},
                     {'name':'OrcWarrior', 'Attack':103, 'Health':910, 'Range':0, 'Speed':7, 'Xid':3, 'Yid':3},
                     {'name':'Pirate', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':3, 'Yid':2},
                     {'name':'Reaper', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':3, 'Yid':1},
                     {'name':'Scout', 'nickname':'FastMelee', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':4, 'Yid':6},
                     {'name':'Shaman', 'nickname':'IllusionGuy', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':4, 'Yid':5},
                     {'name':'Siege', 'nickname':'SuperRanged', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':4, 'Yid':4},
                     {'name':'Skelton', 'Attack':27, 'Health':107, 'Troops':3, 'Range':0, 'Speed':7, 'Xid':4, 'Yid':3},
                     {'name':'Standard', 'nickname':'StandardBear', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':4, 'Yid':2},
                     {'name':'Stormelemental', 'nickname':'WindElemental', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':4, 'Yid':1},
                     {'name':'Tank', 'nickname':'Golem', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':5, 'Yid':6},
                     {'name':'Vampire', 'Attack':27, 'Health':107, 'Troops':3, 'Range':0, 'Speed':7, 'Xid':5, 'Yid':5},
                     {'name':'Witch', 'nickname':'BlackWitch', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':5, 'Yid':4},
                     {'name':'Arrows', 'Attack':27, 'Health':107, 'Troops':3, 'Range':0, 'Speed':7, 'Xid':5, 'Yid':3},
                     {'name':'Blizzard', 'nickname':'unknown', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':5, 'Yid':2},
                     {'name':'Bomb', 'Damage':110, 'Effect':25, 'Xid':5, 'Yid':1},
                     {'name':'CastleRecovery', 'nickname':'unknown', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':6, 'Yid':6},
                     {'name':'Fireball', 'nickname':'unknown', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':6, 'Yid':5},
                     {'name':'Flameexplosion', 'nickname':'Inferno', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':6, 'Yid':4},
                     {'name':'Genielamp', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':6, 'Yid':3},
                     {'name':'Gustofwind', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':6, 'Yid':2},
                     {'name':'Manaramp', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':6, 'Yid':1},
                     {'name':'Natureheal', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':7, 'Yid':6},
                     {'name':'Rage', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':7, 'Yid':5},
                     {'name':'Resurrection', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':7, 'Yid':4},
                     {'name':'Ritual', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':7, 'Yid':3},
                     {'name':'Scarecrow', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':7, 'Yid':2},
                     {'name':'Thunder', 'Attack':97, 'Health':242, 'Range':25, 'Speed':5, 'Xid':7, 'Yid':1}]

        self.cardsInfo2 = [{'name':'Apepirate', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':1, 'Yid':1},
                     {'name':'Dryad', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':1, 'Yid':2},
                     {'name':'Geisha', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':1, 'Yid':3},
                     {'name':'Metamorph', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':1, 'Yid':4},
                     {'name':'Fireelemental', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':2, 'Yid':1},
                     {'name':'Hollowknight', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':2, 'Yid':2},
                     {'name':'Magician', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':2, 'Yid':3},
                     {'name':'Skeletonsinvocation', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':2, 'Yid':4},
                     {'name':'Iceelemental', 'nickname':'IceGolem', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':3, 'Yid':1},
                     {'name':'Necromancer', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':3, 'Yid':2},
                     {'name':'Phoenix', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':3, 'Yid':3},
                     {'name':'Unchaineddemon', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':3, 'Yid':4},
                     {'name':'Orcshorde', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':4, 'Yid':1},
                     {'name':'Skeletonstribe', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':4, 'Yid':2},
                     {'name':'Spikedstatue', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':4, 'Yid':3},
                     {'name':'Cannonshot', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':4, 'Yid':4},
                     {'name':'Skullqueen', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':5, 'Yid':1},
                     {'name':'Valkyrie', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':5, 'Yid':2},
                     {'name':'Armorshield', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':5, 'Yid':3},
                     {'name':'Tripleinvocation', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':5, 'Yid':4},
                     {'name':'Wraith', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':6, 'Yid':1},
                     {'name':'Giantgrowth', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':6, 'Yid':2},
                     {'name':'Shock', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':6, 'Yid':3},
                     {'name':'Poison', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':7, 'Yid':1},
                     {'name':'Vampirelady', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':7, 'Yid':2},
                     {'name':'DarkAngel', 'Attack':0, 'Health':0, 'Range':0, 'Speed':10, 'Xid':7, 'Yid':3}]


    def GetCard1(self, x, y):
        for card in self.cardsInfo1:
            Left = self.XSTEP * (card['Xid'] - 1)
            Right = self.XSTEP * card['Xid']
            Top = self.YSTEP * (card['Yid'] - 1)
            Down = self.YSTEP * card['Yid']
            if x > Left and x < Right and y > Top and y < Down:
                return card
           
        return None

    def GetCard2(self, x, y):
        for card in self.cardsInfo2:
            Left = self.XSTEP * (card['Xid'] - 1)
            Right = self.XSTEP * card['Xid']
            Top = self.YSTEP * (card['Yid'] - 1)
            Down = self.YSTEP * card['Yid']
            if x > Left and x < Right and y > Top and y < Down:
                return card
           
        return None        