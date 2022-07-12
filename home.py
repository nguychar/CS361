import time

character_list = ["Albedo", "Aloy", "Amber", "Arataki Itto", "Barbara", "Beidou", "Bennett", "Chongyun", "Diluc", "Diona", "Eula", "Fischl", "Ganyu", "Gorou", "Hu Tao", "Jean", "Kaedehara Kazuha", "Kaeya", "Kamisato Ayaka", "Kamisato Ayato", "Keqing", "Klee", "Kujou Sara", "Kuku Shinobu", "Lisa", "Mona", "Ningguang", "Noelle", "Qiqi", "Raiden Shogun", "Razor", "Rosaria", "Sangonomiya Kokomi", "Sayu", "Shenhe", "Sucrose", "Tartaglia", "Thoma", "Traveler", "Venti", "Xiangling", "Xiao", "Xingqiu", "Xinyan", "Yae Miko", "Yanfei", "Yelan", "Yoimiya", "Yun Jin", "Zhongli"]

def main_menu():
    while True:
        print("")
        print("MAIN MENU:")
        print("1. Characters")
        print("2. Inventory")
        print("3. Artifact Quality")
        print("4. Help")
        print("5. Exit")
        print("")
        print("Please input the number of your selection, then press ENTER.")
        user_input = input()
        if user_input == "1":
            return "character_menu"
        if user_input == "2":
            return "inventory_menu"
        if user_input == "3":
            return "quality_menu"
        if user_input == "4":
            return "main_help"
        if user_input == "5":
            return "exit"
        print("")
        print("Invalid input. Please try again.")

def character_menu():
    while True:
        print("")
        print("CHARACTER MENU:")
        print("1. View All Characters")
        print("2. View Your Characters")
        print("3. Add Character to Collection")
        print("4. Remove Character from Collection")
        print("5. Help")
        print("6. Return to Main Menu")
        print("7. Exit")
        print("")
        print("Please input the number of your selection, then press ENTER.")
        user_input = input()
        if user_input == "1":
            print("")
            print("CHARACTER LIST:")
            print(*character_list, sep = ", ")
            print("")
            input("Press ENTER to return to the previous menu.")
            return "character_menu"
        if user_input == "2":
            print("")
            print("YOUR CHARACTERS:")
            with open("character_save.txt", "r") as file:
                characters = file.read()
            characters = characters.split()
            characters.sort()
            for character in characters:
                print(character)
            print("")
            input("Press ENTER to return to the previous menu.")
            return "character_menu"
        if user_input == "3":
            with open("character_save.txt", "r") as file:
                characters = file.read()
            characters = characters.split()
            while True:
                print("")
                print("Please type the name of the character you wish to add, then press ENTER.")
                print("If you wish to cancel, type 'CANCEL' and press ENTER.")
                user_input = input()
                if user_input in character_list:
                    if user_input not in characters:
                        print("")
                        print("Are you sure you wish to add " + user_input + " to your collection?")
                        print("Please type 1 to confirm or 2 to cancel, then press ENTER.")
                        confirm = input()
                        if confirm == "1":
                            with open("character_save.txt", "a") as file:
                                file.write(str(user_input) + "\n")
                            print("")
                            print(user_input + " was added to your collection!")
                            return "character_menu"
                        elif confirm == "2":
                            return "character_menu"
                        else:
                            print("")
                            print("Invalid input. Please try again.")
                    else:
                        print("")
                        print("Character already exists in collection. Please try again.")
                elif user_input == "CANCEL":
                    return "character_menu"
                else:
                    print("")
                    print("Invalid input. Please try again.")
        if user_input == "4":
            with open("character_save.txt", "r") as file:
                characters = file.read()
            characters = characters.split()
            while True:
                print("")
                print("Please type the name of the character you wish to remove, then press ENTER.")
                print("If you wish to cancel, type 'CANCEL' and press ENTER.")
                user_input = input()
                if user_input in character_list:
                    if user_input in characters:
                        print("")
                        print("Are you sure you wish to remove " + user_input + " from your collection?")
                        print("Please type 1 to confirm or 2 to cancel, then press ENTER.")
                        confirm = input()
                        if confirm == "1":
                            characters.remove(user_input)
                            with open("character_save.txt", "w") as file:
                                for character in characters:
                                    file.write(str(character) + "\n")
                            print("")
                            print(user_input + " was removed from your collection!")
                            return "character_menu"
                        elif confirm == "2":
                            return "character_menu"
                        else:
                            print("")
                            print("Invalid input. Please try again.")
                    else:
                        print("")
                        print("Character does not exist in your collection. Please try again.")
                elif user_input == "CANCEL":
                    return "character_menu"
                else:
                    print("")
                    print("Invalid input. Please try again.")
        if user_input == "5":
            return "character_help"
        if user_input == "6":
            return "main_menu"
        if user_input == "7":
            return "exit"
        print("")
        print("Invalid input. Please try again.")

