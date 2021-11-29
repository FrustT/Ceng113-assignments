##########################################################################################
#      Group-35                                                                          #
#        290201099 - Burak ERİNÇ                                                         #    
#        290201082 - Arif Ege ÖNDER                                                      #
#                                                                                        #
##########################################################################################

# we declare our global variable
# so we can use them later
ans = 0

# this statement ensures that program keeps
# running till user enters "2" to exit
while not ans == 2:
    print("Welcome to FullAdder!\n(1) Compute and Display the Outputs\n(2) Exit") 
    ans = int(input("You choose: "))

    # with this flag, we will check if computation
    # of entered input is necessary
    computed = False

    if ans == 1:
        # this statement ensures that after calculation executed,
        # user isn't asked to enter a base
        while not computed:
            base = int(input("Which base will you use to enter data lines (base 16/8/2)? "))

            if base == 2:

                # this statement ensures that after calculation executed,
                # user isn't asked to enter a number
                while not computed:
                    number = input("Please enter input: ")

                    # with this flag, we will check if the value
                    # entered is worthy enough to compute
                    not_in_correct_form = False

                    # since the biggest value we can compute is binary 111
                    # this code checks if the number is in acceptable range
                    if len(number) > 3: 
                        print("Please enter a value with max 3 digits!")

                        not_in_correct_form = True

                    for digit in number:
                        # This loop takes every digit in string and checks
                        # if this digit is in string below
                        # if not, then it is not in binary
                        if not digit in "01":
                            print("Your input is not in binary!")

                            not_in_correct_form = True

                            # if any found, break out of the loop
                            # since it's not necessary to look after
                            break

                                    
                    # checking if it's not in correct form
                    # if not, then no need to compute
                    if not not_in_correct_form:

                        # since our code needs 3 digit to execute,
                        # this code converts smaller valid unexecutable
                        # inputs to executable one (e.g 11 => 011)
                        while len(number) < 3:
                            number = "0" + number

                        # defining our A, B and C values for base 2
                        A = int(number[0])
                        B = int(number[1])
                        C = int(number[2])

                        # saying it's ready to compute
                        computed = True

            elif base == 8:

                # this statement ensures that after calculation executed,
                # user isn't asked to enter a number
                while not computed:
                    number = input("Please enter input: ")

                    # with this flag, we will check if the value
                    # entered is worthy enough to compute
                    not_in_correct_form = False

                    for digit in number:
                        # This loop takes every digit in string and checks
                        # if this digit is in string below
                        # if not, then it is not in base 8
                        if not (digit in "01234567"): 
                            print("Your input is not in base 8!")

                            not_in_correct_form = True

                            # if any found, break out of the loop
                            # since it's not necessary to look after
                            break

                    if not not_in_correct_form:
                        # since the biggest value we can compute is binary 111
                        # this code checks if the number is in acceptable range
                        if (len(number) > 1 or int(number) > 7):
                            print(f"Octal {number} cannot be represented with 3 bits!")

                            not_in_correct_form = True
                    
                    # checking if it's not in correct form
                    # if not, then no need to compute
                    if not not_in_correct_form:

                        # converting into integer since
                        # we haven't done it at the beginning
                        number = int(number)

                        # defining our A, B and C values for base 8
                        C = number % 2
                        B = (number % 4 - C )// 2
                        A = number // 4

                        # saying it's ready to compute
                        computed = True


            elif base == 16:

                # this statement ensures that after calculation executed,
                # user isn't asked to enter a number
                while not computed:

                    # we are using upper here because in base 16,
                    # value entered could be an hexadecimal letter
                    number = input("Please enter input: ").upper()

                    # with this flag, we will check if the value
                    # entered is worthy enough to compute
                    not_in_correct_form = False

                    # since the biggest value we can compute is binary 111
                    # this code checks if the number is in acceptable range
                    if(len(number) > 1 or "0123456789ABCDEF".index(number) > 7):
                        print(f"Hexadecimal {number} can not be represented with 3 bits!")

                        not_in_correct_form = True

                    for digit in number:
                        # This loop takes every digit in string and checks
                        # if this digit is in string below
                        # if not, then it is not in base 16
                        if not (digit in "0123456789ABCDEF"): 
                            print("Your input is not in base 16!")

                            not_in_correct_form = True

                            # if any found, break out of the loop
                            # since it's not necessary to look after
                            break

                    # checking if it's not in correct form
                    # if not, then no need to compute
                    if not not_in_correct_form:

                        # converting into integer since
                        # we haven't done it at the beginning
                        number = int(number)
                            
                        # defining our A, B and C values for base 16
                        C = number % 2
                        B = (number % 4 - C )// 2
                        A = number // 4

                        # saying it's ready to compute
                        computed = True

            # since previous statements covers all the options,
            # if they are all 'false', then that means input is invalid.
            else:
                print("Invalid input, please enter again.")

            # this statement ensures that
            # computation doesn't executed unnecessarily 
            if computed:
                carry_out = 0

                # find raw sum of bits
                total = A + B + C

                # perform an operation to determine
                # carry out and sum values
                carry_out = total // 2
                total = abs(total - 2)

                # print the result!
                print(f"Sum: {total}\nC_out: {carry_out}")
                

    elif ans == 2:
        print("Byee :(")

    # since previous statements covers all the options,
    # if they are all 'false', then that means input is invalid.  
    else :
        print("Invalid input, please enter again.")
