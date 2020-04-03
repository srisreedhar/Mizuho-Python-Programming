# Interview program

name=input("Enter your Name ")
dob=input("Enter your Year of birth ")
edu=input("Enter your Degree ")
curent_year=2020
details=[]

details.append(dob)
dob=int(dob)
yr=curent_year-dob
details.append(name)
details.append(dob)
details.append(edu)

print("""
Hi,
Your name is %s,
You're %s years old and you've studied %s"""%(name,curent_year-dob,edu))


print("the list is ",details)
