def char_count_occurence(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    return dict(sorted(char_count.items()))

s="babisamineedi"
result=char_count_occurence(s)
print(result)
