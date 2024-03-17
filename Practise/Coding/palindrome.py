user = input()

def isPalinedromeNumber(string):
    a = len(string)
    b = ''
    for i in range(0, a):
        b += string[(a - 1) - i]
    return string == b

input_string = input("Enter a keyword:")
result = isPalinedromeNumber(input_string)
print(
    f"Enter keyword {input_string} is palindrome" if result else f"Enter keyword {input_string} is Not a palindrome")


'''
Implement a function isPalindromeString that takes a string
as input and returns true if it's a palindrome, false otherwise.
'''
def isPalindromeString(s):
    # Convert the string to lowercase to handle case-insensitivity
    s = s.lower()

    # Remove non-alphanumeric characters from the string
    s = ''.join(char for char in s if char.isalnum())

    # Compare the original string with its reverse
    return s == s[::-1]


# Example usage:
input_string = "1A man, a plan, a canal: Panama1"
result = isPalindromeString(input_string)
print(result)  # Output: True


'''
Write a function isPalindromeNumber to determine if a given integer is a palindrome
'''
def isPalindromeNumber(num):
    # Convert the number to a string
    num_str = str(num)

    # Compare the original string with its reverse
    return num_str == num_str[::-1]


# Example usage:
input_number = 121
result = isPalindromeNumber(input_number)
print(result)  # Output: True
