#Fundamental topics in Python
#This file contains notes that I have taken while in Section 2 of 'The Complete Python Course' on Udemy
#Topics covered in this file:
    # If Statements
    # While Loops
    # For Loops
    # Destructing
    # Iterating over Dictionaries
    # Break & Continue
    # Else keywonrd in loops
    # List Slicing
    # List Comprehension
    # Comprehension with Conditionals
    # Set and Dictionaries Comprehension
    # Zip function
    # Enumerated function
    # Functions in Python
    # Arguments and Parameters
    # Functions and Return values
    # Default Parameter values
    # Lamda Functions
    # First-class functions


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                          If Statement
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Example 1
friend = "Genny"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!")
    print("As long as we keep these prints in line, this will be contained in the if statement")
#if statement ends here

print("This is not in the if statement")



#Example 2: The Else condition
secret_word = "Bananas"
your_word = input("Enter a word: ")

if your_word == secret_word:
    print("Thats the secret word!")
else:
    print("Thats NOT the secret word!")



#Example 3: Boolean functions
my_bool = 0
your_bool = 5

if my_bool:
    print("This statement will never execute because 0 = false")
#end if

if your_bool:
    print("True!") #This will print since 5 is always true
#end if



#Example 4: Check if user input is valid
your_name = input("Enter your name: ")

if your_name:
    print("You have entered a valid name!")
else:
    print("You did NOT enter a valid name.")



#Example 5: lists and nested if statements
friends = ["Margo", "Jan", "Don"]
family = ["Genny", "Mary", "Louise"]

user_name = input("Enter your name:")

if user_name in friends:
    print("Hello friend!")
elif user_name in family:
    print("Hello family!")
else:
    print("I do not know you...")
#end if
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                          While Loops
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#use when you want to repeat something an UNDEFINED number of times!


#Example 1: the basics
is_learning = True

while is_learning:
    print("you're learning!")
    is_learning = False #Terminates the loop
#end while



#Example 2: get user input to terminate loop
is_learning = True

while is_learning:
    print("you're learning!")
    user_input = input("Are you still learning? ")
    is_learning = user_input == 'yes'
#end while



#Example 3: Simple menu with User input
user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes":
    print("The program is running.")
    user_input = input("Do you wish to continue running the program? (yes/no): ")
#end while

print("Program has stopped running")



#Example 4: Menu  --> my practice. not tested
menu = """Options:
1. Display Name
2. Display Age
3. Display Employment Status
4. Exit"""
print(menu)

user_input = input("Enter your choice: ")

while user_input != 4:
    if user_input == 1:
        print("You entered 1. Display Name")
        print("Name: Bri")
    elif user_input == 2:
        print("You entered 2. Display Age")
        print("Age: 27")
    elif user_input == 3:
        print("You entered 3. Display Employment Status")
        print("Employment Status: Employed")
    elif user_input == 4:
        print("You entered 4. Exit")
        print("Goodbye!")
    else:
        print("Your option is not valid")
    #end if

    print(menu)
    user_input = input("Enter your choice: ")
#end while


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                          For Loops
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#use when you want to execute something a DEFINED number of times!
#Syntax: For <new variable> in <list>:
#can be used with a list, tuple, set, etc. (any iterable)

#Example 1: print the names of friends on separate lines
friends = ["Margo", "Jan", "Don"]

for friend in friends:
    print(friend)

#note that friend is not previously defined variable. we are telling ptyon to
#define friend once for every friend. friend will be the first element in friends (margo)
#then when the loops repeats again, friend will become 'jan'.


#Example 2: use the list as a counter
counter = [1,2,3,4,5,6,7,8,9]

for _ in counter:
    print("Hello!")

#you do not necessarily have to do anything with the contents of the list. in this
#example, we used the list as a way to print out the same thing 9 times.

#instead of creating a name for the new variable, we denote it as _ since we are not using it in the loop.
#_ is a signal to other python users that you do not intend on using the contents of the list.


#Example 3: use Range instead of what we did in example 2
for index in range(9):
    print("Hello!")

#Does the exact same thing as example 2, except we used range instead of a list.


#Example 3: Range
#1. use Range instead of what we did in example 2
for index in range(9):
    print("Hello!")
#Does the exact same thing as example 2, except we used range instead of a list.

#2. print the last 2 digits in range 10
for index in range(2, 10):
    print(index)
#prints:
# 9
# 10

#3. gives you the number from 2 to 19, but only every 3 numbers
for index in range(2, 20, 3):
    print(index)


#Example 4: dictonaries
students = (
    {"name": "Jill", "grade": 58},
    {"name": "Melinda", "grade": 59},
    {"name": "Kurt", "grade": 27}
)

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has the grade of {grade}")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                       Destructuring
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#taking a tuple and breaking it down into multiple variables

#Example 1: tuple
currencies = 0.8, 1.2
usd, eu = currencies #usd = 0.8 and eu = 1.2

#Example 2: list of tuples
my_friends = [("Libby", 31), ("Miranda", 29), ("Charles", 32), ("Brandon", 27)]

