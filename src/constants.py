from pathlib import Path

CHARACTER_REGISTRY = Path('src/character_registry.pkl')
RADICAL_FILE = Path('src/radicals.txt')

ILLEGAL_VALUES = (
    "abcdefghiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()<>/?;:'[]{}`~-_=+"
)


def check_radical_file():
    # Checks the file RADICAL_FILE for duplicates and illegal values

    with RADICAL_FILE.open('r') as file:
        lines = [char.strip('\n') for char in file.readlines()]

    for line_number, character in enumerate(lines):
        # Only 1 character per line
        if len(character) > 1:
            raise ValueError(f"In file {RADICAL_FILE}, more than 1 character on line {line_number}\n\t{character}.")

        # Check for illegal values
        if character in ILLEGAL_VALUES:
            raise ValueError(f"In file {RADICAL_FILE}, illegal value on line {line_number}\n\t{character}.")

        # Check for duplicates
        if lines.count(character)>1:
            raise Exception(f"In file {RADICAL_FILE}, duplicate values of character {character}.")



if not CHARACTER_REGISTRY.exists():
    print(f"No file {CHARACTER_REGISTRY} in repository. Created one now.")
    empty_dict = {}
    with CHARACTER_REGISTRY.open('wb') as file:
        pickle.dump(empty_dict, file)

if not RADICAL_FILE.exists():
    print(f"No file {RADICAL_FILE} in repository.")
    exit(1)
else:
    check_radical_file()
