import pickle

from constants import CHARACTER_REGISTRY, RADICAL_FILE

EXIT_CHAR = 'q'
REMOVE_CHAR = 'r'

def _compute_position(radicals_of_character: list, radical_list):
    character_position = 0
    for radical in radicals_of_character:
        exponent = radical_list.index(radical)
        character_position += 2**exponent
    
    return character_position

def _position_contained(x: int, y: int) -> bool:
    # Returns True if all 1-bits in x are also in y.
    # This implies that the radicals associated with x are present
    # in the characters at key y of the CHARACTER_REGISTRY.
    
    # Note: if x is a power of 2 and has a coinciding 1-bit with y, then
    # (y-x) has 1 less 1-bit than y. If x has a 1-bit at a position
    # where y has a 0-bit, then the left-part sequence 10...0
    # is replaced by 01...1, such that (y-x) has equal or more
    # 1-bits than y.
    # Conclusion: x is contained in y iff number of 1-bits in (y-x) equal
    # (number of 1-bits in y) - (number of 1-bits in x).
    
    if x > y:
        return False
        
    n_1_bits_x = x.bit_count()
    n_1_bits_y = y.bit_count()
    
    if n_1_bits_x > n_1_bits_y:
        return False
    
    n_1_bits_substraction = (y-x).bit_count()
    
    return n_1_bits_substraction == n_1_bits_y - n_1_bits_x
    
if __name__ == '__main__':
    # Get list of radicals
    with RADICAL_FILE.open('r') as file:
        radical_list = [char.strip('\n') for char in file.readlines()]
    
    # Load character_registry as dict
    with CHARACTER_REGISTRY.open('rb') as file:
        char_registry_dict = pickle.load(file)
        
    print("Look up a character in the character_registry by providing radicals")
    print(f"Quit by typing '{EXIT_CHAR}' or providing empty input.")
    print(f"Remove last radical by typing '{REMOVE_CHAR}'.")
    
    
    hits = []
    radicals_of_character = []
    radical = ' '
    character_position = 0
    
    print("Now, providing radicals ...")
    while radical != EXIT_CHAR and radical != '':
        radical = input("Radicals " + ' '.join(radicals_of_character) + ' : ')
        
        if radical == REMOVE_CHAR:
            radicals_of_character.pop(-1)
        elif radical in radical_list:
            radicals_of_character.append(radical)
            
            character_position = _compute_position(
                radicals_of_character,
                radical_list
                )
            hits = []
            for key, sublist in char_registry_dict.items():
                if _position_contained(character_position, key):
                    hits += sublist
                    
            print("Possible hits: " + ' '.join(hits[:10]))
        elif radical != EXIT_CHAR and radical != '':
            print(f"{radical} not in file '{RADICAL_FILE.name}'.")
    
