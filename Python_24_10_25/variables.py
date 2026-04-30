a=10
b=20
c=a+b

print("The sum of a and b is:", c )


x = 10 
x = 10+1

age =10
age += 1 
age += 2
print("Your age is:", age)

age = "10"
# age+=1

# print("Your age is:", age)
print(type(age)) # to check the type of variable 



age = int("10") 
age += 1  
print("Your age is:", age) # this is type conversion or type casting from string to integer 

#concatenation of strings

first_name='Ram'
last_name = "Sharma"   

# print is a function to display output on the screen in pyhton 

full_name = first_name +  last_name

full_name = first_name +" "+ last_name

print("Full name is:", full_name)

## boolean

boys = True
print(boys) 

print ( "Is boys: " + str(boys)) 

height = 5.9 

print ("height is : " +str(height)+  "feet")  

print ("height is : ", height , " feet") ## type conversion from float to string

# variable assignment 

watch  = 500 
print("Watch price is:"+ str(watch))

print("Watch price is:" , str(watch))

print("Watch price is:"+ str(watch+ 100))

print (watch +100)

print ("watch +100")

print (watch - 100)

print (watch  * 100)

watch1 , name =  "Titan" , 500 
print( watch1)

x, y = 10, 20
print("x:", x)
print("y:", y)  

                          

def bat():{
    print("test")
}

bat()

f = float(10)
print(f)    
print(type(f))

i = int(10.9)
print(i)
print(type(i))


s = str(100)
print(s)
print(type(s))          

x = 10  
y = 20
z= x+y
print(TypeError(z))

def multiply(a,b):
    c = a * b 
    return c

multi_Result =multiply(3,4)
print(multi_Result)

x = None
print(x)

m = 20 
print(m)

"""
String primitive data type 
"""

name = " Ram  Sayana   " # array /string is a series of characters / array follows indexing method / string and list will act like array 
print(name[1])
print(name[5])
print(name[1:3])

# string will act like array (indexing method/ slicing will have a starting and ending point)

numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(numbers[::5]) # incrementation 
print(numbers[::2])
print(numbers[::3])
print(numbers[-15:-20]) # empty array / the bigger value should come first or else it will print empty
print(numbers[-20:-15]) # answer would be [ 1,2,3,4,5,] 

#reverse string / how to do that / no start value for reverse string as its advanced value 

print(name[::-1])
print(numbers[::-1])
print(name[::-3])
print(numbers[::-3])



# start:stop:step


"""
slicing , indexing , ranging (discussed)

negative ranging 
"""
print(len(name)) # no index here 

print(name.strip()) # will remove unwanted values front and back spaces

print(name.upper())
print(name.lower())

#print(name.replace(s))

# please replace charlie to charlie chaplin

joker = "charlie"

print(joker.replace("lie","liechaplin")) #it needs two arguments from what to what / replacing old to newvalues

print(joker.split("r"))

print(1>10)
print(10>1)

print(1==10) # condition to evaluate 1 ==10means evaluate 1 is equal to 10

print("Ram" in name)  # strictly checks the upper or lower case " in " is the boolean functionality 

print("Tanush" in name)

print(joker.split("r"))

# primitive data types completed

##########Recap what we discussed in Primitive Data types########

"""
String will act like an array or list

we have learnt 
1.indexing (by position starts with zero )
2.Slicing
3.Ranging
4. Negative ranging

In built functions below : 

Other methods include : 

Split method ( will split into two if you give a letter in a word )
Lower and Upper Method (if will change the lower or upper case in word)
Replace method ( this will replace with existing letters with another letter in print function)
lenght Method ( will give the (len) of the word)


"""

"""
Non-Primitive data types : 
List ([]) ## stores mulitiple values / acts like array and allow duplicate values / indexing , reverse of a list also same / Ranging will start from zero and slicing will start where we give the value in string or array 
Set ( { }) ( mainly used in gaming because it has no indexing value like : no start no end like no indexing no zero start etc.. it will give random when you click no specific order)
Tuple ( round bracket) ( exactly like list / this is static / adding or remove is not possible / it will index value )
Dictionary ( key pair : values / name: ram / key cant be changed but value can be changed)

Home work : 
find the difference of all above and real time examples

user defined 
"""
 
## LIST ###

group = [1,2,3,4,5]   

#create a list of food 

