import setCP
from checkpoints import CPList
import instructions




def main(startPoint, endPoint):
    Paths = setCP.listOfPaths(CPList)
    setCP.isLegal(Paths)
    setCP.getHeuristics(Paths)
    route = findRoute(Paths, startPoint, endPoint)
    result = instructions.generate_instr(route)
    print(result)
    return result

def findRoute(Paths, startPoint, endPoint):
    route = []
    # for key in Paths:
    #     path = Paths.key
    #     if path.cp1.name == startPoint[0] and path.legal:

    #HARDCODE FOR TEST ONLY
    route.append(Paths["WEH5312_to_WEH_5300_Corridor"])
    route.append(Paths["WEH_5300_Corridor_to_WEH_DH_Entrance_WEHside"])
    route.append(Paths["WEH_DH_Entrance_WEHside_to_WEH_DH_Entrance_DHside"])
    route.append(Paths["WEH_DH_Entrance_DHside_to_DH_AF_WestStair"])
    route.append(Paths["DH_AF_WestStair_to_DH_1F_WestStair"])
    route.append(Paths["DH_1F_WestStair_to_DH_2F_WestStair"])
    route.append(Paths["DH_2F_WestStair_to_DH_2350_Corridor"])
    route.append(Paths["DH_2350_Corridor_to_DH2210"])
    return route