for name, age in my_friends:
    print(f"{name} is {age} years old.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                    Iterating over Dictonaries
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Example 1
students = {"Jill":58, "Melinda": 59, "Kurt": 27}

#only prints the keys in our dictionary and not the values
for name in students:
    print(name)

#only prints the values in our dictionary and not the keys
for age in students.values():
    print(age)

#print both the name and ages via destructuring
for name, age in students.items():
    print(f"{name} is {age} years old.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                    Break & Continue
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Break will stop the loop - terminate it completely
#Continue will skip the current iteraion of the loop and go to the next iteration

#Example 1: Stop a loop when we encounter a specific value
#Scenario: suppose we have a list of car productions. Most are ok but sometimes we get a faulty one.
#When we encounter a faulty one, we want to stop the production line entirely.
cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

#iterate over the list
for status in cars:
    if status == "faulty":
        print(f"Stopping the production line!")
        break
    print(f"This car is {status}")
    print("Shipping car to customer.")


#Example 2: skip over a value then continue the loop w/o terminating it
cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

#iterate over the list
for status in cars:
    if status == "faulty":
        print(f"Faulty car detected.. Skipping.")
        continue
    print(f"This car is {status}")
    print("Shipping car to customer.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                    Else in Loops
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                    List Comprehension
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Example 1: you want to take a list of numbers and multiply it by 2
numbers = [0,1, 2, 3, 4,]
doubled_numbers = [numbers * 2 for number in numbers] # much quicker than using a for loop

#Example 1.a: can also use range
doubled_numbers = [numbers * 2 for numbers in range(5)]


#Example 2: you have a list of friends ages, and want to create a new list of strings describing the age
friends_ages = [22, 31, 27, 19, 29]
age_string = [f"My friend is {age} years old." for age in friends_ages]


#Example 3: you have a list of friends names and want to create a new list of their names lower-case
names = ["Jen", "Marty", "Jon", "Kim"]
lower = [name.lower() for name in names]
#useful technique for making comparisons with user input (if they entered a name in lower case)


#Example 3.a: user input comparison usefulness
friend = input("Enter your friends name: ")
friends = ["Jen", "Marty", "Jon", "Kim"]
friends_lower = [name.lower() for name in friends]

#converts user input to lower case and compares to friends_lower list.
if friends.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends.")
#ensures regardless of the capitalization methos, if the user spells the name correct, this will run soccessfully.
#friend.title() converts the case to This, regardless of the input.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                     Comprehensions with Conditionals
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Example 1: you want to retreive only ages that are odd number only
ages = [21, 29, 30, 32, 22]
odds = [age for age in ages if age %2 == 1]

#Example 2: you want to compare friends list to guest list, but the list contains mixed case names
friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = set([friends.lower() for friend in friends]) #convert all friends to lower case and puts them into a set
guests_lower = set([guests.lower() for guest in guests]) #converts all guests to lower and puts them into a set

print(friends_lower.intersection(guests_lower)) #prints charlie and rolf (in lowercase)


#Example 2b: you want the print statement to have capital names. Instead of set, use list comprehension
friends_lower = [friends.lower() for friend in friends] #converts to lower but doesnt use a set

present_friends = [
    name.title()
    for name in guests
    if name.lower() in friends_lower
]

print(present_friends)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                     Set and Dictionary Comprehensions
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Example 1: you want to compare friends list to guest list, but the list contains mixed case names - with Set Comprehension
friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {friends.lower() for friend in friends}
guests_lower = {guests.lower() for guest in guests}

present_friends = {name.title() for name in friends_lower.intersection(guests_lower)}
print(present_friends)


#Example 2: you have a list of friends and a list of time last seen - you want to create a dictionary out of them
friends = ["Rolf", "Anne", "Charlie", "Jen"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
} #Associate friends list with time_since_seen list

print(long_timers)

#Example 2b: if you want to print only friends you havnt seen in > 5 years
long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen > 5 #you can add a conditional like this
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                     Zip Function
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Zip combines two lists (or more) into one list
#if the lists are different lengths, the result will always be the len of the shortest list

#Example 1: combine the friends and time_since_seen lists with Zip function
friends = ["Rolf", "Anne", "Charlie", "Jen"]
time_since_seen = [3, 7, 15, 11]

#create [(Rolf, 3), (Anne, 7), (Charlie, 15), (Jen, 11)]
long_timers = dict(zip(friends, time_since_seen))

#now we do not need to use the long_timers set comprehension function (from prev section)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                     Enumerate Function
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Can use enumerate to turn a list into something new
#starts at 0 by default

#Example 1: associate list of friends with their index
friends = ["Rolf", "John", "Anna"]

print(list(enumerate(friends))) #same as (list(zip([0,1,2], friends)))
print(dict(enumerate(friends))) #can also turn into a dictionary instead of list

#Example 2: start index at 1 instead of default 0
print(list(enumerate(friends, start=1)))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                     Functions in Python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Example 1: basic function definition
def greet():
    name = input("Enter your name:")
    print(f"Hello, {name}!")

#call the function - must be done after the function is defined!
greet()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                     Arguments and Parameters
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Imagine you've got some code that calculates the fuel efficiency of a car:

car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}

mpg = car["mileage"] / car["fuel_consumed"]
name = f"{car['make']} {car['model']}"
print(f"{name} does {mpg} miles per gallon.")

# You could put this in a function:


def calculate_mpg():
    car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}

    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")


calculate_mpg()

# But this is not a very reusable function since it only calculates the mpg of a single car.
# What if we made it calculate the mpg of "any" arbitrary car?

car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}


