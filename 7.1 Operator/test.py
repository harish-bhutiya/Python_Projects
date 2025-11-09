x = 8
y = 7

#Diffrenet Arithmetic operator

addition = x + y
substraction = x - y
multiplication = x * y
division = x / y
floor_division = x // y
modulus = x % y
exponent = x ** y

result =(addition, substraction, multiplication, division, modulus,floor_division, exponent)

for result in result:
     print(result)

# Comparison Operators, It will return with boolean value

is_equal = x==y
is_not_equal = x!=y
is_greater_than = x>y
is_less_than = x<y
is_less_equal = x <= y
is_greater_equal = x >= y

comparison_operator =(is_equal, is_not_equal, is_greater_than, is_less_than, is_less_equal,is_greater_equal)

for comparison_operator in comparison_operator:
    print(comparison_operator)

#Logical operator
#  and
#  or
#  not

p = True
q = False

result_and = p and q
result_or = p or q
result_not = not p

logical_operator = (result_and,result_or,result_not)

for logical_operator in logical_operator:
     print(logical_operator)

# Assignment Operator

# =: Assignment

# -=: Subtract and assign
# *=: Multiply and assign
# /=: Divide and assign
# //=: Floor divide and assign
# %=: Modulus and assign
# **=: Exponentiate and assign

# +=: Add and assign

x =10
x+=5
print(x) # so here x will count as 10 and +5 will add to them make it 15 

# +=: Add and assign

x =10
x-=5
print(x)

# /=: Divide and assign

x =10
x/=5
print(x)

# //=: Floor divide and assign

x =10
x//=5
print(x)

# %=: Modulus and assign
x =10
x%=5
print(x)

# **=: Exponentiate and assign
x =10
x**=5
print(x)