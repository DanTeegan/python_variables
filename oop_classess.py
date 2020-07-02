# Why should we create a class?
# Create a class with key word called class
# Naming convention for creating a class is to capitalise the first letter

# Everything is an object in a class
# Self keyword refers to the class




# This defines the class. In this case it is called Python_Calculator
class Python_Calculator:

# Created a function to add the users input. Choice 1
    def add_values(self,):
        print("Your numbers where {} and {} so the answer is: ".format(num1, num2), (num1+num2))

# Created a function to subtract the users input. Choice 2
    def subtract_values(self,):
        print("Your numbers where {} and {} so the answer is: ".format(num1, num2), (num1 - num2))

# Created a function to multiply the users input. Choice 3
    def multiply_values(self,):
        print("Your numbers where {} and {} so the answer is: ".format(num1, num2), (num1 * num2))

# Created a function to divide the users input. Choice 4
    def divide_values(self,):
        print("Your numbers where {} and {} so the answer is: ".format(num1, num2), (num1 / num2))

# Created a function to modulus the users input. Choice 5
    def remainder_values(self,):
        print("Your numbers where {} and {} so the answer is: ".format(num1, num2), (num1 % num2))

# Here we are asking for the user input
num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter a second integer: "))


# Here we are creating the object Python_Calculator
object = Python_Calculator()

choice = 1
# Using a while loop to iterate through the calculation choices
# Here the while loop is stating when choice is not 0 print
while choice !=0:

# Displaying the user with the a choice of 5 math operators
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Remainder (Modulus)")

# Getting the input for the calculation from the user
    choice = int(input("Please enter your required calculation: "))

# Control flow to choose the outcome of the maths operator. These choices are linked back to the while loop
    if choice == 1:
        print(object.add_values())
    elif choice == 2:
        print(object.subtract_values())
    elif choice == 3:
        print(object.multiply_values())
    elif choice == 4:
        print(object.divide_values())
    elif choice == 5:
        print(object.remainder_values())
    else:
        print("Invalid choice")




# Create a basic calculator inside a class
# Should have methods to add, subtract, divide, multiply and modulus
# create an object of a class / Run the class

# Methods are inside the class
# Functions are outside the class
