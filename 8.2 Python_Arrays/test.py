import numpy as np

myarray = np.array([1,2,3,4,5,6])
print(myarray)

# Addition wise array operation

arra1 = np.array([1,2,3,4])
arra2 = np.array([5,6,7,8])
result = arra1 + arra2
print(result)

myarray = np.array([1,2,3,4,5,6])
element1 = myarray[0]
sliced = myarray[1:4]

print(element1)
print(sliced)

#Array with sort method

myarray = [1,2,3,4,5]
sorted = np.sort(myarray) #this will sort an array
mean = np.mean(myarray) #this will calcualate mean 

print(sorted)
print(mean)

# Array with for loop

myarray = np.array([1,2,3,4,5])
for element in myarray:
    print(element)