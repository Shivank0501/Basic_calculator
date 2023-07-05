while True:
    print("*** Basic Calculator ***")
    Num_1 = int(input("Enter first number =  "))
    Num_2 = int(input("Enter second number =  "))


    def add(Num_1, Num_2):

        print(Num_1+Num_2)

    def sub(Num_1, Num_2):

       print(Num_1 -Num_2)

    def Mul(Num_1, Num_2):

        print(Num_1 * Num_2)

    def Div(Num_1, Num_2):

        print(Num_1/Num_2)

    def power(Num_1, Num_2):

        print(Num_1**Num_2)

    def mod(Num_1, Num_2):

        print(Num_1//Num_2)

    choose = int(input("Press 1 For Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for division \nPress 5 for Power \nPress 6 for Modulation\n--> "))

    if choose == 1:
        add(Num_1, Num_2)

    elif choose == 2:
        sub(Num_1,Num_2)

    elif choose ==3:
        Mul(Num_1, Num_2)

    elif choose ==4:
        Div(Num_1, Num_2)

    elif choose ==5:
        power(Num_1, Num_2)

    elif choose ==6:
        mod(Num_1,Num_2)

    else:
        print("Enter correctly")

    x= input("Calculate again? = y/n")

    if x=="n":
        print("Thank You for Using")
        break

