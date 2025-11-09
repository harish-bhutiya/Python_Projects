#Assign type of data
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#Global and local variable

#Here x is in globle scope

x = "Great"
def myfunc():
    #Here x is in local scope
    x = "Awesome"
    print("Python is " + x)

myfunc()