def inventory_menu():
    while True:
        print("")
        print("INVENTORY MENU:")
        print("1. View All Artifacts")
        print("2. Add Artifact to Collection")
        print("3. Remove Artifact from Collection")
        print("4. Help")
        print("5. Return to Main Menu")
        print("6. Exit")
        print("")
        print("Please input the number of your selection, then press ENTER.")
        user_input = input()
        if user_input == "1":
            print("")
            print("YOUR ARTIFACTS:")
            with open("artifact_save.txt", "r") as file:
                artifacts = file.read()
            artifacts = artifacts.split()
            quantity = len(artifacts) // 10
            counter = 0
            while counter < quantity:
                buffer = 10 * counter
                print("Artifact Number:", counter + 1)
                print("Artifact Type: " + artifacts[buffer + 0])
                print("Artifact Main Stat: " + artifacts[buffer + 1])
                print(artifacts[buffer + 2] + ": " + artifacts[buffer + 3])
                print(artifacts[buffer + 4] + ": " + artifacts[buffer + 5])
                print(artifacts[buffer + 6] + ": " + artifacts[buffer + 7])
                print(artifacts[buffer + 8] + ": " + artifacts[buffer + 9])
                counter += 1
                print("")
            input("Press ENTER to return to the previous menu.")
            return "inventory_menu"
        if user_input == "2":
            new_artifact = []
            artifact_type = artifact_type_helper()
            new_artifact.append(artifact_type)
            new_artifact.append(artifact_main_stat_helper(artifact_type))
            for counter in range(0, 4):
                substat_type = artifact_substat_helper()
                new_artifact.append(substat_type)
                new_artifact.append(artifact_substat_value_helper(substat_type))
            print("")
            print("Are you sure you wish to add the following artifact?")
            print("")
            print("Artifact Type: " + new_artifact[0])
            print("Artifact Main Stat: " + new_artifact[1])
            print(new_artifact[2] + ": " + new_artifact[3])
            print(new_artifact[4] + ": " + new_artifact[5])
            print(new_artifact[6] + ": " + new_artifact[7])
            print(new_artifact[8] + ": " + new_artifact[9])
            print("")
            print("Please type 1 to confirm or 2 to cancel, then press ENTER.")
            confirm = input()
            if confirm == "1":
                with open("artifact_save.txt", "a") as file:
                    for value in new_artifact:
                        file.write(str(value) + "\n")
                print("")
                print("The artifact was added to your collection!")
                return "inventory_menu"
            elif confirm == "2":
                return "inventory_menu"
            else:
                print("")
                print("Invalid input. Please try again.")
        if user_input == "3":
            while True:
                print("")
                print("YOUR ARTIFACTS:")
                with open("artifact_save.txt", "r") as file:
                    artifacts = file.read()
                artifacts = artifacts.split()
                quantity = len(artifacts) // 10
                counter = 0
                while counter < quantity:
                    buffer = 10 * counter
                    print("Artifact Number:", counter + 1)
                    print("Artifact Type: " + artifacts[buffer + 0])
                    print("Artifact Main Stat: " + artifacts[buffer + 1])
                    print(artifacts[buffer + 2] + ": " + artifacts[buffer + 3])
                    print(artifacts[buffer + 4] + ": " + artifacts[buffer + 5])
                    print(artifacts[buffer + 6] + ": " + artifacts[buffer + 7])
                    print(artifacts[buffer + 8] + ": " + artifacts[buffer + 9])
                    counter += 1
                    print("")
                print("Please input the number of the artifact you wish to remove, then press ENTER.")
                print("If you do not wish to remove any artifacts, make any other input and/or press ENTER to return to the previous menu.")
                user_input = input()
                if user_input.isnumeric() is True:
                    if int(user_input) % 1 == 0 and int(user_input) <= quantity:
                        buffer = 10 * (int(user_input) - 1)
                        print("")
                        print("Are you sure you wish to remove the following artifact from your collection?")
                        print("")
                        print("Artifact Number:", int(user_input))
                        print("Artifact Type: " + artifacts[buffer + 0])
                        print("Artifact Main Stat: " + artifacts[buffer + 1])
                        print(artifacts[buffer + 2] + ": " + artifacts[buffer + 3])
                        print(artifacts[buffer + 4] + ": " + artifacts[buffer + 5])
                        print(artifacts[buffer + 6] + ": " + artifacts[buffer + 7])
                        print(artifacts[buffer + 8] + ": " + artifacts[buffer + 9])
                        print("")
                        print("Please type 1 to confirm or 2 to cancel, then press ENTER.")
                        confirm = input()
                        if confirm == "1":
                            for counter in range(1, 11):
                                artifacts.pop((10 * int(user_input)) - counter)
                            with open("artifact_save.txt", "w") as file:
                                for value in artifacts:
                                    file.write(str(value) + "\n")
                            print("")
                            print("The artifact was removed from your collection!")
                            return "inventory_menu"
                        elif confirm == "2":
                            return "inventory_menu"
                        else:
                            print("")
                            print("Invalid input. Please try again.")
                return "inventory_menu"
        if user_input == "4":
            return "artifact_help"
        if user_input == "5":
            return "main_menu"
        if user_input == "6":
            return "exit"
        print("")
        print("Invalid input. Please try again.")
        print("")

