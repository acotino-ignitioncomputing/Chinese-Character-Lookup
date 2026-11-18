# Chinese character lookup

This repository contains the simple CLI tool `src/look_up.py`
for looking up Chinese characters using their radicals.

The radicals should be stored in `src/radicals.txt` where each line contains
precisely 1 radical. Each radical is then associated with a power of 2
according to its line number.

Each Chinese character will be associated with the sum of its radicals,
counting each power of 2 only once. For example, let the radicals `木` and `广` be associated with
the integers 1 and 3 respectively. The character `麻` will be associated with `9 = 2^1 + 2^3`.

The Chinese characters are stored as a Python dictionary in the
file `src/character_registry.pkl`. The keys of this dictionary are integers and its values are
lists of characters. Its type hint is `dict[int, list[str]]`. 
The library `Pickle` is used for loading and storing
this dictionary.

The CLI tool `src/add_radical.py` can be used for creating the file `src/radicals.txt` and 
appending radicals to it.

The CLI tool `src/register_character.py` can be used for creating the file `src/character_registry.pkl`
and adding characters to the dictionary.

## Example

Check which characters in `src/character_registry.pkl` contain the radical `由`

```bash
python look_up.py

Look up a character in the character_registry by providing radicals
Quit by typing 'q' or providing empty input.
Remove last radical by typing 'r'.
Now, providing radicals ...
Radicals  : 由
Possible hits: 油
Radicals 由 : 
```

