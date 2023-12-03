file = open('input.txt', 'r')
lines = file.readlines()

total_sum = 0

spelled_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in lines:
    first_digit = ""
    last_digit = ""
    index_digit = {}
    
    for digit in spelled_digits:
        first_index = line.find(digit)
        last_index = line.rfind(digit)

        if first_index != -1:
            index_digit[first_index] = spelled_digits.index(digit)

        if last_index != -1:
            index_digit[last_index] = spelled_digits.index(digit)

    character_index = 0

    for character in line:
        if character.isdigit():
            index_digit[character_index] = character
        character_index += 1
    
    # Search the first and last index
    min_index = float('inf')
    max_index = float('-inf')
    first_number = ""
    last_number = ""

    for character_index, digit in index_digit.items():
            if character_index < min_index:
                min_index = character_index
                first_number = digit
            if character_index > max_index:
                max_index = character_index
                last_number = digit

    total_sum += int(str(first_number) + str(last_number))

print(total_sum)