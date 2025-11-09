#Membership Operator

# Membership operators are used to test if a value is present in a sequence.

# in 
# not in

x = [1,2,3,4]

is_in = 3 in x
print(is_in)

is_not_in = 5 not in x
print(is_not_in)

# Identity Operator

# Identity operators are used to compare the memory locations of two objecs.

# is: True if two variables reference the same object
# is no: True if two variables reference different objects

a = [1,2,3]
b = a #Both a and b reference the same list object

is_same_object = a is b #true