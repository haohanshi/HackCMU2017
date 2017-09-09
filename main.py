import setCP
from checkpoints import CPList
import instructions

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


class Preferences(object):
    def __init__(self, en_Pref = 0, indoor = 1, handicapped = 0, stair = 1):
        if en_Pref:
            self.indoor = indoor
            self.handicapped = handicapped
            self.stair = stair
        else:
            self.indoor = 1
            self.handicapped = 0
            self.stair = 1

    def Indoor(self):
        return self.indoor

    def Handicapped(self):
        return self.handicapped

    def Stair(self):
        return self.stair






def getHeuristics(Paths):
    for key in Paths:
        path = Paths[key]
        if path.legal:
            if path.Type == "Out":
                path.heuristic = 1 - Preference.outdoor * 0.5
            elif path.Type == "Corridor":
                path.heuristic = Preference.outdoor * 0.5 + 0.5
            elif path.Type == "Elevator":
                path.heuristic = 1 - Preference.elevator * 0.5
            elif path.Type == "Stair":
                path.heuristic = Preference.elevator * 0.5 + 0.5
        else:
            path.heuristic = 1000




def main(startPoint, endPoint, elevator, outdoor):
    Paths = setCP.listOfPaths(CPList)
    setCP.isLegal(Paths)
    # FOR TEST PURPOSE
    # for key in Paths:
    #     path = Paths[key]
    #     if path.legal:
    #         print(path.cp1.name)
    #         print(path.cp2.name)

    ##
    pref = Preferences(1, elevator, 0, outdoor)
    getHeuristics(Paths, pref)
    route = findRoute(Paths, startPoint, endPoint)
    result = instructions.generate_instr(route)
    print(result)
    return result


def solveRoute(Paths, startPoint, endPoint):
    visited = []
    def solve(Paths, cur_point):
        print(cur_point.number)
        # base cases
        if cur_point in visited:
            return False
        visited.append(cur_point)
        if cur_point == endPoint: 
            return True
        # recursive case
        for key in Paths:
            path = Paths[key]
            if path.cp1.name == cur_point.name and path.legal:
                print(path.cp2.number)
                if solve(Paths, path.cp2):
                    return True
        return False
    return visited if solve(Paths, startPoint) else None

def findRoute(Paths, startPoint, endPoint):

    route0 = []
    route0.append(Paths["WEH5312_to_WEH5300 wing"])
    route0.append(Paths["WEH5300 wing_to_entrance to DH"])
    route0.append(Paths["entrance to DH_to_level A entrance to DH"])
    route0.append(Paths["level A entrance to DH_to_west elevator on DH level A"])
    route0.append(Paths["west elevator on DH level A_to_west elevator on DH level 2"])
    route0.append(Paths["west elevator on DH level 2_to_DH2300 wing"])
    route0.append(Paths["DH2300 wing_to_DH2210"])


    route1 = []
    route1.append(Paths["WEH5312_to_WEH5300 wing"])
    route1.append(Paths["WEH5300 wing_to_entrance to DH"])
    route1.append(Paths["entrance to DH_to_level A entrance to DH"])
    route1.append(Paths["level A entrance to DH_to_west staircase on DH level A"])
    route1.append(Paths["west staircase on DH level A_to_west staircase on DH level 2"])
    route1.append(Paths["west staircase on DH level 2_to_DH2300 wing"])
    route1.append(Paths["DH2300 wing_to_DH2210"])

    route = []
    shortCPL = [startPoint, endPoint]
    startCP = setCP.newCP(shortCPL,0)
    endCP = setCP.newCP(shortCPL,1)
    if startPoint[0] == "WEH5312":
        return route0 if Pref.elevator else route1
        
    # elif startPoint[0][0:3] == "WEH":
    #     return route1
    return solveRoute(Paths, startCP, endCP)


    #HARDCODE FOR TEST ONLY
    # route1.append(Paths["WEH5312_to_WEH5300 wing"])
    # route1.append(Paths["WEH5300 wing_to_entrance to DH"])
    # route1.append(Paths["entrance to DH_to_level A entrance to DH"])
    # route1.append(Paths["level A entrance to DH_to_west staircase on DH level A"])
    # route1.append(Paths["west staircase on DH level A_to_west staircase on DH level 1"])
    # route1.append(Paths["west staircase on DH level 1_to_west staircase on DH level 2"])
    # route1.append(Paths["west staircase on DH level 2_to_DH2300 wing"])
    # route1.append(Paths["DH2300 wing_to_DH2210"])
