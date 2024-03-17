def generate_sequential_digits(start, end):
    result = []
    for num in range(start, end + 1):
        digits = [int(digit) for digit in str(num)]
        if all(digits[i] + 1 == digits[i + 1] for i in range(len(digits) - 1)):
            result.append(num)
    return result

# Example: Generate sequential digits between 100 and 300
start_range = 100
end_range = 300
sequential_numbers = generate_sequential_digits(start_range, end_range)
print(sequential_numbers)
