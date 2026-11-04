import pickle

from constants import CHARACTER_REGISTRY, RADICAL_FILE

EXIT_CHAR = 'q'
FLUSH_CHAR = 'f'
REMOVE_CHAR = 'r'

def append_registry(character: str , radicals_of_character, radical_list):
    # Load dict
    with CHARACTER_REGISTRY.open('rb') as file:
        char_registry_dict = pickle.load(file)
    
    # Compute character_position based on provided list of radicals
    character_position = 0
    for radical in radicals_of_character:
        exponent = radical_list.index(radical)
        character_position += 2**exponent
    
    # Append dict
    if character_position in char_registry_dict.keys():
        if character not in char_registry_dict[character_position]:
            char_registry_dict[character_position].append(character)
        else:
            print(f"Character {character} already registered")
    else:
        char_registry_dict[character_position] = [character]

    # Store new dict
    with CHARACTER_REGISTRY.open('wb') as file:
        pickle.dump(char_registry_dict, file)

if __name__ == '__main__':

    with RADICAL_FILE.open('r') as file:
        radical_list = [char.strip('\n') for char in file.readlines()]

    print("Add character to character_registry by first providing the character and then its radicals.")
    print(f"Quit by providing '{EXIT_CHAR}' or empty input.")
    print(f"Remove last radical by typing '{REMOVE_CHAR}'.")
    print(f"Register the character by typing '{FLUSH_CHAR}'.")

    character = input("Character: ")

    print("Now, providing radicals ...")
    radicals_of_character = []
    radical = ' '
    character_position = 0

    while radical != EXIT_CHAR and radical != '':
        radical = input(character + ' '.join(radicals_of_character) + ' : ')

        if radical == FLUSH_CHAR:
            append_registry(character, radicals_of_character, radical_list)
            radical = EXIT_CHAR
        elif radical == REMOVE_CHAR:
            radicals_of_character.pop(-1)
        elif radical in radical_list:
            radicals_of_character.append(radical)
        elif radical != EXIT_CHAR and radical != '':
            print(f"{radical} not in file '{RADICAL_FILE.name}'.")


    print("Done")



