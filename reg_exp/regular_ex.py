"""

"""
import re

character_1 = "Alice"
character_2 = "White Rabbit"
with open("data/alice_in_wonderland.txt", "r") as f:
    content = f.read()
    found_alice = re.findall(character_1, content)
    if found_alice:
        print(len(found_alice))
    found_rabbit = re.findall(character_2, content)
    if found_rabbit:
        print(len(found_rabbit))

