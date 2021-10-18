


def checkDate(BirthYear, DeathYear):
    if(BirthYear < DeathYear):
        return True
    else:
        return False


def CheckMarriage(HusBirt, WifBirt, MarrDay):
    HusAge = MarrDay - HusBirt
    WifAge = MarrDay - WifBirt
    if(HusAge <= 14 or WifAge <= 14):
        return False
    else:
        return True