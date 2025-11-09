numbers = (1,2,3)
print(numbers[1])

# You can iterate through the elements of a tuple using a #for Loop.

for number in numbers:
 print(number)

if 2 in numbers:
 print("Yes 2 is avaliable")
else:
 print("No 2 is not avaliable")

# You can concanate 2 tuples 

children_age = (1,2)
parent_ages = (23,56)

result = (children_age + parent_ages)
print(result)