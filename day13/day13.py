"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def k_distinct(s: str, k: int):
    l = list()
    for i in range(len(s)):
        if i == 0:
            l.append(0)
        else:
            index = l[-1]  # where starts the last substring with k unique characters (ends with i-1)
            subset = set(s[index:i])  # unique characters of index to i-1 + the new character
            if len(subset) <= k:
                l.append(index)
            else:  # the new character isn't fit
                for j in range(index, i+1):  # iterate in the list until the substrng will fit
                    if len(set([*s[j:i], s[i]])) <= k:
                        l.append(j)
                        break
    start = 0
    end = 0
    for i in range(len(l)):
        if (i-l[i]) > (end-start):
            start = l[i]
            end = i
    return s[start:end]



print(k_distinct("abcba", 2))