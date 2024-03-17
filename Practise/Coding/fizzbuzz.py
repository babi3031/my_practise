"""
% modulo operator
"""
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#  """
#  // integer division
#  """
# for i in range(1,101):
#     if i//3*3==i and i//5*5==i:
#         print("FizzBuzz")
#     elif i//3*3==i:
#         print("Fizz")
#     elif i//5*5==i:
#         print("Buzz")
#     else:
#         print(i)