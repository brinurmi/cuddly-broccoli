#Intro to the Python coding language
#This file contains notes that I have taken while in 'The Complete Python Course' on Udemy
#Topics covered in this file:
    # Variables
    # Output
    # Math
    # Strings
    # String Formatting
    # User Input
    # AND & OR
    # Lists
    # Tuples
    # Sets
    # Dictionaries
    # Length & Sum
    # Joining a List


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                          Variables
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
age = 30
friend_age = 30 # use snake_case
PI = 3.14159 #constant
RADIANS_TO_DEGREES = 180/PI
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                         Output (Basic)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(age) #print variable
print(30) #print hard coded number
print('Hello World!')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                           Math
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
math_operations = 10 + 8 * 5 / 2 - 1 #python uses PEMDAS to solve
print(math_operations)

float_division = 12 / 3 # division will always produce a float number
print(float_division)

integer_division = 13 // 5 # use double // to remove everything after the decimal
print(integer_division)

remainder = 13 % 5 #find the remainder
print(remainder)

#use %2 to determine if numbers are even/odd
even_number = 10 % 2 #even = 0
odd_number = 13 % 2 #odd = 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                        Strings
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Can use either "" or ''
my_string = "Hello, world!"
my_string2 = 'Hello, world!'

string_with_quotes = "Hello, it's me."
string_with_quotes2 = 'He said, "That is awesome!" the other day.'
string_with_quotes3 = "He said, \"That is awesome!\" the other day" #can use \ to use "" inside a "" string, called escaping. 

multiline_string = """Hello, use three sets of quotation marks 
to create a string with miltiple lines.

My name is Bri. Thanks for coming to my TedTalk!
"""
print(multiline_string)

"""Can use the triple quotations as another form of comments (instead of using #).
You dont even have to assign this type of string to a variable. you can just use it."""

#adding strings together
name = "Bri"
greeting = "Hello, " + name
print(greeting)

age = 34
print("Your age is: " + age)# will produce an error. can only do this with strings!

#convert to string
age_string = "34" #option 1: just put double quotes
age_to_string = str(age) #option 2: cast the int to a string with str()
print("Your age is: "+age_to_string)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                       String Formatting
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"Your age is: {age}") #F string. can replace the print statement above with the int age variable.

name = "Jose"
greeting = f"How are you, {name}?" #F string variable
print(greeting)

#problem:
name = "Bob"
print(greeting) #still print out Jose because when greeting was generated, name = Jose and not bob.

#F-string method 2:
name = "Buster"
final_greeting = "How are you, {}?"
buster_greeting = final_greeting.format(name) #inserts the name inside the {} in final_greeting
print(buster_greeting) #prints "How are you, Buster?"

joe_greeting = final_greeting.format("Joe") #can also insert a string instead of a variable
print(joe_greeting) #Prints "How are you, Joe?"

#F-string method 3:
name = "Ken"
final_greeting = "How are you, {name}?" #will not replace name with "ken", an extra step is involved
ken_greeting = final_greeting.format(name="Ken") # must format name="ken"
print(ken_greeting)

#method 3.1:
ken_greeting = final_greeting.format(name=name) #also an option. python knows that the first instance of name refers to {name} and the second is our variable

#method 3.2:
friend_name = "Beth"
ken_greeting = final_greeting.format(name = friend_name)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                       User Input
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Example 1
my_name = "Bri"
your_name = input("Enter your name")
print(f"Hi {your_name}, my name is {my_name}.")


#Example 2
age = input("Enter your age") #even tho the user will enter a num, it is stored as a string
print(f"You have lived {age * 12} months.") #PROBLEM! This will just pring the age 12 times! 

#->to fix:
age_num = int(age) #must case the string to an int
print(f"You have lived {age_num * 12} months.") #will now compute age_num * 12 and print the expected statement

#Alternative (Nested)
age = int(input("Enter your age: ")) #Python run the innner most () first, so this is valid
print(f"You have lived {age * 12} months.")

