welcome_text ="Welcome to FullAdder!"
flag = True
not_in_correct_form = False
total = 0
carry_out = 0
computed = False

print(f"{welcome_text}\n"+'_'* len(welcome_text))

while not computed:
    print("(1) Compute and Display the Outputs\n(2) Exit") 
    ans = input("What do you want to do?")

    if ans == "1":
        print("Lets compute")

        while not computed:
            base = int(input("Which base you will enter? (2, 8, 16)"))

            if base == 2:
                while True:
                    number = input("Please Enter the number you want in base 2:")

                    not_in_correct_form = False

                    if len(number) > 3: 
                        print("Please enter a value with max 3 digits")
                    else:
                        for digit in number:
                            if not digit in "01":
                                not_in_correct_form = True
                                
                    if not_in_correct_form:
                        print("You entered in incorrect format\nPlease Enter Again")

                    else:
                        
                        while len(number) < 3:
                            number = "0" + number

                        A = int(number[0])
                        B = int(number[1])
                        C = int(number[2])

                        computed = True

                        break

            elif base == 8:
                while True:
                    number = input("Please Enter the number you want in base 8:")

                    not_in_correct_form = False
                    
                    if len(number) > 1:
                        print("Please enter only 1 digit")# https://en.wikipedia.org/wiki/Octal#:~:text=Binary%20to%20octal%20conversion%5Bedit,Octal%20to%20hexadecimal%20conversion
                    else:
                        for digit in number:
                            if not digit in "01234567": not_in_correct_form = True
                
                    if not_in_correct_form:
                        print("You entered in incorrect format\nPlease Enter Again")
                    else:
                        number = int(number)
                        C = number % 2
                        B = (number % 4 - C )// 2
                        A = number // 4

                        computed = True

                        break

            elif base == 16:
                while True:
                    number = input("Please Enter the number you want in base 16:")

                    not_in_correct_form = False
                    
                    if len(number) > 1:
                        print("Please enter only 1 digit")#https://en.wikipedia.org/wiki/Octal#:~:text=Binary%20to%20octal%20conversion%5Bedit,Octal%20to%20hexadecimal%20conversion
                    else:
                        for digit in number:
                            if not digit in "0123456789ABCDEF":
                                not_in_correct_form = True

                    if not_in_correct_form:
                        print("You entered in incorrect format\nPlease Enter Again")
                        break

                    intNumber = int(number)
                        
                    C = intNumber % 2
                    B = (intNumber % 4 - C )// 2
                    A = intNumber // 4

                    computed = True

                    break
            else:
                print("Invalid input\n please enter again!")
                break
                
            if computed:
                print(f"{A = }\n{B = }\n{C = }")

                total = A + B + C

                if total == 3:
                    total = 1
                    carry_out = 1        
                elif total == 2:
                    total = 1
                    carry_out = 0

                print(f"{number = }\n{total = }\n{carry_out = }")

                computed = False

                break

    elif ans == "2":
        print("Thanks for coming!\nSee you again!!")
        break
    else :
        print("Invalid input, please enter again.")
        ans = input("What do you want to do?")
