import pickle

from constants import CHARACTER_REGISTRY, RADICAL_FILE

EXIT_CHAR = 'q'
FLUSH_CHAR = 'f'

def append_registry(character: str , character_position: int):
    # Load dict
    with CHARACTER_REGISTRY.open('rb') as file:
        char_registry_dict = pickle.load(file)

    # Append dict
    if character_position in char_registry_dict.keys():
        char_registry_dict[character_position].append(character)
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
    print(f"Register the character by typing '{FLUSH_CHAR}'.")

    character = input("Character: ")

    print("Now, providing radicals ...")
    radicals_of_character = []
    radical = ' '
    character_position = 0

    while radical != EXIT_CHAR and radical != '':
        radical = input(character + ' '.join(radicals_of_character) + ' : ')

        if radical == FLUSH_CHAR:
            append_registry(character, character_position)
            radical = EXIT_CHAR
        elif radical in radical_list:
            exponent = radical_list.index(radical)
            character_position += 2**exponent
            radicals_of_character.append(radical)
        elif radical != EXIT_CHAR and radical != '':
            print(f"{radical} not in file '{RADICAL_FILE.name}'.")


    print("Done")



