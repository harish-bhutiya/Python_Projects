# *** Dictionaries ***

# Dictionaries are a fundamental data structure in python that allow you to store and retrieve data in key-value pairs. Each key in a dictionary is unique, and you can use it to access the corresponding value quickly.Dictionaries are also known as associative arrays or hash maps in other programming languages.

# You can create an empty dictionary or initialise it with values using curly braces {} or the dict() constructor.

# Empty dictionary

my_dict = {}

#Dictionary with initial values

person = {
    'name':'Harish',
    'age':30,
    'city': 'New York'
}

#How to get value from the key

name = person['name']
print(name)

# Get value from Get method

age = person.get('age')
print(age)

#assign default value in case of key is not found

age1 = person.get('age1', 'Unknown Key')
print(age1)

#Modifing dictionary

modified_age = person['age'] = 45
print(modified_age)

# Key Method keys()
print(person.keys())

# Values method values()
print(person.values)

#items methods items(), it will return key-value pairs
print(person.items())

#iterating the keys by looping

for key in person:
    print(key,person[key])

#Another Method 

for key, value in person.items():
    print(key,value)

#Copy method

mycopy = person.copy()
print(mycopy)

#Copy by dict method

mycopy1 = dict(person)
print(mycopy1)