##########################################################################################
#      Group-35                                                                          #
#        290201099 - Burak ERİNÇ                                                         #    
#        290201082 - Arif Ege ÖNDER                                                      #
#                                                                                        #
##########################################################################################

#We declare our global variables so we can use them later.
not_in_correct_form = False
total = 0
carry_out = 0
computed = False
ans = "0"


#This statement ensures that program keeps running till user enters "2" to exit
while not ans == "2":

    print("Welcome to FullAdder!\n(1) Compute and Display the Outputs\n(2) Exit") 
    ans = input("You choose: ")

    computed = False

    if ans == "1":
        print(f"You have chosen option {ans}")

        #This statement ensures that after calculation executed,User isn't asked to enter a base
        while not computed:
            base = int(input("Which base will you use to enter data lines (base 16/8/2)? "))

            if base == 2:

                #This statement ensures that after calculation executed,User isn't asked to enter a number
                while not computed:
                    number = input("Please enter input:")

                    not_in_correct_form = False


                    for digit in number:

                            #This loop takes each char in string and checks if this char is in string below 
                            # if it is not then it is not in binary 
                            if not digit in "01":
                                print("Your input is not in binary!",end= '')

                                not_in_correct_form = True

                    #This statement ensures that if an invalid input is entered, code below doesn't throw an error
                    if not_in_correct_form is False:
                        
                        #Since the biggest value we can compute is binary 111
                        #This code checks if the number is in acceptable range
                        if len(number) > 3: 
                            print("Please enter a value with max 3 digits!",end= '')

                            not_in_correct_form = True
                                    
                    if not_in_correct_form:
                        print("Please try again!")

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
                    number = input("Please enter input:")

                    not_in_correct_form = False

                    #This loop takes each char in string and checks if this char is in string below 
                    #If it is not then it is not in base 8 
                    for digit in number:

                              
                            if not (digit in "01234567"): 
                                print("Your input is not in base 8.",end='')

                                not_in_correct_form = True
                    
                    #This statement ensures that if an invalid input is entered ,code below doesn't throw an error
                    if not_in_correct_form is False :

                        #Since the biggest value we can compute is binary 111
                        #This code checks if the number is in acceptable range
                        if (len(number) > 1 or int(number) > 7):
                            print(f"Octal {number} cannot be represented with 3 bits!",end='')# https://en.wikipedia.org/wiki/Octal#:~:text=Binary%20to%20octal%20conversion%5Bedit,Octal%20to%20hexadecimal%20conversion

                            not_in_correct_form = True

                    
                    if not_in_correct_form:
                        print("Please try again!")
                    else:
                        number = int(number)
                        C = number % 2
                        B = (number % 4 - C )// 2
                        A = number // 4

                        computed = True


            elif base == 16:

                #This statement ensures that after calculation executed,User isn't asked to enter a number
                while not computed:
                    number = input("Please enter input:").upper()

                    not_in_correct_form = False

                    #This loop takes each char in string and checks if this char is in string below 
                    #If it is not than it is not in base 16
                    for digit in number:

                               
                            if not (digit in "0123456789ABCDEF"): 
                                print("Your input is not in base 16.",end=' ')

                                not_in_correct_form = True
                  
                    #This statement ensures that if an invalid input is entered ,code below doesn't throw an error
                    if not_in_correct_form is False :

                        
                        #Since the biggest value we can compute is 111(binary)
                        #This code checks if the number is in acceptable range
                        if(len(number) > 1 or "0123456789ABCDEF".index(number) > 7):
                            print(f"Hexadecimal {number} can not be represented with 3 bits!",end='')

                            not_in_correct_form = True

                    if not_in_correct_form:
                        print("Please try again!")
                    else:
                        intNumber = int(number)
                            
                        C = intNumber % 2
                        B = (intNumber % 4 - C )// 2
                        A = intNumber // 4

                        computed = True

            #Since previous statements covers all the options,
            #If they are all False then that means input is invalid.
            else:
                print("Invalid input, please enter again.")

            #This statement ensures that computation doesn't executed unnecessarily    
            if computed:
                total = A + B + C

                if total == 3:
                    total = 1
                    carry_out = 1        
                elif total == 2:
                    total = 0
                    carry_out = 1

                print(f"Sum is {total} C_out is {carry_out}")
                

    elif ans == "2":
        print(f"You have chosen option {ans}")

    #Since previous statements covers all the options,
    #If they are all False then that means input is invalid.    
    else :
        print("Invalid input, please enter again.")

print("Byee!!")