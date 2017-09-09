'''
Generate instructions for users
input: a list of small paths
*path object attributes: cp1,cp2,type
output: a list of strings(instructions)
'''
import json

def path_to_instr(path):
    #input object, output string
    #type:corridor,stair,elevator,road,entrance
    action=''
    if path.cat=='Corridor' or path.cat=='Road':
        action='Walk down the'+path.cp1.name
    elif path.cat=='Stair':
        destination='Level'+str(path.cp2.level)
        action='Climb up the stairs to'+destination
    elif path.cat=='Elevator':
        destination='Level'+str(path.cp2.level)
        action='Take the elevator to'+destination
    elif path.cat=='Entrance':
        action='Go through the'+path.cp1.name
    willsee='Then you will see'+ path.cp2.name
    instr = action + '\n' + willsee
    return instr

def generate_instr(pathlist):
    all_instr={'description':[], 'cpList':[]}
    for path in pathlist:
        instr=path_to_instr(path)
        all_instr['description'].append(instr)
        if (path.cp2.cat == "Stair" or path.cp2.cat == "Elevator"):
            cp_name = path.cp2.cat
        else:
            cp_name = path.cp2.name
        all_instr['cpList'].append(cp_name)

    return all_instr
        
