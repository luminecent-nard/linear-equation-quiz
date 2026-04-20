import random

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
math_list = ["+","-","*"]
question_format = ["1","2","3","xxx"]
read_format = ["a + 5 = 10 (1)", "a - 5 = 5 (2)", "a5 = 10 (3)"]
format_decider = random.choice(question_format)
format_choice_list = []
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

    math_type = random.choice(math_list)
    int_1 = random.randint(1, 100)
    int_2 = random.randint(1, 100)


    type_1 = f"a{math_type}{int_1}={int_2}"
    type_2 = f"a{int_1}={int_2}"
     


