import random


# Function read_file() - place your own comments here...  : )
def read_file(filename):
    # List to store information on heroes and villains (character list)
    character_list = []

    # This line will eventually be removed - used for development purposes only.
    # print("In function read_file()")

    # Place your code and comments here

    infile = open(filename, "r")

    index = 0

    # Read first line of file.
    line = infile.readline()

    # While not end of file reached i.e. empty string not returned from readline method.
    while line != "":
        # Get name
        name = line.strip("\n")

        # Read in next line
        line = infile.readline()

        # Get secret_identity
        secret_id = line.strip("\n")

        # Read in next line
        line = infile.readline()

        # Split line into no battles, no won, no lost, etc.
        info_list = line.split()
        is_hero = info_list[0]
        no_battles = int(info_list[1])
        no_won = int(info_list[2])
        no_lost = int(info_list[3])
        no_drawn = int(info_list[4])
        health = int(info_list[5])

        # Create new list to store individual character information
        new_character = [
            name,
            secret_id,
            is_hero,
            no_battles,
            no_won,
            no_lost,
            no_drawn,
            health,
        ]

        # Add new character to character_list (creating a list of lists)
        character_list.append(new_character)

        # Read next line of file.
        line = infile.readline()

    return character_list





# Function display_characters() - place your own comments here...  : )
def display_characters(character_list, display_type):
    if display_type == "list":
        char_list = character_list
    elif display_type == "heroes":
        char_list = [character for character in character_list if character[2] == "h"]
    else:
        char_list = [character for character in character_list if character[2] == "v"]

    heading = (
        f"{'='*50}\n-{' '*3} Character (heroes and villains) Summary{' '*3} -\n{'='*50}"
    )

    print(heading)
    table_head = f"- {'':<20} {'P':^4} {'W':^3} {'L':^3} {'D':^3} {'Health':>5} -"
    print(table_head)
    print("-" * 50)
    for character in char_list:
        (
            name,
            secret_id,
            is_hero,
            no_battles,
            no_won,
            no_lost,
            no_drawn,
            health,
        ) = character
        alignment = "<"

        character_info = f"- {name:{alignment}20} {no_battles:^4} {no_won:^3} {no_lost:^3} {no_drawn:^3} {health:>5} -"
        print(character_info)
        print("-" * 50)
    print("=" * 50)






# Function write_to_file() - place your own comments here...  : )
def write_to_file(filename, character_list):
    with open(filename, "w") as file:
        for char in character_list:
            (
                name,
                secret_id,
                is_hero,
                no_battles,
                no_won,
                no_lost,
                no_drawn,
                health,
            ) = char
            file.write(name + "\n")
            file.write(secret_id + "\n")
            file.write(
                f"{is_hero} {no_battles} {no_won} {no_lost} {no_drawn} {health}\n"
            )






# Function find_character() - place your own comments here...  : )
def find_character(character_list, name):
    ind = 0
    index = -1
    for character in character_list:
        ind += 1
        if character[0] == name:
            index = ind-1     
    return index






# Function add_character() - place your own comments here...  : )
def add_character(character_list, name, secret_id, is_hero):
    Flag = True
    for character in character_list:
        (
            lname,
            secret,
            hero,
            no_battles,
            no_won,
            no_lost,
            no_drawn,
            health,
        ) = character
        if lname == name:
            Flag = False
    if Flag == True:
        character = [name, secret_id, is_hero, 0, 0, 0, 0, 100]
        character_list.append(character)
        write_to_file("new_characters.txt", character_list=character_list)
    return Flag






# Function remove_character() - place your own comments here...  : )
def remove_character(character_list, name):
    result = find_character(name=name,character_list=character_list)
    if result != 1:
        new_character_list = []
        for character in character_list:
                (
                    lname,
                    secret,
                    hero,
                    no_battles,
                    no_won,
                    no_lost,
                    no_drawn,
                    health,
                ) = character
                if lname != name:
                    new_character_list.append(character)
        write_to_file("new_characters.txt",character_list=new_character_list)
        print(f"Successfully removed {name} from character list.")
    else:
        print(f"{name} is not found in characters.")
        






