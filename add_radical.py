# This file implements a simple CLI tool for adding one or several chinese characters to
# 'radicals.txt' and checking for duplicates.

RADICAL_FILE = 'radicals.txt'

if __name__ == '__main__':
    with open(RADICAL_FILE,'r') as file:
        radical_list = [char.strip('\n') for char in file.readlines()]

    print(f"Total {len(radical_list)} radicals.")
    print("Add radicals by entering one or several characters, separated by a single space:")
    character_list = input("Input: ").split(' ')

    duplicate_list = []

    for radical in radical_list:
        if radical in character_list:
            duplicate_list.append(radical)

            # Remove all duplicates
            i = 0
            total_duplicates = character_list.count(radical)
            while i < total_duplicates:
                character_list.remove(radical)
                i = i + 1

    # Report found duplicates
    if duplicate_list:
        print(f"Following provided characters appear in {RADICAL_FILE}.")
        for duplicate in duplicate_list:
            print('\t' + duplicate)

    if character_list:
        print(f"Append remaining characters to file '{RADICAL_FILE}'?? y / n")
        choice = input("Input: ")
    else:
        # Terminate if no characters are left
        choice = 'n'

    # Add remaining characters to file
    if choice == 'y':
        with open(RADICAL_FILE, 'a') as file:
            for character in character_list:
                file.write('\n' + character)
        print(f" {len(character_list)} character(s) added.")
    else:
        print("Done")