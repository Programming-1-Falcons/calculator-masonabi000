space = " -- "

while True:
    print (space)
    print (space)
    print ("Welcome to Calculator!")
    print (space)
 
    #user chooses which operation they want to use
    print("Operation options: addition, subtraction, division, multiplication, exponents")
    chosen_operation = input("What operation would you like to perform? (type the word in lowercase): ")
    print(space)
    
    print (chosen_operation + " of which two numbers? ")

    #user chooses which numbers will be used in the operation in order
    num_1 = float(input("1st number?: "))
    num_2 = float(input("2nd number?: "))
    print(space)

    #perform the operation
    if chosen_operation == "addition":
        print (str(num_1) + " + " + str(num_2) + " = ")
        print(num_1 + num_2)

    elif chosen_operation == "subtraction":
        print(str(num_1) + " - " + str(num_2) + " = ")
        print(num_1 - num_2)

    elif chosen_operation == "division":
        if num_2 == 0:
            print("Error. Cannot divide by 0")
        else:
            print(str(num_1) + " / " + str(num_2) + " = ")
            print(num_1 / num_2)

    elif chosen_operation == "multiplication":
        print(str(num_1) + " * " + str(num_2) + " = ")
        print(num_1 * num_2)

    elif chosen_operation == "exponents":
        print(str(num_1) + " ^ " + str(num_2) + " = ")
        print(num_1 ** num_2)

    else:
        print ("This is not a performable operation! Please try again.")
