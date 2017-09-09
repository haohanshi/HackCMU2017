import setCP.py
import checkpoints.py

global CPList



def main(startPoint, endPoint):
    Paths = listOfPath(CPList)
    isLegal(Paths)
    getheuristics(Paths)
    route = findRoute(Paths, startPoint, endPoint)
    return route

def findRoute(Paths, startPoint, endPoint)
    for key in Paths:
        path = Paths.key
        if path.cp1.name == startPoint[0] and path.legal:

