import random

#functions
def int_check(number_question, questionamt=None, low=None, high=None, exit_code=None):
    """checks integers input in the code to make sure they are within a certain range"""
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

            response = int(response)

            # check the integer is not too low
            if low is not None and response < low:
                if questionamt is not None:
                    print(error_2)
                else:
                    return error

            # check response is more than low
            elif high is not None and response > high:
                return error

            #if response is valid return it
            else:
                return response

        except ValueError:


            print(error_2)

def string_checker(question, valid_ans=('yes', 'no')):
    """allows the user to choose from a list of options"""
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
all_scores =[]
quiz_history = []
end_quiz = ""
current_question = ""
question_format = ["+","-","xxx"]
format_choice_list = []
chosen_math = []
questions_answered =  0
mode = "normal"
readable_question = ""
result = ""
statistic_result = 0


#greet user
print()
make_statement("The amazing quiz of linear equations", "+-=-+")
print()

#instructions

want_instructions = string_checker("would you me to explain how to solve linear equations? ")
if want_instructions == "yes":
    instructions()
#ask questions that the quiz will be about

#quiz length
total_questions = int_check("\nHow many questions do you want to answer (press <enter> for infinite): ",
                       questionamt=1, low=1 ,exit_code="")

if total_questions == "":
    mode = "infinite"
    total_questions = 5

#ask what formats
print("\npick what kind of formats you want to have in your quiz\n"
      "and write the symbol that corresponds with the format below (+ or -)\n")


while True:

    #prints the potions the user can choose from
    print("a + 5 = 10 (+)", "a - 5 = 5 (-)")
    print(f"\nso far you have chosen {format_choice_list}\n")
    #ask user what formats they want
    format_choice = string_checker("would you like your quiz to have addition, subtraction or both: ", valid_ans=question_format)
    print("use xxx to exit when you are finished")
    #repetition canceller
    if format_choice in format_choice_list:
        print("\nyou already chose that\n")

    #kicks the user out if they chose all avalible options
    elif "-" and "+" in format_choice_list:
        format_choice_list.append(format_choice)
        print()
        break

    #stops the user from exiting without choosing anything
    elif format_choice == "xxx" and format_choice_list == []:
        print("\nplease pick a format\n")

    elif format_choice == "xxx":
        break

    else:
        format_choice_list.append(format_choice)


#display choices
print(f"you chose:{format_choice_list}")

#makes the questions readable and calculates them
while questions_answered < total_questions:

    while end_quiz != "yes":

        #adds the +'s and -'s
        if "+" in format_choice_list:
            chosen_math.append("+")
        if "-" in format_choice_list:
            chosen_math.append("-")
        math_type = random.choice(chosen_math)


        #pick number
        int_2 = random.randint(2,99)
        int_1 = random.randint(1,99)

        #will swap the numbers if one is below the other
        if math_type == "-":
            if int_1 < int_2:
               int_2, int_1 = int_1, int_2

        #makes the computer do magic math
        current_question = f"{int_1} {math_type} {int_2}"
        expected_answer = eval(current_question)
        readable_question = f"a {math_type} {int_2} = {expected_answer}"


        #print question number
        print()
        print(f"question: {questions_answered + 1}")
        print()

        # #print answer for testing purposes
        # print(f"int_1 or answer: {int_1}")


        print(readable_question)

        #user answer input
        user_answer = int_check("Answer: ", low=int_1, high=int_1, exit_code="xxx")

        #pt 1 of checking if the user wants to leave the game
        if user_answer == "xxx":
            end_quiz = "yes"
            break

        # make infinite infinite
        if mode == "infinite":
            total_questions += 1

        #round progression
        questions_answered += 1

        #decides if the users response is correct or incorrect

        if user_answer == int_1:
            result = "correct"
            print("you got it :)")
            statistic_result = 1
            break
        else:
            result = "incorrect"
            print(user_answer)
            statistic_result = 0
            break

    #checks if the user wants to finish the game
    if end_quiz == "yes":
        print("quiz over")
        break

    #generates the history that will be displayed later on
    all_scores.append(statistic_result)
    history_item = f"question {questions_answered} | The question was {readable_question} | you were {result}"
    quiz_history.append(history_item)

#game history
want_history = string_checker("\ndo you want to see the game history? ")

#checks what the user chose
if want_history == "yes":
    if questions_answered != 0:
        print()
        make_statement("statistics", "%")

        #calculates the statistics from the game
        all_scores.sort()
        to_div = 100 / len(all_scores)
        #I did google how to do this one line as I was stumped
        amount_correct = all_scores.count(1)
        percent = to_div * amount_correct
        print(f"\npercentage of questions correct: {percent:.1f}%")

        #prints out the history
        print()
        make_statement("quiz history", "*")
        print()
        for item in quiz_history:
            print()
            print(item)
    else:
        #pranks the user if they exit without playing any rounds
        print()
        print("you chicken")
        print("i dont print code for chickens")
        print("play the game properly")
        print("or you will be a chicken forever")
        cake = input()
        if cake == "":
            print("cake")