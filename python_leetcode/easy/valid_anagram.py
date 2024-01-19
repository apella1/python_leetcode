"""NeetCode 150"""


from collections import Counter


# using collections' Counter
def valid_anagram_counter(s: str, t: str) -> bool:
    if len(t) > len(s):
        return False
    t_letters = Counter(t)
    s_letters = Counter(s)
    if t_letters == s_letters:
        return True
    return False


print(valid_anagram_counter("bat", "tab"))
print(valid_anagram_counter("hello", "kings"))
