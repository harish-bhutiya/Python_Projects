# Conditional Statement

#if else method

x = 13
y = 23

if x<5:
    print("X is greater than 5")
else:
    print("X is not less than 5")

#if elif method

if x>55:
    print("X is greater than 5")
elif x<5:
    print("X is less than 5")
else:
    print("None of the above")

# Nesting 

x = 10
y = 5

if x>5:
    if y>2:
        print("Both are true")
    else:
        print("One is true, the other is false")

else:
    print("None of the above")