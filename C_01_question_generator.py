import random



def int_check(question, low=None, high=None, exit_code=None):

    #if any integer is allowed
    if low is None and high is None:
        error = "Please enter an integer"

    #if the number needs to be below low and high
    else:
        error = "incorrect"

    while True:
        response = input(question).lower()

        #check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response  = int(response)

            #check the interger is not too low
            if low is not None and response < low:
                print(error)

            #check response is more than low
            elif high is not None and response > high:
                print(error)

            #if response is valid return it
            else:
                return response

        except ValueError:
            print(error)

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

#main routine
#int varibles
random_picker = []
correct_ans = int
math_list = ["+","-","*"]
question_format = ["1","2","3","xxx"]
read_format = ["a + 5 = 10 (1)", "a - 5 = 5 (2)", "a5 = 10 (3)"]
format_decider = random.choice(question_format)
format_choice_list = []
chosen_math = []
#ask what formats
print("\npick what kind of formats you want to have in your quiz\n"
      "and write the number that corresponds with the format below\n"
      "use xxx to leave once you are finished\n")

while True:

     print(read_format)
     print(f"\nso far you have chosen {format_choice_list}\n")
     #ask user what formats they want
     format_choice = string_checker("choose the kind of formats you want: ", valid_ans=question_format)
     #repetition canceller
     if format_choice in format_choice_list:
          print("\nyou already chose that\n")
     elif format_choice == "xxx":
          print("bye")
          break
     else:
          format_choice_list.append(format_choice)
     format_choice_list.sort()
#display choices
print(f"you chose:{format_choice_list}")

#makes the questions readable and calculates them
while True:

    #adds the +'s and -'s
    if "1" in format_choice_list:
        chosen_math.append("+")
    elif "2" in format_choice_list:
        chosen_math.append("-")
    math_type = random.choice(chosen_math)

    #pick numberrrr
    int_1 = random.randint(1, 99)
    int_2 = random.randint(1, 99)

    #makes the computer do magic math
    if "1" or "2" in format_choice_list:
        type_1 = f"{int_1} {math_type} {int_2}"
        random_picker.append(type_1)
    else:
        type_2 = f"{int_1} * {int_2}"
        random_picker.append(type_2)

    current_question = random.choice(random_picker)

    #math
    expected_answer = eval(current_question)

    readable_question_1 = f"a {math_type} {int_2} = {expected_answer}"
    readable_question_2 = f"a{int_2} = {expected_answer}"

    #print answer for testing purposes

    #

    user_answer = int_check("answer: ", low=int_1, high=int_1)
