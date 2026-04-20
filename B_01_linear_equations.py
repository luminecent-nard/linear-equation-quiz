import random

#functions

def string_checker(question, valid_ans=('yes', 'no')):
    error = f"please enter a valid option from the following list: {valid_ans}"
    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            #check if the user response is a word in the list
            if item == user_response:
                return item

            #check if user response is the same as
            #the first letter of an item in the list
            elif user_response == item[0]:
                return item
        #print error if user does not enter something that is valid
        print(error)
        print()

def make_statement(statement, decoration):
    """adds emoji/decoration to headings"""

    ends = decoration * 3
    print(f"{ends} {statement} {ends}")

def instructions():
    """prints instructions"""

    print("""
*** Instructions ***
Welcome to the amazing quiz of linear equations, here you wil be doing MATH!!
(scary i know) so grab your calculator and i will explain how to solve linear equations!

Linear equations are a  part of algebra that involve solving a equation backwards
to find the value of the variable in the question, for example:
    
    a + 7 = 10
    
We can figure out (a) quite easily by reversing the equation:

    10 - 7 = a
    
This is now a very simple equation now and we just need to do basic math:

    10 - 7 = 3
    
To note:
In algebra, you don't use the times symbol to not confuse it with the letter x
instead if a number and a variable are next to each other like 2a + 3 = 17
it is to be treated as 2 x a + 3 = 17.
    """)
#main routine starts here
#int variables

#greet user
print()
make_statement("The amazing quiz of linear equations", "+-=-+")
print()

#instructions

want_instructions = string_checker("would you me to explain how to solve linear equations? ")
if want_instructions == "yes":
    print(instructions())
#ask questions that the quiz will be about

#QUIZ TIME