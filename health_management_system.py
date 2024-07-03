def getdate():
    import datetime
    return datetime.datetime.now()


def healthmgmt():
    """This is a health management sysytem that take user inp
    about his exercise or his diet (he/she can write or read both)"""

    print("Enter 0 for Shubham")
    print("Enter 1 for Nitin")
    print("Enter 2 for Mohit")
    client = int(input("Enter : "))
    readorappend = int(input("Enter 1 for read and 0 for write : "))
    diet_ex = int(input("Enter 0 for diet and 1 for excercise : "))
    if client == 0:
        if readorappend == 0:
            if diet_ex == 0:
                with open("shubham_diet.txt", "a") as f:
                    diet = input("What did u ate : ")
                    f.write(str(getdate()) + " : " + diet + "\n")
                    print("Successfully entered : ", diet)
            elif diet_ex == 1:
                with open("shubham_exercise.txt", "a") as f:
                    exercise = input("Which exercise u performed : ")
                    f.write(str(getdate()) + " : " + exercise + "\n")
                    print("Successfully entered : ", exercise)
        elif readorappend == 1:
            if diet_ex == 0:
                with open("shubham_diet.txt", "r") as f:
                    print(f.read())
            elif diet_ex == 1:
                with open("shubham_exercise.txt", "r") as f:
                    print(f.read())
    if client == 1:
        if readorappend == 0:
            if diet_ex == 0:
                with open("Nitin_diet.txt", "a") as f:
                    diet1 = input("What did u ate : ")
                    f.write(str(getdate()) + " : " + diet + "\n")
                    print("Successfully entered : ", diet1)
            elif diet_ex == 1:
                with open("Nitin_exercise.txt", "a") as f:
                    exercise1 = input("Which exercise u performed : ")
                    f.write(str(getdate()) + " : " + exercise1 + "\n")
                    print("Successfully entered : ", exercise1)
        elif readorappend == 1:
            if diet_ex == 0:
                with open("Nitin_diet.txt", "r") as f:
                    print(f.read())
            elif diet_ex == 1:
                with open("Nitin_exercise.txt", "r") as f:
                    print(f.read())
    if client == 2:
        if readorappend == 0:
            if diet_ex == 0:
                with open("Mohit_diet.txt", "a") as f:
                    diet2 = input("What did u ate : ")
                    f.write(str(getdate()) + " : " + diet2 + "\n")
                    print("Successfully entered : ", diet2)
            elif diet_ex == 1:
                with open("Mohit_exercise.txt", "a") as f:
                    exercise2 = input("Which exercise u performed : ")
                    f.write(str(getdate()) + " : " + exercise2 + "\n")
                    print("Successfully entered : ", exercise2)
        elif readorappend == 1:
            if diet_ex == 0:
                with open("Mohit_diet.txt", "r") as f:
                    print(f.read())
            elif diet_ex == 1:
                with open("Mohit_exercise.txt", "r") as f:
                    print(f.read())


healthmgmt()
