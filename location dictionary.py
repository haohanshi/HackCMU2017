'''
Location Naming Standardization: Type_Building_Level_Number
'''
class location:
    def __init__(self,name,type,building,level,number):
        self.type=type
        self.building=building
        self.level=level
        self.number=number


    def Type(self):
        return self.type

    def Building(self):
        return self.building

    def Level(self):
        return self.Level

    def Number(self):
        return self.Number

'''
path: heuristic, legal status, stations(printer,eatery,toilet,vending)
'''
class stations:
    def __init__(self,have==True,printer,eatery,toilet,vending):
        self.have=have
        self.printer=printer
        self.eatery=eatery
        self.toilet=toilet
        self.vending=vending

    def Have(self):
        return self.have

    def Printer(self):
        return self.printer

    def Eatery(self):
        return self.eatery

    def Toilet(self):
        return self.toilet

    def Vending(self):
        return self.vending


class path:
    def __init__(self,heuristic,legal,haveStations==False,stations==None):
        self.heuristic=heuristic
        self.legal=legal
        self.haveStations
        self.stations=stations

    def Heuristic(self):
        return self.heuristic

    def Legal(self):
        return self.legal

    def Stations(self):
        return self.stations


'''
Generating Path Objects
e.g. WEH5312_to_DH2210
Input: location names
Output: path objects
'''
while 
Dir={}
def direction_list(loc1,loc2,heuristic,legal,stations,haveStations):
    path_name=loc1.Name+"_to_"+loc2.Name
    if haveStations:
        stations=stations(have,printer,eatery,toilet,vending)
    Dir[path_name]=path(heuristic,legal,haveStations,stations)
    