#Boolean values
truthy = True
falsy = False 

#Example 1:
age = 20
is_adult = age >=18 #True
is_minor = age<18 #False
is_twenty = age == 20 #True

#Example 2:
magic_number = 5
your_number = int(input("Enter a number: "))
print(magic_number == your_number) #Will print "True"/"False" depending on the user's input
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                           and & or
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Example 1: AND
age = int(input("Enter your age: "))
can_drive = age >= 16 and age < 90 #The value of the variable will become either "True" or "False"
print(f"Drive Eligability: {can_drive}")

#Example 2: OR - Problem
age = int(input("Enter your age: "))
cant_work = age < 16 or age > 65 #Problem: usually do not want to write variables as negatives. (gets confusing)
print(f"Unemployed: {cant_work}")

#Example 3: Boolean
#Note: most values in boolean are True, except for 0, 0.0, or empty strings. 
bool(35) # = True
bool(0) # = False

bool("Sam") # = True
bool("") # = False

#Example 4: True and False
#Note: python looks at the first value, if its true it will print the second value. Otherwise, it will just print the first value.
x = True and False
print(x) # "False"

x = 35 and 0
print(x) # "0"

x = bool(35) and bool(0)
print(x) # "False"


#Example 5: OR
#Note: Gives you the first value if true, otherwise it gives the second value
x = 35 or 0
print(x) # 35

x = 0 or 0
print(x) # 0

#Example 6:
#Assume you have gotten the first and last name from the user, but for the first name they entered
#an empty string. OR is useful for this.
first_name = ""
last_name = "Smith"
greeting = first_name or f"Mr. {last_name}"

#Example 7: NOT
print(not True) # "False"
print(not False) # "True"
print(not 35) # "False" (python sees "not" and turns 35 into a boolean value)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                           LISTS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Use [] to signify a list

#Example 1: List
friends = ["Mike", "Joe", "Mary", "Sue"]
print(friends) # [Mike, Joe, Mary, Sue]
print(friends[0]) # "Mike"
print(len(friends)) # 4

favorites = [7, "Pizza", "Chevy", 21.5, True] #lists do not have to be homogeneous

friends_detailed = [["Mike", 30],["Joe", 25], ["Mary", 18], ["Sue", 21]]
print(friends_detailed[0]) #Mike 30
print(friends_detailed[0] [1]) # 30

#Add/Remove from list
friends.append("June") #add to end of list
friends.remove("Mike") # removed Mike, readjusted list so Joe is now friends[0]

friends_detailed.append(["June", 27])
friends_detailed.remove(["Mike", 30])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                           TUPLES
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Use () and , to signify a tuple

#Syntax
correct_tuple_syntax = ("String1", "String2") # () no required but they help python recognize its a tuple
also_a_tuple = "String1", "String2" #on it's own, python knows this is a tuple

#Example 1: without () python might get confused
tuples_in_a_list = ["String1", "String2"]
regular_list = ["String1", "String2"] #there is no difference between this var and the one above.

#Solution: use () so python knows its is a list of tuples and not a regular list
tuples_in_a_list_corrected = [("String1", "String2")] #contents inside () are evaluated first

#Example 2: strings vs tuples
string_variable = "String"
tuple_variable = "String",

#Example 3: Adding an element to a tuple
#Technically not possible, but there is a uwork around:
friends_tuple = ("Joe", "Gary", "Maria", "Fran")
friends_tuple = friends_tuple + ("Jen",)
print(friends_tuple) #"Joe", "Gary", "Maria", "Fran", "Jen"

#Note: the initial friends_tuple did not change. we created a new tuple and added two tuples together
#friends_tuple and ("Jen",) were added together and inserted into a new tuple, friends_tuple (same name)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                           SETS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Do not hold order
#Do not contain multiple elements
#Use {} to signify a Set
#Useful in comparing one set to another

#Example 1:
art_friends = {"Anne", "Rob"}

#Add Hanna to art_friends
art_friends.add("Hanna") #Could be added to front, middle, or end of the set. no guarantee on the order

