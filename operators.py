"""
 Operations to practice / mathetmatical
 arithmatic operators (+,-,*/) / 1>10 
 Comparison operators (>,<,>=,<=)
 Assign operators (AND, OR,NOT,)
 Identity Operators (is,isnot)
 Membership operators(in , notin )
 bitwise operators( & )
"""

 #Aritmatic Operators 

a = 5
b = 10
c= a+b 
print(c)
c= a*b 
print(c)
c= a/b 
print(c)

print(5 +3.5)
print(5 - 1)

# Comparison operators
x=10
y=20
c=x>y
print(c) ## output is False
c=x<y
print(c)
c= x<=y
print(c)
c=x>y
print(c)
c= x=y
print(c)
c= x==y
print(c)
c= x!=y  ## check with Sharmila
print(c)
c= x>=y
print(c)

print(6 >= 7)
print(6 != 7)

##### Logical Oprators #####

# The outcome is a True or False

x = 4
y = 6

print((x > y and y < x)) #false and false is false
print((x > y or y < x)) ## false or false is false
print((x < y and y < x)) ## true and false is false
print((x < y and y > x)) # true and true is true 

if ((x < y and y > x)):
 print("this is true")
else :("this is false")

if ((x < y or y > x)):
 print("this is true")
else :
  print("this is false")

if ((x > y or y > x)): # false or true is true 
 print("this is true")
else :
  print("this is false")

if ((x > y or y < x)): # false or false is false 
 print("this is true")
else :
  print("this is false")

#elif

if (x > y ): 
 print("x is greater")
elif (x<y) :
 print("x is greater than Y")
else :
  print("something is wrong")

#if not

if not (x > y ): 
 print("x is greater")
elif (x<y) :
 print("x is greater than Y")
else :
  print("something is wrong")


## Identity operators 
# two variable refers to same object in memory 

a =[1,2]
b= a 
c= [1,2]

print("a is b")  # true
print("a is c") # false
print("a is not c") # true 
print(1000 is 1000)

##membership operators (in , not in) test if a value exist in list / sequence

team = [1,2,3,4,5]

print( 4 in team)
print( 5 in team)
print( 1 not in team)

# bitwise Operators (&, |, ~, ^, <<, >> )

h = 5 # binary :101
j = 3 # binary : 011
print(h &j) # output is 1 as last bit for both variables is 1
print(h or j)
print(h < j)
print(h >> j)

# assignmet operators 
a = 10     # =   Assignment, sets a to 10
a += 5     # +=  Addition assignment, a = a + 5; now a is 15
a -= 3     # -=  Subtraction assignment, a = a - 3; now a is 12
a *= 2     # *=  Multiplication assignment, a = a * 2; now a is 24
a /= 4     # /=  Division assignment, a = a / 4; now a is 6.0
a %= 5     # %=  Modulus assignment, a = a % 5; now a is 1.0

print(a)




