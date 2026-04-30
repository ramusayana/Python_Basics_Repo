# many forms

# poly => many and morphism => behaviours

# same method/function/operators with the same name can be executed on many objects or class

class Android:
    
    def camera(self):
        
        print("I have 2 camera")
        
class Apple:
    
    def camera(self): # same method name and inheriting it is called method overriding
        
        print("I have 3 cameras")
        
andriod = Android()
ios =  Apple()

andriod.camera()
ios.camera()

# method overloading will be achieved through => *args and *kwargs

# runtime polymorphism => method overriding
# compile time polymorphism => method overloading => not in python like java and c++ but can be achieved through *args and *kwargs or decorator(functools) 

        
        