# Function display_highest_battles_won() - place your own comments here...  : )
def display_highest_battles_won(character_list):

    highest_won_character = None
    highest_won = -1
    low_battle = 0

    for character in character_list:
        (   name,
            secret_id,
            is_hero,
            no_battles,
            no_won,
            no_lost,
            no_drawn,
            health,
        ) = character
        if no_won > highest_won or (no_won == highest_won and no_battles < low_battle):
            highest_won_character = character
            highest_won = no_won
            low_battle = no_battles

    if highest_won_character:
        name, _, _, _, no_won, _, _, _ = highest_won_character
        print(f"\nHighest number of battles won => {name} with {no_won} opponents defeated!\n")
    else:
        print("\nDo some battles!\n")







def do_battle(character_list, opponent1_pos, opponent2_pos):

    opponent1 = character_list[opponent1_pos]
    opponent2 = character_list[opponent2_pos]


    opponent1_damage = random.randint(0, 50)
    opponent2_damage = random.randint(0, 50)

    opponent1_health = opponent1[7] - opponent1_damage
    opponent2_health = opponent2[7] - opponent2_damage
    if opponent1_health <0:
        opponent1_health = 0
    if opponent2_health<0:
        opponent2_health = 0
    print(f"{'':<2}> {opponent1[0]} - Damage: {opponent1_damage} - Current health: {opponent1_health}")
    print(f"{'':<2}> {opponent2[0]} - Damage: {opponent2_damage} - Current health: {opponent2_health}")

    opponent1[7] = opponent1_health
    opponent2[7] = opponent2_health    
    write_to_file("new_characters.txt", character_list=character_list)





