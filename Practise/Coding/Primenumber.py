# from math import sqrt
# def isPrime(num):
# 	if num <= 1:
# 		return False
# 	for i in range(2, int(sqrt(num)) + 1):
# 		if num % i == 0:
# 			return False
# 	return True
# user=int(input())
# result=isPrime(user)
# print(result)
#

# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# def generate_twin_primes(start, end):
#     twin_primes = []
#     for num in range(start, end - 1):
#         if is_prime(num) and is_prime(num + 2):
#             twin_primes.append((num, num + 2))
#     return twin_primes
#
# # Example usage:
# start_range = 1
# end_range = 50
# result = generate_twin_primes(start_range, end_range)
#
# print(f"Twin prime numbers between {start_range} and {end_range} are:")
# for twin_prime_pair in result:
#     print(twin_prime_pair)

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i) == 0:
            return False
    return True


def generate_twin_prime(start, end):
    twin_primes = []
    for num in range(start, end - 1):
        if isPrime(num) and isPrime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes


start = int(input())
end = int(input())
result = generate_twin_prime(start, end)

print(f"Twin prime numbers between {start} and {end} are:")
for twin_prime_pair in result:
    print(twin_prime_pair)