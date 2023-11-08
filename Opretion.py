def App():
    first_number= int(input("What's Your fisrt number? "))
    second_number= int(input("What's Your second number? "))

    print("Your fisrt number is ",first_number," Your second number is " ,second_number)
    def adding_operation():
        operation = input("Which Operation do you want (+,-,*,/) : ")

        def continue_message():
            re_calc = input("Do you want to go agein?(yes,no)")
            if re_calc == "yes":
             return App()
            else:
                print("thanks for your time")

        def plus():
            print(first_number + second_number)
            continue_message()
        
        def minus():
            print(first_number - second_number)
            continue_message()

        def multiplication():
            print(first_number * second_number)
            continue_message()

        def division():
            print(first_number / second_number)
            continue_message()
        # def continue_message():
        #     re_calc = input("Do you want to go agein?(Yes,No)").lower
        #     if re_calc == "yes":
        #      return "hii"
        #     else:
        #         print("thanks for your time")

        if operation == "+":
                plus()
        elif operation == "-":
                minus()
        elif operation == "*":
                multiplication()
        elif operation == "/":
                division()
        else:
            print("Plz enter one of those operation(+,-,*,/)")
            return adding_operation()
    adding_operation()

App()



