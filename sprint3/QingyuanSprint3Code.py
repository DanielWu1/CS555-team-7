def findAge(Birthday):
    AgeList = []
    for i in range(len(Birthday)):
        age = 2021 - Birthday[i]
        AgeList.append(age)
        i = i+1
    return AgeList


def sortByAge(ageList):
    return ageList.sort()