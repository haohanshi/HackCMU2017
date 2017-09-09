class Globals(object):
    stations = [None, "Café", "Restroom", "Vending Mahcine", "Printer"]
    preferences = [None, "Indoor", "Handicapped", "Elevator"]

    def __init__(self, en_Pref, en_Station):
        self.en_Pref = en_Pref
        self.en_Station = en_Station
