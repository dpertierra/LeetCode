def firstUniqChar(s):
    letters = {}
    for i, c in enumerate(s):
        if c in letters:
            letters[c] = -1
        else:
            letters[c] = i
    for key, value in letters.items():
        if value > -1:
            return value
    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))