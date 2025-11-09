#Tuple have limited built-in methods due to their immutability.

# count() : Return the numbers of times a specified value appears in the tuple.
# index(): Return the index of the first occurrence of a specified value in the tuple.

#count()

numbers = 1,2,2,3,3,3,3,4,5,6,7,9,
print(numbers.count(3))

def coordinates():
    return(3,4)

x,y = coordinates()

print(x,y)