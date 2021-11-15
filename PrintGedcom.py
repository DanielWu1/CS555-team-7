from prettytable import PrettyTable
from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from ged4py import GedcomReader

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


table1 = PrettyTable()
table1.field_names = ["ID", "Name", "gender", "birthday"]
for i in range(len(name)):
    table1.add_row([Id[i],name[i], gender[i], birthday[i]])

#print(table1)

Married = []
HusbandName = []
HusbandID = []
wifeName = []
wifeID = []
with GedcomReader(file_path) as parser:
    # iterate over each FAM record in a file
    for i, fam in enumerate(parser.records0("FAM")):

        # Get records for spouses, FAM record contains pointers to INDI
        # records but sub_tag knows how to follow the pointers and return
        # the referenced records instead.
        husband, wife = fam.sub_tag("HUSB"), fam.sub_tag("WIFE")
        if husband:
            HusbandName.append(husband.name.format())
        if wife:
            wifeName.append(wife.name.format())

        # Get _value_ of the MARR/DATE tag
        marr_date = fam.sub_tag_value("MARR/DATE")
        if marr_date:
            print(type(marr_date))
            Married.append(marr_date)

        husbandid, wifeId = fam.sub_tag("HUSB"), fam.sub_tag("WIFE")
        if husbandid:
            HusbandID.append(husbandid.xref_id)
        if wifeId:
            wifeID.append(wifeId.xref_id)


table2 = PrettyTable()
table2.field_names = ["Married", "HusbandID", "HusbandName", "WifeID", "WifeName"]
for i in range(len(Married)):
    table2.add_row([Married[i],HusbandID[i], HusbandName[i], wifeID[i], wifeName[i]])

a = Married[0]
print(type(a.date))
if(1994 > a.date.year):
    print("Yes")
else:
    print("no")

#print(table1)
#print(table2)