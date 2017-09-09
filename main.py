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


def solveRoute(Paths, startPoint, endPoint):
    visited = []
    def solve(Paths, cur_point):
        # base cases
        if cur_point in visited: return False
        visited.append(cur_point)
        if cur_point == endPoint: return True
        # recursive case
        for key in Paths:
            path = Paths[key]
            if path.cp1.name == cur_point.name and path.legal:
                if solve(Paths, path.cp2.name): return True
        visited.pop(visited.index(cur_point))
        return False
    return visited if solve(Paths, startPoint) else None

def findRoute(Paths, startPoint, endPoint):

    route0 = []
    route0.append(Paths["WEH5312_to_WEH5300 wing"])
    route0.append(Paths["WEH5300 wing_to_entrance to DH"])
    route0.append(Paths["entrance to DH_to_level A entrance to DH"])
    route0.append(Paths["level A entrance to DH_to_west staircase on DH level A"])
    route0.append(Paths["west staircase on DH level A_to_west staircase on DH level 1"])
    route0.append(Paths["west staircase on DH level 1_to_west staircase on DH level 2"])
    route0.append(Paths["west staircase on DH level 2_to_DH2300 wing"])
    route0.append(Paths["DH2300 wing_to_DH2210"])

    route = []
    shortCPL = [startPoint, endPoint]
    startCP = setCP.newCP(shortCPL,0)
    endCP = setCP.newCP(shortCPL,1)
    if startPoint[0] == "Randy Pausch Bridge":
        return route0
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
