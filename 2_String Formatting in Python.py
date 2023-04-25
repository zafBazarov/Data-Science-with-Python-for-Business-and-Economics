#####################
## String Formatting in Python
####################

# Old Style:
number = 2.7465543867
number2 = 13

print(type(number))

name = "Bob"

print('Hello, %s.' % name) # access to variables through the % operator and %s for strings

print('This is a number, %d.' % number) # %d for integers

print('This is a number, %f.' % number) # %f for floats

print('This is a number, %.2f.' % number) # %f for floats

print('This is a number, %f and my name is %s' % (number, name))

print('This is a number, %f and my name is %s. I am %d years old. Years in float: %f' % (number, name, number2, number2))

##########################################################################

# New Style

number = 2.7465543867
number2= 13
name = "Bob"


print('Hello, {}.'.format(name))

print('Hello, {name}.'.format(name=name)) # access to variables through the % operator

print('This is a number,{:d}.'.format(int(number))) # %d for integers

print('This is a number, {:f}.'.format(number))

print('This is a number, {:.2f}.'.format(number))

print('This is a number, {:-10.2f}.'.format(number))

print('This is a number, {:-1.2f}.'.format(number))


first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"

print(("Hello, {first_name} {last_name}. You are {age}. " +
       "You are a {profession}. You were a member of {affiliation}.").format(first_name=first_name,
                                                                             last_name=last_name,
                                                                             age=age,
                                                                             profession=profession,
                                                                             affiliation=affiliation))


############################################################################
# Literal String Interpolation

number = 2.7465543867
number2= 13
name = "Bob"

print(f'Hello, {name}.')

print(f'This is a number, {number2:f}.')

print(f'This is a number, {number2:d}.')

print(f'This is a number, {number:-10f}.')

print(f'This is a number, {number}.')

print(f'This is a number, {number:.2f}.')

print(f'This is a number, {number:-10.2f}.')

first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"

print(f"Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}.")


first_name = "Eric", "John"
last_name = "Idle", "Abraham"
age = 74, 82
profession = "comedian", "waitress"
affiliation = "Monty Python", "Intermediate"

print(f"Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}.")
#############################################################################

# String functions

print("My mom said, \"You're special.\"")      # \"\" helps to add symhols without problem

some_str = "Please replace something. Please replace something 2. Please replace something 3."

some_str = some_str.replace("replace", "delete") # .replace
print(some_str)

some_str = " How does The strip() Function work? "

print(some_str)

print(some_str.strip()) # strip() removes beginning nand ending blanks


some_str = some_str.strip()
print(some_str)

# .find() command
print(some_str.find("W")) # -1 -> Value not found

print(some_str.find("w")) # 2 -> Match is in the third position.

print("Strip() is applied first. After that, everything is written in lower case:", some_str.strip().lower())

print(some_str.lower().find("w")) # 2

# .lower() command
variant_1="My name is Zafarali"

print("My name is Zafarali".lower()) # makes all capital letters small

# .upper() command
print("My name is Zafarali".upper()) # makes all small letters into capital
##

option_1 = "My name is Zafarali"

print("option 1", option_1.lower())

print("option 2", "My name is Zafarali".lower())

###############################
## Exercises on this topic

#Strings

# 1. Check your understanding of strings by answering the following questions:
# 1.1 Which are the two possible ways to declare a string in Python?
x1 = "string"
print(type(str(x1)))        # just use a str command

#   1.2. How can integers and floats be declared as strings? Give an example!
# with str() command
x2 = 3
print(type( str(x2)))

# or with ""

x3="3"
print(type(x3))

#2. Print these sequence combinations:

#    2.1. One doesn’t simply print this sentence in Python.

#    1. One doesn't simply print this sentence in Python.
print("One doesn't simply print this sentence in Python.")

# Alternatively, but complicated:
print('One doesn\'t simply print this sentence in Python.')

#    2. My mom said, "You're special."
print("My mom said, \"You're special.\"")

#    3. She said, "Don’t smoke!" # anmerkung tutor: ' in dont fixen auf github

print("She said, \"Don\'t smoke!\"")

#3. What are the Python print-outputs? Look for flaws in these inputs and find a solution in case of a flaw. Try doing it yourself before printing in Python.

#    1. "Hello, " + "Nick."
print("Hello, " + "Nick.")

#    2. 'H' + 'e' + 'l' + 'l' + 'o'

print('H' + 'e' + 'l' + 'l' + 'o')

#    3. "This costs " + 7 + " bucks."

print("This costs " + "7" + ' bucks.')

#    4. "This costs " + 7 + 4 + " dollars." (Note: This should print 11 dollars at the end.)
print("This costs " + str(7 + 4) + " dollars.")

## alternative

a=7
b=4
print(f"This costs {a+b} dollars.")

#4. Google how the split function works and explain it!
# With the split function we can split a string into a list according to specified characters

#5. Split the following sentences by the mentioned character in parentheses:
# 1. "16.07.2018 10:00 Uhr MESZ" (Space)

print("16.07.2018 10:00 Uhr MESZ".split())

#    2. "Deutschland,Hessen,35394,Gießen,Licher Straße 74" (Comma)
print("Deutschland,Hessen,35394,Gießen,Licher Straße 74".split(","))

#6. Try writing the output on your own and compare your result to Python’s output:

#    1. print("My name is " + "Matt, Julia, Zara".split(',')[2] + ".")
print("My name is " + "Matt, Julia, Zara".split(',')[2] + ".")

print("My name is " + "Matt, Julia, Zara".split(',')[1] + ".")

print("My name is " + "Matt, Julia, Zara".split(',')[0] + ".")

#    2. print("Matt, Julia, and Zara".split(',')[:])

print("Matt, Julia, and Zara".split(',')[:])

print("I am from " + "Uzbekistan, Germany, USA".split('.')[1] + ".")
