def compressStringLoop(s):
    if not s:
        return s

    compressed_string = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_string += s[i - 1] + str(count) if count > 1 else s[i - 1]
            count = 1

    compressed_string += s[-1] + str(count) if count > 1 else s[-1]

    return compressed_string

# Example usage:
input_string = "aabbbccccdd"
result = compressStringLoop(input_string)
print(result)  # Output: "a2b3c4d2"




def compressStringRecursion(s, index=0, count=1):
    if index == len(s) - 1:
        return s[index] + (str(count) if count > 1 else "")

    if s[index] == s[index + 1]:
        return compressStringRecursion(s, index + 1, count + 1)
    else:
        compressed_part = s[index] + (str(count) if count > 1 else "")
        return compressed_part + compressStringRecursion(s, index + 1, 1)

# Example usage:
input_string = "aabbbccccdd"
result = compressStringRecursion(input_string)
print(result)  # Output: "a2b3c4d2"
