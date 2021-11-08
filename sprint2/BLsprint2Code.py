from ged4py import date
from prettytable import PrettyTable
from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from ged4py import GedcomReader
from ged4py.date import DateValueVisitor


class DateFormatter(DateValueVisitor):
    """Visitor class that produces string representation of dates.
    """
    def visitSimple(self, date):
        return f"{date.date}"

    def visitPeriod(self, date):
        return f"from {date.date1} to {date.date2}"

    def visitFrom(self, date):
        return f"from {date.date}"

    def visitTo(self, date):
        return f"to {date.date}"

    def visitRange(self, date):
        return f"between {date.date1} and {date.date2}"

    def visitBefore(self, date):
        return f"before {date.date}"

    def visitAfter(self, date):
        return f"after {date.date}"

    def visitAbout(self, date):
        return f"about {date.date}"

    def visitCalculated(self, date):
        return f"calculated {date.date}"

    def visitEstimated(self, date):
        return f"estimated {date.date}"

    def visitInterpreted(self, date):
        return f"interpreted {date.date} ({date.phrase})"

    def visitPhrase(self, date):
        return f"({date.phrase})"

file =open("./Qingyuan Liu_My-Family-20-Sep-2021-161439433.ged")

file_path = 'Qingyuan Liu_My-Family-20-Sep-2021-161439433.ged'
gedcom_parser = Parser()
gedcom_parser.parse_file(file_path)
root_child_elements = gedcom_parser.get_root_child_elements()
test1 = gedcom_parser.get_element_dictionary()
Id= []

for key in test1:
    Id.append(key)

name = []
gender = []
birthday = []
family = []
for element in root_child_elements:


    if isinstance(element, IndividualElement):

            (first, last) = element.get_name()
            Id.append((element.get_census))
            gender.append(element.get_gender())
            name.append(((first+" "+last)))
            birthday.append(element.get_birth_data())

def printtable():

    table1 = PrettyTable()
    table1.field_names = ["ID", "Name", "gender", "birthday"]
    for i in range(len(name)):
        table1.add_row([Id[i],name[i], gender[i], birthday[i]])
    print(table1)
    return table1

def storeBirthday():
    myBirthday = []
    for i in range(len(name)):
        #print (birthday[i])
        myBirthday.append(birthday[i])
    
    print(myBirthday)

    return True


mybirdata = []
with GedcomReader(file_path) as parser:
    for i, Indi in enumerate(parser.records0("INDI")):
        birth_date = Indi.sub_tag_value("BIRT/DATE")
        if birth_date:
            # print(type(birth_date))
            intyear = int(birth_date.date.year)
            # print(birth_date.date.year)

def checkParentsNotTooOld(fatherage, motherage):
    fatherflag = False
    motherflag = False
    if (fatherage < 1941):
        fatherflag = True
    if (motherage < 1961):
        motherflag = True

    if (motherflag == True or fatherflag == True):
        if(motherflag == True and fatherflag == True):
            print('both parents too old')
            return False
        if(motherflag == True):
            print('mother is too old')
            return False
        if(fatherflag == True):
            print('father is too old')
            return False    
    else:
        print('parents is not too old')
        return True

def checkMultipleBirths(people):
    # print(len(people))
    if (len(people) <= 5):
        print( 'there donot have more than 5 people born on same time')
        return True
    else:
        print('there have more than 5 people born on same time')
        return False