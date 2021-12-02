def findPartialDate(DateList):
    output = []
    for i in range (len(DateList)):
        if(len(DateList[i]) != 10):
            output.append(DateList[i])
            i = i + 1

    return output




def rejectDate(DateList):
    output = []
    for i in range (len(DateList)):
        Date = DateList[i]
        if(int(Date[6:10] ) >= 2100 or int(Date[6:10] ) <= 1900 ):
            output.append((DateList[i]))
            i = i +1
    return output


