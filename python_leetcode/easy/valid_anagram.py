"""NeetCode 150"""


from collections import Counter


# using collections' Counter
# uses extra memory by creating the hash map
def valid_anagram_counter(s: str, t: str) -> bool:
    # The body can be reduced to a single line of code
    # * return Counter(s) == Counter(t)
    if len(t) != len(s):
        return False
    t_letters = Counter(t)
    s_letters = Counter(s)
    if t_letters == s_letters:
        return True
    return False


print(valid_anagram_counter("bat", "tab"))
print(valid_anagram_counter("hello", "kings"))


# manually creating hash maps
def make_map_from_string(s: str) -> dict[str, int]:
    s_map = {}
    for letter in s:
        if letter not in s_map:
            s_map[letter] = 0
        s_map[letter] += 1
    return s_map


print(make_map_from_string("ich koche manchmal"))


# using manual maps
def valid_anagram(s: str, t: str) -> bool:
    counter_s, counter_t = {}, {}
    if len(t) != len(s):
        return False
    for i in range(len(s)):
        # * using get() to assign a default value for missing keys
        counter_s[s[i]] = 1 + counter_s.get(s[i], 0)
        counter_t[t[i]] = 1 + counter_t.get(t[i], 0)
    for ct in counter_s:
        if counter_s[ct] != counter_t.get([ct], 0):
            return False
    return True


def valid_anagram_sorted(s: str, t: str) -> bool:
    # todo write own sorting function
    return sorted(s) == sorted(t)


print(valid_anagram_sorted("cat", "tac"))
