file = open('input.txt', 'r')
text = file.readlines()

game_id_sum = 0

max_red = 12
max_green = 13
max_blue = 14

for line in text:
    splitted_game = line.split(":")
    game = splitted_game[0].split(" ")
    sets = splitted_game[1].split(";")

    game_id = int(game[1])

    # Game is valid by default
    valid_game = True
    
    for set in sets:
        red_count = 0
        green_count = 0
        blue_count = 0

        subsets = set.split(",")

        for subset in subsets:
            splitted_subsets = subset.split(" ")
            cube_quantity = splitted_subsets[1]
            cube_color = splitted_subsets[2].strip("\n")

            if cube_color == "red": 
                red_count += int(cube_quantity)
            if cube_color == "green": 
                green_count += int(cube_quantity)
            if cube_color == "blue": 
                blue_count += int(cube_quantity)
        
        if (red_count > max_red) or (green_count > max_green) or (blue_count > max_blue):
            # If a color quantity exceeds max value game is no longer valid
            valid_game = False
            break
    
    if valid_game == True: game_id_sum += game_id

print(game_id_sum)