#printing the set out, no order guaranteed
print(art_friends) #Rob, Hanna, Anne

#Try adding duplicate value Hanna
art_friends.add("Hanna")
print(art_friends) # no change, "Rob, Hanna, Anne"

#Remove Hanna
art_friends.remove("Hanna")
print(art_friends) #Rob, Anne


#Example 2: Comparing Sets (Difference)
science_friends = {"Mike", "Lori", "Angela"}
math_friends = {"Angela", "Mary", "Louis", "David"}

#Compare
math_not_science_friends = math_friends.difference(science_friends)
print(math_not_science_friends) #Mike, Lori


#Example 3: Comparing Sets (Symmetric Difference)
not_in_both = math_friends.symmetric_difference(science_friends)
print(not_in_both) # Mike, Lori, Mary, Louis, David

#Example 4: Comparing Sets (intersection)
in_both = math_friends.intersection(science_friends)
print(in_both) #Angela

#Example 5: Comparing Sets (Union)
all_friends = math_friends.union(science_friends)
print(all_friends) #prints all names. angela is only printed once
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                          DICTIONARIES
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Allows you to store keys and values
#Keeps the order in which you added values
#Cannot have duplicate keys, (duplicate values are allowed)


#Example 1: A dictionary with 3 values
friend_ages = {"Adam": 23, "Mary": 25, "Gabby": 22}

#Find Adam's age. "Adam" is the key, his age is the value
print(friend_ages["Adam"]) # 23

#Add a key to the dctionary
friend_ages["June"] = 31

#Update a value in the dictionary
friend_ages["June"] = 32

#Example 2: Using a dictionary inside of a tuple
my_friends = (
    {"name": "Jill Biden", "age": 58},
    {"name": "Melinda Gates", "age": 59},
    {"name": "Kurt Cobain", "age": 27}
)

#Since we used "name" as a key instead of the actual name of the friend, lookup is much easier.
#To lookup, we do not necessarily need to know the name of the friend.
print(my_friends[0]["name"]) #"Jill Biden"

#Example 3: Copy into a new variable
jill_biden = my_friends[0]
print(jill_biden) #"Jill Biden 58"


#Example 4: Dict
#Convert a tuple into a dictionary
jills_friends_tuple = [("Michelle Obama", 61), ("Courtney Love", 48), ("Kamala Harris", 51)]
jills_friends_dictionary = dict(jills_friends_tuple)

print(jills_friends_tuple)
print(jills_friends_dictionary)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                          LENGTH & SUM
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Example 1: calculate average of digits in a list
grades = [90, 88, 80, 65, 70]

total = sum(grades)
length = len(grades)
average = total/length
print(average)

#Side Note: Ideal data structure to hold grades
grades = [90, 88, 80, 65, 70] # List -> SAFEST CHOICE!
grades = (90, 88, 80, 65, 70) # Tuple
grades = {90, 88, 80, 65, 70} # Set -> WORST CHOICE!

#The Set is the worst choice because it cannot hold duplicate values. For this case, we are storing grades
#realistically there is a change we have multiple instances of the same grade. 

#The list is the safest choise of all because he has the least amount of restrictions. and has total felxability

#A big downfall of the tuple is that you cannot technically add new values into a tuple.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                          JOINING A LIST
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#JOIN allows you to print out a list a bit better
#Example 1
friends = ["Anne", "Charlie", "Genny"]
print(f"My friends are: {friends}") # My friends are: ['Anne', 'Charlie', 'Genny']

#Create new variable to format the print statement nicer
comma_separated = ", ".join(friends)
print(f"My friends are: {comma_separated}") #My friends are: Anne, Charlie, Genny

and_separated = " & ".join(friends)
print(f"My friends are: {and_separated}") #My friends are: Anne & Charlie & Genny

#What if we wanted the print statement to look like: My friends are: Anne, Charlie & Genny ?
#Will need to do list splicing... covered in a future topic.