welcome_text ="Welcome to FullAdder!"
flag = True
not_in_correct_form = False
total = 0
carry_out = 0
computed = False
ans = "0"

print(f"{welcome_text}\n"+'_'* len(welcome_text))

#This statement ensures that program keeps running till user enters "2" to exit
while not ans == "2":
    print("(1) Compute and Display the Outputs\n(2) Exit") 
    ans = input("What do you want to do?")

    computed = False

    if ans == "1":
        print("Lets compute!!!")

        #This statement ensures that after calculation executed,User isn't asked to enter a base
        while not computed:
            base = int(input("Which base you will enter? (2, 8, 16)"))

            if base == 2:

                #This statement ensures that after calculation executed,User isn't asked to enter a number
                while not computed:
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

                        #Since our code needs 3 digit to execute,
                        #This code converts smaller valid unexecutable inputs to executable one (e.g 11 => 011)
                        while len(number) < 3:
                            number = "0" + number

                        A = int(number[0])
                        B = int(number[1])
                        C = int(number[2])

                        computed = True


            elif base == 8:

                #This statement ensures that after calculation executed,User isn't asked to enter a number
                while not computed:
                    number = input("Please Enter the number you want in base 8:")

                    not_in_correct_form = False ######################BURAYA BU KODU ANLATACAK BİR COMMENT YAZALIM MI ?

                    #Checks if input is in base 8
                    for digit in number:

                            #This loop takes each char in string and checks if this char is in string below 
                            # if it is not than it is not in base 8   
                            if not (digit in "01234567"): 
                                print("Your input is not in base 8")

                                not_in_correct_form = True
                    
                    #This statement ensures that if an invalid input is entered ,code below doesn't throw an error
                    if not_in_correct_form is False :

                        #Since biggest value we can cumpute is binary 111
                        #This code checks if the number is in acceptable range
                        if (len(number) > 1 or int(number) > 7) and not_in_correct_form is False:
                            print("Number you entered needs more than 3 bits to represent in binary.")# https://en.wikipedia.org/wiki/Octal#:~:text=Binary%20to%20octal%20conversion%5Bedit,Octal%20to%20hexadecimal%20conversion

                            not_in_correct_form = True

                    
                        if not_in_correct_form:
                            print("You entered in incorrect format\nPlease Enter Again")
                        else:
                            number = int(number)
                            C = number % 2
                            B = (number % 4 - C )// 2
                            A = number // 4

                            computed = True


            elif base == 16:

                #This statement ensures that after calculation executed,User isn't asked to enter a number
                while not computed:
                    number = input("Please Enter the number you want in base 16:").upper()

                    not_in_correct_form = False

                    #Checks if input is in base 16
                    for digit in number:

                            #This loop takes each char in string and checks if this char is in string below 
                            #If it is not than it is not in base 16   
                            if not (digit in "0123456789ABCDEF"): 
                                print("Your input is not in base 16")

                                not_in_correct_form = True
                  
                    #This statement ensures that if an invalid input is entered ,code below doesn't throw an error
                    if not_in_correct_form is False :

                        """
                        #Since bigger value than 7 is not computeable (https://en.wikipedia.org/wiki/Octal#:~:text=Binary%20to%20octal%20conversion%5Bedit,Octal%20to%20hexadecimal%20conversion)
                        #We can check if input is bigger than 7 in base 16
                                                                                Bu iki commentten birini seçemedim
                        #Since biggest value we can cumpute is binary 111
                        #This code checks if the number is in acceptable range      """
                        if(len(number) > 1 or "0123456789ABCDEF".index(number) > 7):
                            print("Number you entered needs more than 3 bits to represent in binary.")

                            not_in_correct_form = True

                    if not_in_correct_form:
                        print("You entered in incorrect format\nPlease Enter Again")
                    else:
                        intNumber = int(number)
                            
                        C = intNumber % 2
                        B = (intNumber % 4 - C )// 2
                        A = intNumber // 4

                        computed = True

            #Since previous statements covers all the options,
            #If they are all False then that means input is invalid.
            else:
                print("Invalid input\nPlease enter again!")

            #This statement ensures that computation doesn't executed unneccasserily    
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
                input("Press enter to go back to menu.")
                
                #This line is required to for healthy loops (?????????daha iyi comment yazılabilir)
                #computed = False # BU KODU ÇIKARDIM

    elif ans == "2":
        print("You have chosen exit.")

    #Since previous statements covers all the options,
    #If they are all False then that means input is invalid.    
    else :
        print("Invalid input, please enter again.")

print("Thanks for coming!\nSee you again!!")