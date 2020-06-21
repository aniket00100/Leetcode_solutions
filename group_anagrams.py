def group_anagrams(strs):
    dictionary = {}
    values = set()
    for i in strs:
        dictionary[i] = ''.join(sorted(i))
        values.add(dictionary[i])
    ans = []
    for i in values:
        temp = []
        for key in dictionary:
            val = dictionary[key]
            if val == i:
                temp.append(key)
        ans.append(temp)
    return ans

strs = input("strs = ").split()
print(group_anagrams(strs))
# group_anagrams(strs)