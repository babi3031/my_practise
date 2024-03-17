# def generteFibonacciloop(n):
#     fib_series = [0,1]
#     if n <= 0:
#         return []
#     elif n==1:
#         return [0]
#     else:
#         for i in range(2,100):
#             next_fib_series = fib_series[i-1]+fib_series[i-2]
#             fib_series.append(next_fib_series)
#         print(len(fib_series))
#         return fib_series
#
# n=int(input())
# result = generteFibonacciloop(n)
# print(result)

"""
Implement a function generateFibonacciRecursion to generate
the Fibonacci series up to the nth term using recursion.
"""
# def generateFibonacciRecursion(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fibonacci_series = generateFibonacciRecursion(n - 1)
#         print(fibonacci_series)
#         fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
#         return fibonacci_series
#
# # Example usage:
# n = 30
# result = generateFibonacciRecursion(n)
# print(result)  # Output: [0, 1, 1, 2, 3, 5, 8, 13]

a=256
b=256
print(a is b)
a=257
b=257
print(a is b)