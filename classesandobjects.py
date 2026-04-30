# class => set of functions and variables(blueprint for creating objects)

# object => instance of class with properties and behaviours

# class classname:

class Chennai:
    
    name = " " # empty string variable
    
    juice = " "
    
    # def party():
    #     print("Lets Party!")
    # party()    

    # if you are calling "Party" func. inside the class then no need of self in argment but if you call party method outside the class then we need the following "self" this self denotes the future object

    def party(self):
        print("Lets Party!")
    
        
    # self => is a keyword to denote current object
    
    def beach(self):
        print("Lets enjoy!")
               
      
        
# going to create object

# objname = classname()

city = Chennai()
capital = Chennai()

city.beach()
capital.party()
    
    
city.name = "Python" # registering the variable name

print(city.name) # activating the name inside the class Chennai

capital.name = "Tamilnadu"
print(capital.name)

city.juice = "Yes"
capital.juice = "No"

print("Juice:",city.juice)
print("Juice:",capital.juice)



    


