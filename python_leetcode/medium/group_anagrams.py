"""NeetCode 150: Arrays and Hashing"""


from collections import defaultdict


def group_anagrams(strs: list[str]):
    res = defaultdict(list)  # mapping char count to the list of anagrams
    for s in strs:
        count = [0] * 26  # a ... z
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return res.values()


string_items = ["cat", "owl", "low", "king", "wol", "act", "hello"]

print(group_anagrams(string_items))
