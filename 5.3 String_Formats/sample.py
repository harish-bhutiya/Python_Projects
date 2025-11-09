# age = 36
# my_age = "I am  " + age +"years old."

#it will give you error
#print(my_age)

#Correct way to format with format function {}

age = 36 
my_age ="I am {} years old."

print(my_age.format(age))

#multiple placeholders

quantity = 10
items = 20
price = 50.05

myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,items,price))

#format by using index

myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity,items,price))

# escape character with using special character \

#Below example will give you error
# full_name = "My name is :"Harish""
#print(full_name)

#correct way to write with eacape character

myName = "My name is:\"Harish\""
print(myName)

#example with other escape character
myName = "My name is:\'Harish'"
print(myName)

#example with other escape character
myName = "My name is:\nHarish"
print(myName)

#example with other escape character
myName = "My name is:\rKarish"
print(myName)

#example with other escape character
myName = "My name is:\tHarish"
print(myName)

#example with other escape character
myName = "My name is:\bHarish"
print(myName)

#example with other escape character
myName = "My name is:\fHarish"
print(myName)

#example with other escape character
myName = "My name is:\000Harish"
print(myName)

