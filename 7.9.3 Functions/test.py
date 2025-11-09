# Function define by *def*

#Example 

def greet(name):
    print("Hello, " + name + "! How are you?")

greet('Harish')

#Anothet example


def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# If parameter has mentioned in the function then two value must present function otherwise it will show error

def my_function(fname,lname):
    print(fname+' '+lname)
my_function("Harish","Bhutiya")

# Arbitary arguments args
#When you do not have idea of numners arguments are just add *

def my_function(*kids):
    print("The youngest child is "+ kids[2])
    
my_function("Emil",'Tobias','Linus')

def my_function(child3,child2,child1):
    print("The youngest child is "+child3)
my_function(child3='Linus',child1='Emil',child2='Tobias')

# When do not know how many keys are there add **

def my_function(**kid):
    print("His last name is "+ kid["lname"])
my_function(fname="Tobias",lname="Refsnes")

#Defult Value

def my_function(country = "Norway"):
    print("I am from :" + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Peru")

#Loop throw

def my_function(food):
    for x in food:
        print(x)
fruits = ['Apple','Banana','Cherry']
my_function(fruits)

# Return values

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# Pass

def my_function():
    pass
my_function()

#Function Recursions

def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")

tri_recursion(6)