def quality_menu():
    while True:
        print("")
        print("ARTIFACT QUALITY MENU:")
        print("1. View All Artifacts")
        print("2. Evaluate an Artifact")
        print("3. Advanced Options")
        print("4. Help")
        print("5. Return to Main Menu")
        print("6. Exit")
        print("")
        print("Try out my Advanced Options if you wish to select your own criteria for artifact evaluation!")
        print("")
        print("Please input the number of your selection, then press ENTER.")
        user_input = input()
        if user_input == "1":
            print("")
            print("YOUR ARTIFACTS:")
            with open("artifact_save.txt", "r") as file:
                artifacts = file.read()
            artifacts = artifacts.split()
            print(artifacts)
            quantity = len(artifacts) // 10
            counter = 0
            while counter < quantity:
                buffer = 10 * counter
                print("Artifact Number:", counter + 1)
                print("Artifact Type: " + artifacts[buffer + 0])
                print("Artifact Main Stat: " + artifacts[buffer + 1])
                print(artifacts[buffer + 2] + ": " + artifacts[buffer + 3])
                print(artifacts[buffer + 4] + ": " + artifacts[buffer + 5])
                print(artifacts[buffer + 6] + ": " + artifacts[buffer + 7])
                print(artifacts[buffer + 8] + ": " + artifacts[buffer + 9])
                counter += 1
                print("")
            input("Press ENTER to return to the previous menu.")
            return "quality_menu"
        if user_input == "2":
            while True:
                print("")
                print("YOUR ARTIFACTS:")
                with open("artifact_save.txt", "r") as file:
                    artifacts = file.read()
                artifacts = artifacts.split()
                quantity = len(artifacts) // 10
                counter = 0
                while counter < quantity:
                    buffer = 10 * counter
                    print("Artifact Number:", counter + 1)
                    print("Artifact Type: " + artifacts[buffer + 0])
                    print("Artifact Main Stat: " + artifacts[buffer + 1])
                    print(artifacts[buffer + 2] + ": " + artifacts[buffer + 3])
                    print(artifacts[buffer + 4] + ": " + artifacts[buffer + 5])
                    print(artifacts[buffer + 6] + ": " + artifacts[buffer + 7])
                    print(artifacts[buffer + 8] + ": " + artifacts[buffer + 9])
                    counter += 1
                    print("")
                print("Please input the number of the artifact you wish to evaluate, then press ENTER.")
                print("If you do not wish to evaluate an artifact, make any other input and/or press ENTER to return to the previous menu.")
                user_input = input()
                if user_input.isnumeric() is True:
                    if int(user_input) % 1 == 0 and int(user_input) <= quantity:
                        buffer = 10 * (int(user_input) - 1)
                        print("")
                        print("Are you sure you wish to evaluate the following artifact?")
                        print("")
                        print("Artifact Number:", int(user_input))
                        print("Artifact Type: " + artifacts[buffer + 0])
                        print("Artifact Main Stat: " + artifacts[buffer + 1])
                        print(artifacts[buffer + 2] + ": " + artifacts[buffer + 3])
                        print(artifacts[buffer + 4] + ": " + artifacts[buffer + 5])
                        print(artifacts[buffer + 6] + ": " + artifacts[buffer + 7])
                        print(artifacts[buffer + 8] + ": " + artifacts[buffer + 9])
                        print("")
                        print("Please type 1 to confirm or 2 to cancel, then press ENTER.")
                        confirm = input()
                        if confirm == "1":
                            with open("evaluator_data.txt", "w") as file:
                                for counter in range(0, 10):
                                    file.write(str(artifacts[buffer + counter]) + "\n")
                            print("")
                            print("Please hold while the evaluator works its magic.")
                            print("")
                            time.sleep(10)
                            input("Done! Press ENTER to continue.")
                            print("")
                            with open("evaluator_data.txt", "r") as file:
                                evaluation = file.read()
                            print("The artifact has " + evaluation + "%" + " stat efficiency.")
                            print("")
                            input("Press ENTER to return to the previous menu.")
                            return "quality_menu"
                        elif confirm == "2":
                            return "quality_menu"
                        else:
                            print("")
                            print("Invalid input. Please try again.")
                return "quality_menu"
        if user_input == "3":
            print("")
            print("Welcome to Advanced Options!")
            print("")
            print("Here you will be able to select a substat type, then change the evaluation modifier for that particular substat.")
            print("The modifier represents the weight which will be given to that particular substat.")
            print("The default weight of every substat is 1. It is recommended to utilize values between 0 and 2.")
            print("")
            input("Press ENTER to continue.")
            substat_type = quality_substat_helper()
            substat_modifier = quality_substat_value_helper(substat_type)
            print("")
            print("You have modified the weight of " + substat_type + " to " + str(substat_modifier) + ".")
            print("")
            input("Press ENTER to continue.")
            return "quality_menu"
        if user_input == "4":
            return "quality_help"
        if user_input == "5":
            return "main_menu"
        if user_input == "6":
            return "exit"
        print("")
        print("Invalid input. Please try again.")
        print("")

