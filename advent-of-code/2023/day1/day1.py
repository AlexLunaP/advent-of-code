
# Using readlines()
file = open('input.txt', 'r')
lines = file.readlines()


first_digit = ""
last_digit = ""
total_sum = 0
test = "zeroowowowo"

digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# Strips the newline character
for line in lines:
    first_digit = ""
    last_digit = ""

    """ for digit in digits:
        index = line.find(digit) """

    for character in line:
        if character.isdigit() and first_digit == "": 
            first_digit = character
            last_digit = character

        elif character.isdigit() and first_digit != "": 
            last_digit = character
    
    total_sum += int(str(first_digit) + str(last_digit))


print(total_sum)