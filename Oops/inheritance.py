# deriving new class from a existing class

# or

# deriving a child class from the parent class

# inheritance => code reusability

# 4 types => single, hierarchical ,multiple and multilevel

#single inheritance 

# one child class derived from one parent class

class Animal:
    
    alive = True
    
    def eat(self):
        print("this animal is eating")
        
    def sleep(self):
        print("this animal is sleeping")
        
class Rabbit(Animal):
    
    def run(self):
        print("This rabbit is running")
        
rab = Rabbit()
ani = Animal()

rab.run()
rab.eat()
rab.sleep()
#ani.run()

print(rab.alive)

# multilevel inheritance

# child class derived from another child class

class Organism:
    
    alive = True
    
class Animal(Organism):
    
    def eat(self):
        print("this animal is eating")

class Dog(Animal):
    
    def bark(self):
        print("This animal is barking")
        
dog = Dog()

dog.eat() #inherited from animal class

print(dog.alive) # inherited from organism class

dog.bark() # defines in dog class

# multiple inheritance => when a child class derived from one or more parent classes 


class Prey:
    
    def flee(self):
        print("This animal flees")
        
class Predator:
     
    def hunts(self):
        print("This animal is hunting")
        
class Rabbit(Prey):
    
    pass # place holder for future codes 

class Hawk(Predator):
    
    pass

class Fish(Prey,Predator):
    
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunts()
fish.flee()
fish.hunts()
#rabbit.hunts()
#hawk.flee()

#hierarchical 

# multiple child class derived from single parent class

class Animal:
    
    alive = True
    
    def eat(self):
        print("this animal is eating")
        
    def sleep(self):
        print("this animal is sleeping")

class Rabbit(Animal):
    
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    
    pass

class Dog(Animal):
    
    #pass
    
    def jump(self):
        print("This animal is jumping")

rab = Rabbit()
fish = Fish()
dog = Dog()

rab.eat()
fish.eat()
dog.eat()

rab.run()

#dog.run()




    

        
    