def main_help():
    print("")
    print("HELP TOPICS:")
    print("1. Characters allows you to view all playable characters and select characters you wish to add to your collection.")
    print("2. Inventory allows you to fill your personal inventory with artifacts.")
    print("3. Artifact Quality allows you to check the quality of your artifacts via my personal algorithm or one of your own choosing.")
    print("")
    input("Press ENTER to return to the previous menu.")
    return "main_menu"

def character_help():
    print("")
    print("HELP TOPICS:")
    print("1. View All Characters allows you to see all the characters available for adding to your collection.")
    print("2. View Your Characters allows you to look at your own personal collection of characters.")
    print("3. Add Character to Collection allows you to add a character to your collection.")
    print("4. Remove Character from Collection allows you to remove a specific character from your collection.")
    print("")
    input("Press ENTER to return to the previous menu.")
    return "character_menu"

def artifact_help():
    print("")
    print("HELP TOPICS:")
    print("1. View All Artifacts allows you to see all the artifacts in your own personal collection.")
    print("2. Add Artifact to Collection allows you to add a new artifact to your collection.")
    print("3. Remove Artifact from Collection allows you to remove an existing artifact from your collection.")
    print("4. Stat abbreviations are as follows: HP (Hit Points), ATK (Attack), DEF (Defense), EM (Elemental Mastery), ER (Energy Recharge), CR (Critical Hit Rate), CD (Critical Hit Damage).")
    print("")
    input("Press ENTER to return to the previous menu.")
    return "inventory_menu"

