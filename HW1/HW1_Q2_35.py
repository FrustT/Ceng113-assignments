##########################################################################################
#      Group-35                                                                          #
#        290201099 - Burak ERİNÇ                                                         #    
#        290201082 - Arif Ege ÖNDER                                                      #
#                                                                                        #
##########################################################################################

# get a numerical value from user
num = int(input("Enter a number: "))

# calculate all digits of the number
thousands = num // 1000
hundreds = (num % 1000) // 100
tens = (((num % 1000) % 500) % 100) // 10
ones = (((((num % 1000) % 500) % 100) % 50) % 10) // 1

# defining the error message initially
# so that we can use it again
error_message = "Invalid input, please enter a number between 1-3999"

# error handling for wrong input
if thousands >= 4:
	# cannot be bigger than 3999
	print(error_message)
elif num <= 0:
	# cannot be smaller than 1
	print(error_message)

# if there is no error with the input
# then, calculate the roman numeral
else:

	# this variable will be our final
	# roman numeral
	roman = ""

	# since thousands can not be bigger than 5 
	# we can add "M"s without an if statement
	roman += thousands * "M"

	# we need to check for special 
	# cases for 9s and 4s in roman numerals
	if hundreds >= 5:
		if hundreds == 9:
			# if there is a 9 in hundreds,
			# we need to add a "CM"
			roman += "CM"
		else:
			# if the number given is greater
			# than 500, we need to add the
			# 'five hundred' roman numeral,
			# which is 'D'
			roman += "D"
			# then we need to add the remaining
			# 100's to the final roman number
			roman += (hundreds - 5) * "C"
	elif hundreds == 4:
		# if there is a 4 in hundreds,
		# we need to add a "CD"
		roman += "CD"
	else:
		# if there is no 9 or 4 in hundreds,
		# we need to add the number of hundreds
		# to the roman numeral
		roman += hundreds * "C"

	if tens >= 5:
		if tens == 9:
			# if there is a 9 in tens,
			# we need to add a "XC"
			roman += "XC"
		else:
			# if the number given is greater
			# than 50, we need to add the
			# 'fifty' roman numeral,
			# which is 'L'
			roman += "L"
			# then we need to add the remaining
			# 10's to the final roman number
			roman += (tens - 5) * "X"
	elif tens == 4:
		# if there is a 4 in tens,
		# we need to add a "XL"
		roman += "XL"

	else:
		# if there is no 9 or 4 in tens,
		# we need to add the number of tens
		# to the roman numeral
		roman += tens * "X"
		
	if ones >= 5: 
		if ones == 9:
			# if there is a 9 in ones,
			# we need to add a "IX"
			roman += "IX"
		else:
			# if the number given is greater
			# than 5, we need to add the
			# 'five' roman numeral,
			# which is 'V'
			roman += "V"
			# then we need to add the remaining
			# 1's to the final roman number
			roman += (ones - 5) * "I"

	elif ones == 4:
		# if there is a 4 in ones,
		# we need to add a "IV"
		roman += "IV"

	else:
		# if there is no 9 or 4 in ones,
		# we need to add the number of ones
		# to the roman numeral
		roman += ones * "I"

	# print the final roman numeral
	print(f"Year {num} is represented as {roman} in roman numerals.")
