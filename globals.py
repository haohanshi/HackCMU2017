class GlobalVal(object):
    stations = {"Cafe":0, "Restroom":0, "Vending":0, "Printer":0}
    preferences = {"Indoor":0, "Handicapped":0, "Elevator":0}

    def __init__(self, en_Pref = 0, en_Station = 0):
        self.en_Pref = en_Pref
        self.en_Station = en_Station