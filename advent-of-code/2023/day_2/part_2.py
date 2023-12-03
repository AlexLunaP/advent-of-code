file = open('input.txt', 'r')
text = file.readlines()

total_power = 0

for line in text:
    splitted_game = line.split(":")
    game = splitted_game[0].split(" ")
    sets = splitted_game[1].split(";")

    red_max = 1
    green_max = 1
    blue_max = 1

    set_power = 1

    for set in sets:
        subsets = set.split(",")

        for subset in subsets:
            splitted_subsets = subset.split(" ")
            cube_quantity = int(splitted_subsets[1])
            cube_color = splitted_subsets[2].strip("\n")

            if cube_color == "red" and cube_quantity > red_max: 
                red_max = cube_quantity
            if cube_color == "green" and cube_quantity > green_max: 
                green_max = cube_quantity
            if cube_color == "blue" and cube_quantity > blue_max: 
                blue_max = cube_quantity
        
    set_power = red_max * blue_max * green_max
    total_power += set_power

print (total_power)