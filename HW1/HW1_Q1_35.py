##########################################################################################
#      Group-35                                                                          #
#        290201099 - Burak ERİNÇ                                                         #    
#        290201082 - Arif Ege ÖNDER                                                      #
#                                                                                        #
##########################################################################################

# asks user to enter an input and capitalizes
# the first letter in order to deny some invalid input
month = input('Enter a month: ').capitalize()

# this statements check if input matches
# the following string values
if month == 'December' or month == 'January' or month == 'February':
    # if input matches with one of the strings in the
    # statement, the following print function is executed
    print(month, 'is in Winter!')

elif month == 'March' or month == 'April' or month == 'May':
    # same thing was applied in following
    # elif statements as well
    print(month, 'is in Spring!')

elif month == 'June' or month == 'July' or month == 'August':
    print(month, 'is in Summer!')

elif month == 'September' or month == 'October' or month == 'November':
    print(month, 'is in Fall!')

# ERROR HANDLING
else:
    # if input doesn't match with any string value
    # that means that input is not a month name
    # so it tells the user it is not a valid month
    print(month, 'is not a valid month.')
	