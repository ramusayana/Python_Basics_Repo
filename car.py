class Car:
    
    def __init__(self,make,model,year,color):
        
        # init => python inbuilt function
        
        # also called constructor => is a unique function that gets called automatically when an object is created for a class
        
        # this only decide allocation of memory for an object
        
        # the main purpose of constructor is to initialize or assign values to the data members of the class
        
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
    def drive(self):
        print("This"+ self.model + "currently driving")
        
    def stop(self):
        print("This"+ self.model + "currently stopped")
        
            
            
        
        