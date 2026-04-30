## if, else , elif 

age = 20 

if(age>18) :
    print("you can vote") ## indentation is present means space before print and we use : here and also for for condition etcc.

if(age>22) :
    print("you can vote")
else :
    print("wait until 22")



if(age>20) :
    print("you can vote")
elif (age ==18): ## wheter the age is equal to 20 or not
    print("you may apply for voter ID")
else :
    print("wait until you reach 20")
    

## logical keywords###
# 
if(age>20) and (age<20) :##for "and" both conditions true other wise else / both should be true to be true
    print("you're eligible for vote") 
else :
    print("you're not eligible")



if(age==20) and (age<20) :##for "and" both conditions true other wise else / both should be true to be true
    print("you're eligible for vote") 
else :
    print("you're not eligible")


if(age==20) or  (age<20) :##for "and" both conditions true other wise else / both should be true to be true
    print("you're eligible for vote") 
else :
    print("you're not eligible")    


#####  loops 
# for loop
# while loop and no do while loop in python 

##it can be written one time and work many times until the condition is satisfied it will run

mobiles = ["iphone" , " andriod" , 'ipad' , "samsung"]

#print(mobiles)   ##to print in vertical we can use for loop

for letter in mobiles: 
    print(letter) ## we need to call the iterator "letter"

for i in "hi , welcome" :
    print(i)    
###################################

name = "python"

for leters in name :
    print(leters)

## inside the for loop we can have the if else condition 
## in  python no switch case and do while 
"""
switch case can achieved by using if else condition or dictionary
"""

for i in "hi,welcome" :
    if i==',' :
        print(',present ' )   # break and continue / once its found it will break or else it will continue
         
    else :
        print(', is not present')  ## it will run each value it holds of string "hi , welcome"  / if we put break here it will break as index first value "h"
        break

for i in "hi,welcome" :
    if i==',' :
        print(',present ' )   # break and continue / once its found it will break or else it will continue
          ## even it found comma it will run until the last value 
    else :
        print(', is not present')  ## it will run each value it holds of string "hi , welcome"  / if we put break here it will break as index first value "h"
        continue

##### range key word in for loop to access 

for number in range(4):
    print(number)

##########################
for number in range(8,12):
    print(number)    


for number in range(10, 20 ,5):  ## start stop and increment value which is 5 
    print(number)    

for number in range(10,30 ,4 ):   ## 10,14,18,22,26 output 
    print(number)        
    
    
for number in range(4):
    print(number)
else : 
    print("you're always right")

 ###### nesting of for loop ####

for number in range(4):
    print(number)
    for i in range(2):
        print(i)
    else :
        print("Im always right")


##################


"""
while means executes as long as condition is true other wise it will break
"""

x = 1

while x < 5 :
    print(x)
    x+= 1
else : 
    print("over")   ### 1234over / lambda function and user input (Home work) give some value user 


name = input("type your name : ") ## method for userinputs the user like username , password ,PIN
print("my name is :" + name)


numberone = int(input("Enter number one : ")) ### type casting or type conversion do some home work user input 
numbertwo = int(input("Enter number two : "))
print(numberone + numbertwo )


        





