# Simple for loop

# for variable in sequence:
#     Block of code

#Example

fruits = ['apple','cherry','grapes']

for fruit in fruits:
    print(fruit)

#Range loop

for number in range(1,6):
    print(number)

#While Loop "Be careful it will end in infinite loop"

count = 0
while count <5:
    print(count)
    count +=1 #this is prevent from infinite loop. It will add +1 in base count until condition met.

for i in range(5):
    print(i)
else:
    print("Loops without issues")