# Function sort_by_health() - place your own comments here...  : )
def sort_by_health(character_list):
    sorted_list = character_list
    n = len(sorted_list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            health_of_1 = sorted_list[j][7]
            health_of_2 = sorted_list[j + 1][7]
            battles_completed1 = sorted_list[j][3]
            battles_completed2 = sorted_list[j + 1][3]
            if health_of_1 < health_of_2 or (health_of_1 == health_of_2 and battles_completed1 < battles_completed2):
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list
        
    # char_list = sorted(character_list, key=lambda x: x[7], reverse=True)
    # heading = (
    #     f"{'='*50}\n-{' '*3} Character (heroes and villains) Summary{' '*3} -\n{'='*50}"
    # )
    # print(heading)
    # table_head = f"- {'':<20} {'P':^4} {'W':^3} {'L':^3} {'D':^3} {'Health':>5} -"
    # print(table_head)
    # print("-" * 50)
    # for character in char_list:
    #     (
    #         name,
    #         secret_id,
    #         is_hero,
    #         no_of_battles,
    #         no_of_win,
    #         no_of_lost,
    #         no_of_drawn,
    #         health,
    #     ) = character
    #     alignment = "<"

    #     character_details = f"- {name:{alignment}20} {no_of_battles:^4} {no_of_win:^3} {no_of_lost:^3} {no_of_drawn:^3} {health:>5} -"
    #     print(character_details)
    #     print("-" * 50)
    # print("=" * 50)
    
    
    
############################################################################################



display_char = ["list", "heroes", "villains"]
char = read_file("characters.txt")
write_to_file("new_characters.txt",character_list=char)
Game = True




while Game == True:
    character_list = read_file("new_characters.txt")
    display_type = input(
        "\nPlease enter a choice \n [list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: "
    )

    if display_type in display_char:
        display_characters(character_list, display_type)
    elif display_type == "quit":
        Game = False
        write_to_file("new_characters.txt", character_list)
    elif display_type == "search":
        name = input("Please enter name: ")
        result = find_character(character_list, name)
        if result != -1:
            (
                name,
                secret_id,
                is_hero,
                no_battles,
                no_won,
                no_lost,
                no_drawn,
                health,
            ) = character_list[result]
            alignment = ">" if is_hero == "v" else "<"
            print(f"\nAll about {name} --> {'HERO' if is_hero == 'h' else 'VILLAIN'}\n")
            print(f"Secret identity: {secret_id}\n")
            print(f"Battles fought: {no_battles}")
            print(f"> No won: {no_won:>10}")
            print(f"> No lost: {no_lost:>9}")
            print(f"> No drawn: {no_drawn:>8}\n")

            print(f"Current health: {health}%\n")
        else:
            print(f"{name} is not found in character (heroes and villains) list.")

    elif display_type == "reset":
        name = input("\nEnter the name:")
        result = find_character(character_list, name)
        if result != -1:
            character = character_list[result]
            character[7] = 100
            print(f"\nSuccessfully updated {name}'s health to 100\n")
            write_to_file("new_characters.txt", character_list=character_list)
        else:
            print(f"{name} is not found in character (heroes and villains) list.")
            
    elif display_type == "add":
        name = input("\nPlease enter name: ")
        secret_id = input("Please enter secret_identity: ")
        is_hero = input("Is this character a hero or a villain [h|v]? ")
        result = add_character(
            character_list=character_list,
            name=name,
            secret_id=secret_id,
            is_hero=is_hero,
        )
        if result == False:
            print(f"{name} already exists in character list.")
        else:
            print(f"\nSuccessfully added The {name} to character list.\n")
            
    elif display_type == "remove":
        name = input("Please enter name: ")
        result  = find_character(name,character_list)
        if result == -1:
            print(f"{name} is not found in characters.")
        else:
            result = remove_character(character_list,name)
    elif display_type == "high":
        display_highest_battles_won(character_list=character_list)
    elif display_type == "battle":
        first = -1
        second = -1

        while first == -1:
            name1 = input("\nPlease enter opponent one's name: ")
            first_index = find_character(character_list, name1)
            if first_index == -1:
                print(f"\nThe {name1} is not found in character list - please enter another opponent!")
            else:
                first = first_index
                character_list[first_index][3] += 1
        while second == -1:
            name2 = input("\nPlease enter opponent two's name: ")
            second_index = find_character(character_list, name2)
            if second_index == -1:
                print(f"\nThe {name2} is not found in character list - please enter another opponent!")
            else:
                second = second_index
                character_list[second_index][3] += 1
        round = 0
        while round < 1 or round > 5:
            round = int(input("\nPlease enter number of battle rounds: "))
            if round < 1 or round > 5:
                print("\nMust be between 1-5 inclusive.\n")       
        print(f"\n{'':<3}-- Battle --")  
        print(f"\n{name1} versus {name2} - {round} rounds")  
        i = 0
        winner = None
        while i<round:
            print(f"\nRound: {i+1}")
            result = do_battle(character_list=character_list,opponent1_pos=first_index,opponent2_pos=second_index)
            character_list = read_file("new_characters.txt")
            if character_list[first_index][7] == 0 and character_list[second_index][7]!=0:
                print(f"\n{'':<3}-- {character_list[first_index][0]} has died! :( \n")
                winner = character_list[second_index][0]
                i = round
            elif character_list[second_index][7] == 0 and character_list[first_index][7]!=0:
                print(f"\n{'':<3}-- {character_list[second_index][0]} has died! :( \n")
                winner = character_list[first_index][0]
                i = round
            elif character_list[second_index][7] == 0 and character_list[first_index][7] == 0:
                i = round   
            i += 1
        print(f"\n{'':<3}-- End of battle --")
        if winner:
            print(f"{'':<3}** {winner} wins! **")
            if character_list[second_index][7] == 0:
                character_list[first_index][4] += 1
                character_list[second_index][5] += 1
            else:
                character_list[second_index][4] += 1
                character_list[first_index][5] += 1
        else:
            if character_list[first_index][7] == character_list[second_index][7]:
                print(f"{'':<3}The battle ended in a draw!\n")
                character_list[first_index][6] += 1
                character_list[second_index][6] += 1
            elif character_list[first_index][7]<character_list[second_index][7]:
                print(f"{'':<3}** {character_list[second_index][0]} wins! **")
                character_list[second_index][4] += 1
                character_list[first_index][5] += 1
            elif character_list[second_index][7]<character_list[first_index][7]:
                print(f"{'':<3}** {character_list[first_index][0]} wins! **")
                character_list[first_index][4] += 1
                character_list[second_index][5] += 1
        write_to_file("new_characters.txt", character_list=character_list)
    elif display_type == "health":
        result = sort_by_health(character_list)  
        display_characters(character_list=result, display_type="list")  



    else:
        print("Not a valid command - please try again..")

print("\n\n-- Program terminating --\n")
