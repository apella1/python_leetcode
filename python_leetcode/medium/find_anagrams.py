def find_anagrams(s, p):
    if len(p) > len(s):
        return []

    p_count, s_count = {}, {}

    for i in range(len(p)):
        p_count[p[i]] = 1 + p_count.get(p[i], 0)
        s_count[s[i]] = 1 + s_count.get(s[i], 0)

    res = [0] if p_count == s_count else []
    left_ptr = 0
    for right_ptr in range(len(p), len(s)):
        s_count[s[right_ptr]] = 1 + s_count.get(s[right_ptr], 0)
        s_count[s[left_ptr]] -= 1
        if s_count[s[left_ptr]] == 0:
            s_count.pop(s[left_ptr])
        left_ptr += 1
        if s_count == p_count:
            res.append(left_ptr)

    return res


print(find_anagrams("cbaebabacd", "abc"))
