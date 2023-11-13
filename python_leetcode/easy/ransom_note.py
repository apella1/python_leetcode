from collections import Counter
from pprint import pprint


def can_construct_ransom_from_magazine(ransom_note: str, magazine: str) -> bool:
    ransom_note_letters = Counter(ransom_note)
    magazine_letters = Counter(magazine)
    for character in ransom_note_letters:
        if (
            character not in magazine_letters
            or ransom_note_letters[character] > magazine_letters[character]
        ):
            return False
    # warning: avoid ending the for loop before the end of the iterations ->
    # the outer return should not be within the scope of the for loop
    return True


# optimized solution using a single dictionary
def can_construct_optimized(ransom_note: str, magazine: str) -> bool:
    m_dict = Counter(magazine)
    for ch in ransom_note:
        if ch not in m_dict or m_dict[ch] == 0:
            return False
        else:
            m_dict[ch] -= 1
    return True


pprint(can_construct_ransom_from_magazine("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))
pprint(can_construct_optimized("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))

# We can also manually populate a dictionary from a string
# Counter collections module makes it easier to populate the dicts
string_dict = {}
word = "population density"

for letter in word:
    if letter not in string_dict:
        string_dict[letter] = 0
    string_dict[letter] += 1
