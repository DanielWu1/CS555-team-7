file_path = 'Qingyuan Liu_My-Family-20-Sep-2021-161439433.ged'
from ged4py import GedcomReader
with GedcomReader(file_path) as parser:
    # iterate over each INDI record in a file
    for i, indi in enumerate(parser.records0("INDI")):
        # Print a name (one of many possible representations)
        print(f"{i}: {indi.name.format()}")

        father = indi.father
        if father:
            print(f"    father: {father.name.format()}")

        mother = indi.mother
        if mother:
            print(f"    mother: {mother.name.format()}")

        # Get _value_ of the BIRT/DATE tag
        birth_date = indi.sub_tag_value("BIRT/DATE")
        if birth_date:
            print(f"    birth date: {birth_date}")

        # Get _value_ of the BIRT/PLAC tag
        birth_place = indi.sub_tag_value("BIRT/PLAC")
        if birth_place:
            print(f"    birth place: {birth_place}")



with GedcomReader(file_path) as parser:
    # iterate over each FAM record in a file
    for i, fam in enumerate(parser.records0("FAM")):

        print(f"{i}:")

        # Get records for spouses, FAM record contains pointers to INDI
        # records but sub_tag knows how to follow the pointers and return
        # the referenced records instead.
        husband, wife = fam.sub_tag("HUSB"), fam.sub_tag("WIFE")
        if husband:
            print(f"    husband: {husband.name.format()}")
        if wife:
            print(f"    wife: {wife.name.format()}")

        # Get _value_ of the MARR/DATE tag
        marr_date = fam.sub_tag_value("MARR/DATE")
        if marr_date:
            print(f"    marriage date: {marr_date}")

        # access all CHIL records, sub_tags method returns list (possibly empty)
        children = fam.sub_tags("CHIL")
        for child in children:
            # print name and date of birth
            print(f"    child: {child.name.format()}")
            birth_date = child.sub_tag_value("BIRT/DATE")
            if birth_date:
                print(f"        birth date: {birth_date}")


#Sprint2 work code
file_path = '../Qingyuan Liu_My-Family-20-Sep-2021-161439433.ged'
from ged4py import GedcomReader
with GedcomReader(file_path) as parser:
    # iterate over each INDI record in a file
    for i, indi in enumerate(parser.records0("INDI")):
        # Print a name (one of many possible representations)
        if (indi.sex == "M" ):{
            print("all male last name:", {indi.name.surname.format()})
        }


with GedcomReader(file_path) as parser:
    # iterate over each FAM record in a file
    for i, fam in enumerate(parser.records0("FAM")):
        # Get records for spouses, FAM record contains pointers to INDI
        # records but sub_tag knows how to follow the pointers and return
        # the referenced records instead.
        husband, wife, child = fam.sub_tag("HUSB"), fam.sub_tag("WIFE"), fam.sub_tag("CHIL")
        if (husband == child or wife ==child):{
            print("there is a marrage to descendants")
        }
        else:{
            print("there is no marrage to descendants")
        }



