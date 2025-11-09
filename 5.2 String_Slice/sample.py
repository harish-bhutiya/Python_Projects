#string slice 

x = "I love bike riding"

print(x[2:9])

#So here above index start count from 0 so I count as 0 and last character will print 9=(9-1)=8  so it will print i not k


x = "I love bike riding"
# here first character means 0 index will not print rest all print
print(x[1:])

x = "I love bike riding"
print(x[:3])

x = "I love bike riding"
#negative slicing which start from end of the sentance 
print(x[-11:])

#String Modifying

x = "I love to travel"
#make it upprcase

print(x.upper())
print(x.lower())

x = "  I love London   "
#remove white spaces
print(x.strip())

#replace character in string

x = "I love America"
print(x.replace("America","India"))

#convert string into list 

x = "I love myself"
print(x.split(","))

#string concatenation

a = 'Hey'
b= 'There'
c = a + b
#it will add both string without space

print(c)

#for the space 

c = a + " " + b

print(c)

