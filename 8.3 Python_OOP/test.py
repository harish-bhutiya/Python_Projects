# Class in python oop

class Myclass:
    class_variable = "I am a Class variable."

def __init(self,attribute1,attribute2):
    self.attribute1 = attribute1
    self.attributr2 = attribute2

    def instant_method(self):
        return "I am a instance method"
    
    object = Myclass("Value1","Value2")

    object.attribute1 #accesing instance attribute
    Myclass.class_variable #access class attribute

    object.instance.method() #calling instance method