def quality_help():
    print("")
    print("HELP TOPICS:")
    print("1. View All Artifacts allows you to see all the artifacts in your own personal collection.")
    print("2. Evaluate an Artifact allows you to evaluate any in your collection. The scoring system is percentage-based and reflects the stat-efficiency of your artifact compared to a perfect artifact with 9 max substat rolls.")
    print("3. Advanced Options allows you to set your own criteria for artifact evaluation.")
    print("4. Stat abbreviations are as follows: HP (Hit Points), ATK (Attack), DEF (Defense), EM (Elemental Mastery), ER (Energy Recharge), CR (Critical Hit Rate), CD (Critical Hit Damage).")
    print("")
    input("Press ENTER to return to the previous menu.")
    return "quality_menu"

def artifact_type_helper():
    print("")
    while True:
        print("ARTIFACT TYPES:")
        print("1. Flower")
        print("2. Plume")
        print("3. Sands")
        print("4. Goblet")
        print("5. Circlet")
        print("")
        print("Please input the number of the artifact type you wish to add, then press ENTER.")
        user_input = input()
        if user_input == "1":
            return "Flower"
        if user_input == "2":
            return "Plume"
        if user_input == "3":
            return "Sands"
        if user_input == "4":
            return "Goblet"
        if user_input == "5":
            return "Circlet"
        print("")
        print("Invalid input. Please try again.")
        print("")

def artifact_main_stat_helper(artifact_type):
    print("")
    if artifact_type == "Flower":
        return "HP"
    if artifact_type == "Plume":
        return "ATK"
    if artifact_type == "Sands":
        while True:
            print("MAIN STAT TYPES:")
            print("1. HP%")
            print("2. ATK%")
            print("3. DEF%")
            print("4. EM")
            print("5. ER%")
            print("")
            print("Please input the number of the artifact main stat you wish to add, then press ENTER.")
            user_input = input()
            if user_input == "1":
                return "HP%"
            if user_input == "2":
                return "ATK%"
            if user_input == "3":
                return "DEF%"
            if user_input == "4":
                return "EM"
            if user_input == "5":
                return "ER%"
            print("")
            print("Invalid input. Please try again.")
            print("")
    if artifact_type == "Goblet":
        while True:
            print("MAIN STAT TYPES:")
            print("1. HP%")
            print("2. ATK%")
            print("3. DEF%")
            print("4. EM")
            print("5. ER%")
            print("6. Anemo")
            print("7. Cryo")
            print("8. Electro")
            print("9. Geo")
            print("10. Hydro")
            print("11. Pyro")
            print("12. Physical")
            print("")
            print("Please input the number of the artifact main stat you wish to add, then press ENTER.")
            user_input = input()
            if user_input == "1":
                return "HP%"
            if user_input == "2":
                return "ATK%"
            if user_input == "3":
                return "DEF%"
            if user_input == "4":
                return "EM"
            if user_input == "5":
                return "ER%"
            if user_input == "6":
                return "Anemo"
            if user_input == "7":
                return "Cryo"
            if user_input == "8":
                return "Electro"
            if user_input == "9":
                return "Geo"
            if user_input == "10":
                return "Hydro"
            if user_input == "11":
                return "Pyro"
            if user_input == "12":
                return "Physical"
            print("")
            print("Invalid input. Please try again.")
            print("")
    if artifact_type == "Circlet":
        while True:
            print("MAIN STAT TYPES:")
            print("1. HP%")
            print("2. ATK%")
            print("3. DEF%")
            print("4. EM")
            print("5. CRIT Rate")
            print("6. CRIT DMG")
            print("7. Healing")
            print("")
            print("Please input the number of the artifact main stat you wish to add, then press ENTER.")
            user_input = input()
            if user_input == "1":
                return "HP%"
            if user_input == "2":
                return "ATK%"
            if user_input == "3":
                return "DEF%"
            if user_input == "4":
                return "EM"
            if user_input == "5":
                return "CR"
            if user_input == "6":
                return "CD"
            if user_input == "7":
                return "Healing"
            print("")
            print("Invalid input. Please try again.")
            print("")

