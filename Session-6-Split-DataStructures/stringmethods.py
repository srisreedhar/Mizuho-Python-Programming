# collect info from the user and display

name= input("enter your name " ).upper()
office =input("enter your office ").title()
edu=input("enter your qualification ")

name=name.upper()
office=office.title()
edu=edu.lower()


print("""
Name is %s ,
you work in %s ,
you studied %s """%(name,office,edu))
