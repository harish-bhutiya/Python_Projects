import random

#Numner generation through import module
def random_number():
    print("Random Number:",random.randrange(1,100))
    print('Type of data:',type(random_number))

random_number()

#Data Convert from int to float
randomNumber = random.randrange(1,100)
print("Random Number:",randomNumber)

convert_data = float(randomNumber)
print("Converted data to float:",convert_data)
print(type(convert_data))

#Data Convert float to complex

convert_to_complex = complex(convert_data)
print("Converted data to complex:", convert_to_complex)
print(type(convert_to_complex))

x = "Hello"
print(x[2:4])

y = "hello"
print(y[::-1])