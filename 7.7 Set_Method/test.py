#Set Method

numbers = {1,2,3}

# you can write as below

real_numbers = set({3,4,2})

print(numbers)
print(real_numbers)

#Methods in set Methods

# add() - adds an element to the set
# remove() - Removes an element from the set; raises an error if the element is not in the set.
# discard()  - remove element from the set if it exits; does not raises an error if the element is not in the set
# clear() - removes all elements from the set
# copy() - creates a shallow copy of the set
# pop() - remove and returns an arbitrary element from the the set.
# len() - returns the numbers of the element in the set.

# *** Set Operation ***

# Union method - it is combine both set the and returns same value once only

set1 = {1,2,3}
set2 = {3,4,5}

set3 = set1.union(set2)

print(set3)

#intersection - it will reatin only same value from the both table.

set4 = set1.intersection(set2)
print (set4)

#difference 
#symmtrical difference