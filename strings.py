# myString = "Hello, World!"
# print(type(myString))
# print(myString[-2])
# print(len(myString))

countrycode = "PE0067885"
##Print the first 2 characters of the string, NOTE:the second index is not included
print("Print first 2 characters:",countrycode[0:2])
print("Print first 2 characters, 0 is implicit:",countrycode[:2])

alternativeCountrycode = "10067885PE"
print("Only second last index of alternativeCountrycode:",alternativeCountrycode[-2])
print("Print the last 2 characters of the string:",alternativeCountrycode[-2:])
print("PRINT all numbers until -2, second last:",alternativeCountrycode[:-2])

##Print from -5 until the end of the string
print("Print last 5 digits",alternativeCountrycode[-5:])

##Convert number to string
str(22)
print("Hello user"+str(22))