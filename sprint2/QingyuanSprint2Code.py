
def PrintName(inputNameList):
    output = []
    for i in range(len(inputNameList)):
        if(inputNameList[i] == "M"):
            output.append(inputNameList[i+1])
        i += 1
    return output




def CheckMarr(Names):
    if len(Names) == len(set(Names)):
        return False
    else:
        return True