def calculate_mpg(car_to_calculate):  # This can be renamed to `car`
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")


#calculate_mpg(car)

# This means that given a list of cars with the correct data format, we can run the function for all of them!

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

for car in cars:
    calculate_mpg(car)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                     Functions and Return values
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg  # Ends the function, gives back the value


def car_name(car):
    return f"{car['make']} {car['model']}"


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)

    print(f"{name} does {mpg} miles per gallon.")
    # Returns None by default, as all functions do


cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

for car in cars:
    print_car_info(car)
    # try print(print_car_info(car)), you'll see None


# -- Multiple returns --


def divide(x, y):
    if y == 0:
        return "You tried to divide by zero!"
    else:
        return x / y


print(divide(10, 2))  # 5
print(divide(6, 0))  # You tried to divide by zero!

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                     Default parameter values
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def add(x, y=3):  # x=2, y is not OK
    total = x + y
    print(total)


add(5)
add(2, 6)
add(x=3)
add(x=5, y=2)

# add(y=2)  # ERROR!
# add(x=2, 5)  # ERROR!


# -- More named arguments --
print(1, 2, 3, 4, 5, sep=" - ")  # default is " "

# You can use almost anything as a default parameter value.
# But using variables as default parameter values is discouraged, as that can introduce difficult to spot bugs

default_y = 3


def add(x, y=default_y):
    sum = x + y
    print(sum)


add(2)  # 5

default_y = 4
print(default_y)  # 4

add(2)  # 5

# Be careful when using lists or dictionaries as default parameter values. Unlike integers or strings, these will update if you modify the original list or dictionary.
# This is due to a language feature called mutability. It's not important to understand this now, but just know that they behave differently to integers and strings behind the scenes when you change them.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                     Lambda functions
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Lambda functions are functions that are almost solely used to get inputs and return outputs.
# That means we don't often use them to make actions.
# For example, the `print()` function is a function that performs an action. As such, it would not be suitable for lambda function.
# If we wanted a function that just divided two numbers, that might be suitable for a lambda function.

# That's because that function takes inputs, processes them, and returns outputs. And, it's a short, simple function. You'll see why that is relevant with this example.

divide = lambda x, y: x / y
# This spacing is common. After each comma in the parameters, after the colon but not before, and between operators (though that's optional, and sometimes will be seen without spaces).

# That is a lambda function, which takes two arguments and returns the result of dividing one by the other. It is almost identical to this function:


def divide(x, y):
    return x / y


# In both cases you would call it as a normal function:

print(divide(15, 3))

# While traditional functions _need_ the name (you can't define one without it), lambda functions don't have names unless you assign them to a variable.

result = (lambda x, y: x + y)(15, 3)
print(result)

# However you can see that lambda functions can be quite difficult to read, so we won't be using them very often. The main reason to use lambda function is because they are short, so if we use them in conjunction with other functions that can help make our programs a bit more flexible.

# Here's an example. Instead of this:


def average(sequence):
    return sum(sequence) / len(sequence)


students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))

# Since the average function just takes inputs and returns an output, we could re-define it as a lambda function.

average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                     First Class functions
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#First class functions refer to the fact that you can assign them to variables, put it inside lists, dictionaries, or anything else.
# Can also pass functions to other functions 
#  

#Example 1: Assigning to a variable
def greet():
    print("Hi, how are you?")

#This function will run if we call it the usual way, with greet()
#But, we can also call it by assigning the the function call to another variable:
hello = greet   #python knows that greet refers to the greet function. even though we didnt use ()
hello()         #will execute the greet function. behaves exactly the same as running greet()




#Example 2:
#you have some lambda functions
avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

#create association between user input choices and the lambda functions
#Use a dictionary. Drawback: if  the user enters a key that doesnt exist in the dictionary, we will get an error.- Will have to use Error Handling (in a future section)
operations = {
    "average": avg,
    "total": total,
    "top": top,
}

sudents = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

#perform operations on each students grades
for student in students:
    name = student["name"]
    grades = student["grades"]

    #have user choose the desired operation to compute
    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top': ")

    #handle user input
    operation_function = operations[operation] #does not get the result of the function, just identifies which lambda function to use
    print(operation_function(grades))



#Can make this code shorter if we inline the lambda functions with the dictionary:
#and instead of using our lambda functions, we can just call the internal functions directly (for the total and top lambda functions)
# operations = {
#     "average": lambda seq: sum(seq) / len(seq),
#     "total": sum(seq),
#     "top": max(seq),
# }

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

