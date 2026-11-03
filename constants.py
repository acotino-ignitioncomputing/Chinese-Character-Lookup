from pathlib import Path

CHARACTER_REGISTRY = Path('character_registry.pkl')
RADICAL_FILE = Path('radicals.txt')

if not CHARACTER_REGISTRY.exists():
    print(f"No file {CHARACTER_REGISTRY} in repository. Created one now.")
    empty_dict = {}
    with CHARACTER_REGISTRY.open('wb') as file:
        pickle.dump(empty_dict, file)

if not RADICAL_FILE.exists():
    print(f"No file {RADICAL_FILE} in repository.")
    exit(1)