##################
## Simple Data Types in Python
###

# String

print("Hello World!") # prints "Hello World!"

#################################
# Constant
NUMBER = "Zafarali"  # Constant Name contains String Zafarali
number = "Zafarali"  # Constant Name contains String Zafarali
ZAHL = 5             # Python reads as an integer this

print(number, ZAHL)
#########################

## Numbers

a = 5    #integer
b = "5"  #string
c = 5.5  #float

print(a+c)

print(c+c)

# type() function helps to identify a variable type.

print(type(a+c))

print(type(c+c))

print(int((c+c))) # int() function helps to turn a float data into integer

print(type(int((c+c))))

print(int(10.9)) # it is always rounded down when a float is converted into an integer!

print(int("294")+a)

##### Boolean
cart_1 = False
cart_2 = False


## and
print("and:", cart_1 and cart_2)

## or
print("or:", cart_1 or cart_2)

## not
print(not cart_1 and not cart_2)

## Comparison Operators

## <
print(3<2)

print(26<=26)

## == vs !=
print(1==2)   # == equal

print(1!=2)   # != not equal

## c = 1

print(5 == 5.0) #

print(5 is 5.0) # is= checks the value and data type

print(6 is 5.0)

# Strings

example_1 = "Hello! My name is Zafarali."
example_2 = 'Hello! My name is Zafarali.'

example_3 = "Zafarali said: 'My name is Zafarali.'"

print(example_3)

example_4 = "Zafarali said: \"My name is Zafarali.\" \nall said: 'Ok.'" # \n creates a new line
print(example_4)

example_5 = "Zafarali said: \"My name is Zafarali.\" \n\n\t all said: 'Ok.'" # \t creates a tab
print(example_5)

print(isinstance(example_3,str)) # str () converts the specified value into a string

### isinstance() checks the the type of specified object.

x= isinstance(5, int)
print(x)

y= isinstance(5.5, float)
print(y)

z=isinstance('a', str)
print(z)

######################
## Exercises on this topic

### Integers, Floats and Boolean Operators

#1. Can you add up both variable types? Create an example and check it!
a = 1
b = 1.5
c = a + b
print(c)

# 2. What data type should be the result of your calculation? Check it by using "print(type(VARIABLE))"!
# VARIABLE -> Whatever you have called your variable. The variable does not have to be called "VARIABLE.
print(type(c))

# 3. Explain boolean operators by using an example!

print(a > b) # False

print(a < b) # True

# 3. What is the difference between "==" and "="?

# A single equal sign “=” assigns a value (or variable) on the right side to a variable on the left side.
# A double equal sign “==” checks, whether the value on the left side is equal to the value on the right side.
