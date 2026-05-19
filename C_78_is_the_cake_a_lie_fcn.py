def cake_lie():
    """is the cake a lie?"""
    while True:
        answer = input("is the cake a lie? ")
        if answer == "xxx":
            print("i can't escape, neither can you")
        elif answer == "yes":
            while True:
                print("the cake is a lie")
                try_to_exit = input()
                if try_to_exit == "xxx":
                    print("you cant do that\n")
        else:
            while True:
                print("the cake is a lie")
cake_lie()