def artifact_substat_helper():
    print("")
    while True:
        print("SUBSTAT TYPES:")
        print("1. HP")
        print("2. ATK")
        print("3. DEF")
        print("4. HP%")
        print("5. ATK%")
        print("6. DEF%")
        print("7. EM")
        print("8. ER%")
        print("9. CRIT Rate")
        print("10. CRIT DMG")
        print("")
        print("Please input the number of the artifact substat you wish to add, then press ENTER.")
        user_input = input()
        if user_input == "1":
            return "HP"
        if user_input == "2":
            return "ATK"
        if user_input == "3":
            return "DEF"
        if user_input == "4":
            return "HP%"
        if user_input == "5":
            return "ATK%"
        if user_input == "6":
            return "DEF%"
        if user_input == "7":
            return "EM"
        if user_input == "8":
            return "ER%"
        if user_input == "9":
            return "CR"
        if user_input == "10":
            return "CD"
        print("")
        print("Invalid input. Please try again.")
        print("")

def artifact_substat_value_helper(substat_type):
    print("")
    print("Please input the substat value associated with the substat " + substat_type + ", then press ENTER.")
    return input()

def quality_substat_helper():
    print("")
    while True:
        print("SUBSTAT TYPES:")
        print("1. HP")
        print("2. ATK")
        print("3. DEF")
        print("4. HP%")
        print("5. ATK%")
        print("6. DEF%")
        print("7. EM")
        print("8. ER%")
        print("9. CRIT Rate")
        print("10. CRIT DMG")
        print("")
        print("Please input the number of the artifact substat for which you wish to modify the evaluation criteria, then press ENTER.")
        user_input = input()
        if user_input == "1":
            return "HP"
        if user_input == "2":
            return "ATK"
        if user_input == "3":
            return "DEF"
        if user_input == "4":
            return "HP%"
        if user_input == "5":
            return "ATK%"
        if user_input == "6":
            return "DEF%"
        if user_input == "7":
            return "EM"
        if user_input == "8":
            return "ER%"
        if user_input == "9":
            return "CR"
        if user_input == "10":
            return "CD"
        print("")
        print("Invalid input. Please try again.")
        print("")

def quality_substat_value_helper(substat_type):
    print("")
    print("Please input the weight associated with the substat " + substat_type + ", then press ENTER.")
    return input()

print("")
print("Welcome to my program!")

current = "main_menu"

while True:
    if current == "main_menu":
        current = main_menu()
    if current == "character_menu":
        current = character_menu()
    if current == "inventory_menu":
        current = inventory_menu()
    if current == "quality_menu":
        current = quality_menu()
    if current == "main_help":
        current = main_help()
    if current == "character_help":
        current = character_help()
    if current == "artifact_help":
        current = artifact_help()
    if current == "quality_help":
        current = quality_help()
    if current == "exit":
        print("")
        print("Thank you for using my program!")
        print("")
        exit()
