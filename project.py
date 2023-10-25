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
    if display_type == "list":  # checking display type wanted
        char_list = character_list  # setting the list to new list
    elif display_type == "heroes":
        char_list = [
            character for character in character_list if character[2] == "h"
        ]  # adding the heroes to a new list
    else:
        char_list = [
            character for character in character_list if character[2] == "v"
        ]  # adding the villains to a new list

    heading = f"{'='*50}\n-{' '*3} Character (heroes and villains) Summary{' '*3} -\n{'='*50}"  # heading of the output list

    print(heading)
    table_head = f"- {'':<20} {'P':^4} {'W':^3} {'L':^3} {'D':^3} {'Health':>5} -"  # setting the table head
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
        ) = character  # iterating through the new list items one by one
        alignment = "<"

        character_info = f"- {name:{alignment}20} {no_battles:^4} {no_won:^3} {no_lost:^3} {no_drawn:^3} {health:>5} -"  # assigning chracter name and details to a variable to print
        print(character_info)
        print("-" * 50)  # printing the footer section
    print("=" * 50)


# Function write_to_file() - place your own comments here...  : )
def write_to_file(filename, character_list):
    with open(filename, "w") as file:  # openig the file to write
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
                f"{is_hero} {no_battles} {no_won} {no_lost} {no_drawn} {health}\n"  # writing everything to the file
            )


# Function find_character() - place your own comments here...  : )
def find_character(character_list, name):
    ind = 0  # to determine the index
    index = -1  # if the value is not found it will return -1
    for character in character_list:
        ind += 1  # incrementing the value
        if character[0] == name:
            index = ind - 1
    return index  # retuening the index value


# Function add_character() - place your own comments here...  : )
def add_character(character_list, name, secret_id, is_hero):
    Flag = True  # to check the character is already exist
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
            Flag = False  # setting into false if the character is already exist in the list
    if Flag == True:
        character = [
            name,
            secret_id,
            is_hero,
            0,
            0,
            0,
            0,
            100,
        ]  # the health will be 100 in the initial stage
        character_list.append(character)  # adding the item to the list
        write_to_file(
            "new_characters.txt", character_list=character_list
        )  # saving the updated value
    return Flag  # returning the flag


# Function remove_character() - place your own comments here...  : )
def remove_character(character_list, name):  # function to remove specific character
    new_character_list = []  # creating a list to store the items
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
            new_character_list.append(
                character
            )  # appending the character excluding the selected one
    write_to_file(
        "new_characters.txt", character_list=new_character_list
    )  # saving the updates
    print(f"Successfully removed {name} from character list.")


# Function display_highest_battles_won() - place your own comments here...  : )
def display_highest_battles_won(character_list):
    highest_won_character = None  # a variable to assign the character who won more
    highest_won = -1  # the highest number of wins
    low_battle = 0  # the character with low battle

    for character in character_list:
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
        if no_won > highest_won or (
            no_won == highest_won and no_battles < low_battle
        ):  # checking two conditions
            highest_won_character = character  # assigning the value
            highest_won = no_won
            low_battle = no_battles

    if highest_won_character:
        (
            name,
            _,
            _,
            _,
            no_won,
            _,
            _,
            _,
        ) = highest_won_character  # taking the name and number of victory
        print(
            f"\nHighest number of battles won => {name} with {no_won} opponents defeated!\n"
        )


# function to perform the battle
def do_battle(character_list, opponent1_pos, opponent2_pos):
    opponent1 = character_list[
        opponent1_pos
    ]  # getting the character using the index number
    opponent2 = character_list[opponent2_pos]

    opponent1_damage = random.randint(0, 50)  # taking a random number between 1 an 50
    opponent2_damage = random.randint(0, 50)

    opponent1_health = (
        opponent1[7] - opponent1_damage
    )  # minusing the random number from the character health
    opponent2_health = opponent2[7] - opponent2_damage
    if (
        opponent1_health < 0
    ):  # if the present health is below zero, setting that to zero
        opponent1_health = 0
    if opponent2_health < 0:
        opponent2_health = 0
    print(
        f"{'':<2}> {opponent1[0]} - Damage: {opponent1_damage} - Current health: {opponent1_health}"
    )  # printing the damage and remaining health
    print(
        f"{'':<2}> {opponent2[0]} - Damage: {opponent2_damage} - Current health: {opponent2_health}"
    )

    opponent1[7] = opponent1_health  # assigning the present health of the character
    opponent2[7] = opponent2_health
    write_to_file(
        "new_characters.txt", character_list=character_list
    )  # writing to file