food = ["Biryani" , "Pulao" ,"Curry" , " Dessert" , 'Fruits']

print(type(food))

print(food)

print(len(food))

print(food[3])## indexing

print(food[::-1]) ## reverse a list 

print( food[1 :3])## ranging

food[2] = "sandwich"  ## it will replace the old value with new value through indexing method // this is over riding the exist value 

print(food)

## append##

food.append("cheese") ## adding a new value instead of over riding in the list 

print(food)
## remove##

food.remove("Biryani")

print(food)

food.pop() ## removes the last item of the list

print(food)

food.insert(2, "Kheer") ## inserts in between
print(food)

## empty the list or clear

food.clear()
print(food)

## empty string 
name = " " 
print(name)

food = ["Biryani" , "Pulao" ,"Curry" , " Dessert" , 'Fruits']

print(food)

## sorting ### either it can be ascending or descending 

number = [ 1,5,2,21,18, 30, 7 ]

print(number) 

number.sort() ## it will print ascending

print(number)

number.sort(reverse=True) ## prints descending order 

print(number)
number.sort()

print(food + number)

## 2D list ##

## list of two dimensional /  list of list or list inside a list 

drinks = [ "beer" , " whiskey" , "coffee" , "tea" , " mulled wine"]

dinner = ["pasta" , "steak " , "salad" , " grilled"]

desserts = [ "laddu" , " ice cream ", "cake" ]

full_meals = [ drinks , dinner, desserts]

print(full_meals)

print(full_meals[2]) ## this will be desserts list

print(full_meals[2][1]) ## finding values inside a list of list of desserts 

print("#####################################################")
## TUPLE ## Item is not able to assign

student = ("ram" ,40, 5.9, "male" )

print(student.count("ram"))

print(student.index(5.9)) ## we need give the value then it will tell index

## check add or remove

#student.append("Sam")

print(student)

#student.remove(40)

print(student)

drinks = [ "beer" , " whiskey" , "coffee" , "tea" , " mulled wine" , "beer" , "whiskey"]

print(drinks)

student = ("ram" ,40, 5.9, "male" , "male" , 'ram' )
print(student)

### Practical home work based on non-primitive data types
ai_test_suite = { 

     "test_cases" : ["prompts_test" , "accuracy_test" , "agent_test"],  ## list
     "llm" : ("chatGPT","Gemini", "Grok"), ## Tuple

     "tags" : ("smoke","regression","failed","manual","tree"),  ## set 
 
 "test_results":  ## dictioary 
 { 
     "test_pass" : 5 ,
     "test_fail" : "none",
     "test_error" : 1 ,


  } 

}


#### set ##### make a excel sheet topics and dates shows how much practice done and what are the topics covered

## set is unordered and no deplicates (output will not be in the same order and no indexing value )

llm = {"Gemini" , "chatgpt" , "co-pilot" ,"perplexity"}

# print(llm[1]) ## it is un indexed

print(llm)
print(llm)

llm.add("Grok")

print(llm)

llm.remove("Gemini")
print(llm)

#llm.clear()
print(llm)

prompt = {"chatgpt","co-pilot", "grok"}

print(prompt)

prompt.update(llm)

print(prompt)
print(llm)

llm.update(prompt)

print(llm)

llm.add("ai")

print(llm)


##dictionary is key constant and values can be changed 

data = { 
    "name" : "python",
    "age" : 10,
  }

print(data)

capitals = { 
"india" : "Delhi",
"UK" : "London" ,
"Nepal" : "katmandu",
"pakistan" : "islamabad",
"bangladesh" : "bhutan"
}

print(capitals)

#print(capitals("germany"))

print(capitals.get("germany"))

print(capitals.get("india"))

print(capitals.keys()) ## india , pakistan et c..

print(capitals.values()) ##  ['Delhi', 'London', 'katmandu', 'islamabad', 'bhutan']
print(capitals.items()) ## dict_items([('india', 'Delhi'), ('UK', 'London'), ('Nepal', 'katmandu'), ('pakistan', 'islamabad'), ('bangladesh', 'bhutan')])


capitals.update({"Switzerland" : "Berlin" })

print(capitals)

capitals.update({"Switzerland" : "Bern"})

print(capitals)

#capitals.pop({"Switzerland" : "Bern"})

print(capitals)

### in dictionary try with deleting "key" for pop


capitals.pop("Switzerland")

print(capitals)















