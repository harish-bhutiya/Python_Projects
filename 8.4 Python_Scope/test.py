#Local scope variables

def myfunction():
    first_local = 10 # It is local variable because it is define under function name myfunction
    print(first_local)
    
myfunction()

def outerfunction():
    outer_variable = 20
    def inner_function():
        print(outer_variable)
    inner_function()
outerfunction()

#Global scope variable

global_variable = 30

def myfunction():
 print(global_variable)
myfunction()

#LEGO rule (Local,Encoded,Global,Built In)

x = 10
def f1():
   x = 50
   def innerfunction():
      x = 60
      print(x)
   innerfunction()
f1()
print(x)

