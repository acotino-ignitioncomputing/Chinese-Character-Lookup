# This file implements a simple CLI tool for adding one or several chinese characters to
# 'radicals.txt' and checking for duplicates.

from constants import RADICAL_FILE

if __name__ == '__main__':
    with RADICAL_FILE.open('r') as file:
        radical_list = [char.strip('\n') for char in file.readlines()]

    print(f"Total {len(radical_list)} radicals.")
    print("Add radicals by entering one or several characters, separated by a single space:")
    character_list = [char for char in input("Input: ").split(' ') if char != '']

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
        print(f"Following provided characters appear in {RADICAL_FILE.name}.")
        for duplicate in duplicate_list:
            print('\t' + duplicate)
    
    if character_list:
        print(f"Append (remaining) {len(character_list)} character(s) to file '{RADICAL_FILE.name}'?? y / n")
        choice = input("Input: ")
    else:
        # Terminate if no characters are left
        choice = 'n'

    # Add remaining characters to file
    if choice == 'y':
        with RADICAL_FILE.open('a') as file:
            for character in character_list:
                file.write(character+'\n')
        print(f" {len(character_list)} character(s) added.")
    else:
        print("Done")
