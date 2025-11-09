# lamdas argument: expression

# Example

number = lambda x, y: x+y
print(number(3,6))

# lamdas use in map function

number = [1,2,3,4,5,6]
squres = list(map(lambda x: x**2,number))
print(squres)

#lamdas use in function

def number(n):
    return lambda a: a*n
check = number(33)
another = number(5)
print(check(2))
print(another(5))

def multi(s):
    return lambda a: a+s
sum = multi(5)
minus = multi(2)
print(sum(3))
print(minus(4))