# Function sort_by_health() - place your own comments here...  : )
def sort_by_health(character_list):
    sorted_list = character_list  # creating a new list with the present characters
    n = len(sorted_list)  # taking length of the list
    for i in range(n - 1):  # i loop from the index 0 to the 2nd last element.
        for j in range(
            0, n - i - 1
        ):  # get health and battles fought for the current and next characters
            health_of_1 = sorted_list[j][7]
            health_of_2 = sorted_list[j + 1][7]
            battles_completed1 = sorted_list[j][3]
            battles_completed2 = sorted_list[j + 1][3]
            if health_of_1 < health_of_2 or (
                health_of_1 == health_of_2 and battles_completed1 < battles_completed2
            ):
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j],
                )  # swapping the values
    return sorted_list  # returning the sorted list


############################################################################################


display_char = ["list", "heroes", "villains"]  # to reuse in list function
char = read_file(
    "characters.txt"
)  # reading characters.txt and converting into list format
write_to_file(
    "new_characters.txt", character_list=char
)  # converting and adiing the list to new_character.txt
Game = True  # if this is true, it means the game is on
print("File : wayby001.py")
print("Author : Batman")
print("Email ID : wayby001")
print("This is my own work as defined by the University's Academic Misconduct Policy.")


while Game == True:  # checking the game status
    character_list = read_file("new_characters.txt")  # reading the file to get list
    display_type = input(
        "\nPlease enter a choice \n [list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: "  # An input to take the user command
    )

    if (
        display_type in display_char
    ):  # if the command in the list the function will be called
        display_characters(character_list, display_type)
    elif (
        display_type == "quit"
    ):  # quiting the game and writing the present list into new_characters.txt
        Game = False
        write_to_file("new_characters.txt", character_list)
    elif display_type == "search":
        name = input("Please enter name: ")
        result = find_character(
            character_list, name
        )  # passing the list and name to the function
        if result != -1:  # taking the value based on the returned index
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
            print(
                f"\nAll about {name} --> {'HERO' if is_hero == 'h' else 'VILLAIN'}\n"
            )  # displaying the search details
            print(f"Secret identity: {secret_id}\n")
            print(f"Battles fought: {no_battles}")
            print(f"> No won: {no_won:>10}")
            print(f"> No lost: {no_lost:>9}")
            print(f"> No drawn: {no_drawn:>8}\n")

            print(f"Current health: {health}%\n")
        else:
            print(f"{name} is not found in character (heroes and villains) list.")

    elif display_type == "reset":  # used to reset the health to 100
        name = input("\nEnter the name:")
        result = find_character(character_list, name)
        if result != -1:
            character = character_list[result]
            character[7] = 100
            print(f"\nSuccessfully updated {name}'s health to 100\n")
            write_to_file(
                "new_characters.txt", character_list=character_list
            )  # saving the updates
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
        )  # passing the new user details to the function
        if result == False:
            print(f"{name} already exists in character list.")
        else:
            print(f"\nSuccessfully added The {name} to character list.\n")

    elif display_type == "remove":
        name = input("Please enter name: ")
        result = find_character(
            character_list, name
        )  # checking the input name is present
        if result != -1:  # -1 means that the input name is not exist
            result = remove_character(
                character_list, name
            )  # calling the function to remove the character
        else:
            print(f"{name} is not found in characters.")
    elif display_type == "high":
        display_highest_battles_won(
            character_list=character_list
        )  # to find out the character with highest battle won

    elif display_type == "battle":
        first = -1  # this variable is used validate the first input
        second = -1  # this variable is used validate the second input

        while first == -1:  # if the value is changed the while loop will break
            name1 = input("\nPlease enter opponent one's name: ")
            first_index = find_character(
                character_list, name1
            )  # checking the name exist
            if first_index == -1:
                print(
                    f"\nThe {name1} is not found in character list - please enter another opponent!"
                )
            else:
                first = first_index  # if the first_index is diffrent changing the value of first
                character_list[first_index][
                    3
                ] += 1  # increasing the battle total of oppenent one
        while second == -1:
            name2 = input("\nPlease enter opponent two's name: ")
            second_index = find_character(character_list, name2)
            if second_index == -1:
                print(
                    f"\nThe {name2} is not found in character list - please enter another opponent!"
                )
            else:
                second = second_index
                character_list[second_index][
                    3
                ] += 1  # increasing the battle total of oppenent one
        round = 0  # to determine the round is valid or not
        while round < 1 or round > 5:  # value of round should be between 1 and 5
            round = int(input("\nPlease enter number of battle rounds: "))
            if round < 1 or round > 5:
                print("\nMust be between 1-5 inclusive.\n")
        print(f"\n{'':<3}-- Battle --")  # starting the battle
        print(f"\n{name1} versus {name2} - {round} rounds")
        i = 0  # intializing i
        winner = None  # to assign the winner name
        while i < round:  # to get through every round
            print(f"\nRound: {i+1}")
            result = do_battle(
                character_list=character_list,
                opponent1_pos=first_index,
                opponent2_pos=second_index,
            )  # passing the indexes and list to battle function
            character_list = read_file("new_characters.txt")  # to update the details
            if (
                character_list[first_index][7] == 0
                and character_list[second_index][7] != 0
            ):  # checking any of the characters health is zero
                print(
                    f"\n{'':<3}-- {character_list[first_index][0]} has died! :( \n"
                )  # if it's zero we assume that the character is died
                winner = character_list[second_index][
                    0
                ]  # setting the other character as winner
                i = round  # making the value of i to round to exit from the loop
            elif (
                character_list[second_index][7] == 0
                and character_list[first_index][7] != 0
            ):
                print(f"\n{'':<3}-- {character_list[second_index][0]} has died! :( \n")
                winner = character_list[first_index][0]
                i = round
            elif (
                character_list[second_index][7] == 0
                and character_list[first_index][7] == 0
            ):  # if the both characters are dead we stop the battle
                i = round
            i += 1
        print(f"\n{'':<3}-- End of battle --")
        if winner:  # cheking winner have a valid name
            print(f"{'':<3}** {winner} wins! **")
            if (
                character_list[second_index][7] == 0
            ):  # updation the battle status to the respective characters
                character_list[first_index][4] += 1
                character_list[second_index][5] += 1
            else:
                character_list[second_index][4] += 1
                character_list[first_index][5] += 1
        else:
            if (
                character_list[first_index][7] == character_list[second_index][7]
            ):  # conditions to determine the final winner
                print(f"{'':<3}The battle ended in a draw!\n")
                character_list[first_index][6] += 1  # updating the status
                character_list[second_index][6] += 1
            elif character_list[first_index][7] < character_list[second_index][7]:
                print(f"{'':<3}** {character_list[second_index][0]} wins! **")
                character_list[second_index][4] += 1  # updating the status
                character_list[first_index][5] += 1
            elif character_list[second_index][7] < character_list[first_index][7]:
                print(f"{'':<3}** {character_list[first_index][0]} wins! **")
                character_list[first_index][4] += 1  # updating the status
                character_list[second_index][5] += 1
        write_to_file(
            "new_characters.txt", character_list=character_list
        )  # updating the list
    elif display_type == "health":
        result = sort_by_health(character_list)  # sorting the list
        display_characters(
            character_list=result, display_type="list"
        )  # displaying the list
    else:
        print(
            "Not a valid command - please try again.."
        )  # if the command not in any of these

print("\n\n-- Program terminating --\n")  # terminating the program
