import random

#functions
def int_check(number_question, low=None, high=None, exit_code=None):

    #if any integer is allowed
    if low is None and high is None:
        error = "Please enter an integer"

    #if the number needs to be below low and high

    else:
        error = "incorrect, next question"

    error_2 = "please enter an integer"

    while True:
        response = input(number_question).lower()

        #check for infinite mode / exit code
        if response == exit_code:
            return response

        try:


            response  = int(response)


            #check the interger is not too low
            if low is not None and response < low:
                return error

            #check response is more than low
            elif high is not None and response > high:
                return error

            #if response is valid return it
            else:
                return response

        except ValueError:


            print(error_2)

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
end_game = ""
current_question = ""
readable_question = []
correct_ans = int
math_list = ["+","-"]
question_format = ["+","-","xxx"]
read_format = ["a + 5 = 10 (+)", "a - 5 = 5 (-)"]
format_choice_list = []
chosen_math = []
questions_answered =  0
mode = "normal"

#greet user
print()
make_statement("The amazing quiz of linear equations", "+-=-+")
print()

#instructions

want_instructions = string_checker("would you me to explain how to solve linear equations? ")
if want_instructions == "yes":
    print(instructions())
#ask questions that the quiz will be about

#quiz length
total_questions = int_check("\nHow many questions do you want to answer (press <enter> for infinite): ",
                       low=1,exit_code="")

if total_questions == "":
    mode = "infinite"
    total_questions = 5

#ask what formats
print("\npick what kind of formats you want to have in your quiz\n"
      "and write the symbol that corresponds with the format below (+ or -)\n"
      "use xxx to leave once you are finished\n")

while True:

    print(read_format)
    print(f"\nso far you have chosen {format_choice_list}\n")
    #ask user what formats they want
    format_choice = string_checker("choose the kind of formats you want: ", valid_ans=question_format)
    #repetition canceller
    if format_choice in format_choice_list:
        print("\nyou already chose that\n")

    elif "-" and "+" in format_choice_list:
        format_choice_list.append(format_choice)
        print()
        break

    elif format_choice == "xxx" and format_choice_list == []:
        print("\nplease pick a format\n")

    elif format_choice == "xxx":
        break

    else:
        format_choice_list.append(format_choice)
    format_choice_list.sort()

#display choices
print(f"you chose:{format_choice_list}")

#makes the questions readable and calculates them
while questions_answered < total_questions:

    while end_game != "yes":

        #adds the +'s and -'s
        if "+" in format_choice_list:
            chosen_math.append("+")
        elif "-" in format_choice_list:
            chosen_math.append("-")
        math_type = random.choice(chosen_math)

        #pick number
        int_2 = random.randint(2,99)
        int_1 = random.randint(1,99)

        if math_type == "+":
            while int_2 < int_1:

                int_2 = random.randint(2, 99)

        else:
            while int_2 > int_1:

                int_2 = random.randint(1,99)

        #clears the question list
        readable_question = []

        #makes the computer do magic math

            #format type 1
        current_question = f"{int_1} {math_type} {int_2}"
        expected_answer = eval(current_question)
        readable_question_1 = f"a {math_type} {int_2} = {expected_answer}"
        readable_question.append(readable_question_1)


        #print answer for testing purposes
        print(f"int_1 or answer: {int_1}")
        # print(f"computer question: {current_question}")


        #print question
        print()
        print(f"question: {questions_answered + 1}")
        print()
        question = random.choice(readable_question)
        print(question)


        user_answer = int_check("Answer: ", low=int_1, high=int_1, exit_code="xxx")

        questions_answered += 1

        # make infinite infinite
        if mode == "infinite":
            total_questions += 1

        if user_answer != "xxx":
            print(user_answer)

        if user_answer == int_1:
            print("you got it :)")
        elif user_answer == "incorrect, next question":
            break





        if user_answer == "xxx":
            end_game = "yes"
            break

    if end_game == "yes":
        print("quiz over")
        break