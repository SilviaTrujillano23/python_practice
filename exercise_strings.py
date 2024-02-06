## Create a program that asks first,middle and last name and prints the initials
firstName = input("Enter your first name: ")
middleName = input("Enter your middle name: ")
lastName = input("Enter your last name: ")
print("Your initials are: ",firstName[0],middleName[0],lastName[0])

##create a program that prints countrycode,productcode and batch number
lotNumber = "037-00901-00027"
print("countrycode",lotNumber[:3])
print("productcode",lotNumber[4:9])
print("batch number",lotNumber[-5:])
print("BATCH NUMBER,alternative solution",lotNumber[10:])





