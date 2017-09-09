class GlobalVal(object):
    stations = {"Cafe":0, "Restroom":0, "Vending":0, "Printer":0}
    preferences = {"Indoor":0, "Handicapped":0, "Stair":0}

    def __init__(self, en_Pref = 0, en_Station = 0):
        self.en_Pref = en_Pref
        self.en_Station = en_Station

    def En_Pref(self):
        return self.en_Pref

    def En_Station(self):
        return self.en_Station


class Preferences(GlobalVal):
    def __init__(self, indoor = 0, handicapped = 0, stair = 0):
        super().__init__()
        if self.en_Pref:
            self.indoor = indoor
            self.handicapped = handicapped
            self.stair = stair

    def Indoor(self):
        return self.indoor

    def Handicapped(self):
        return self.handicapped

    def Stair(self):
        return self.stair