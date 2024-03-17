# def secondHighestNumber(numbers):
#     num=list(set(numbers))
#     num.sort()
#     return num[-2]
# user=[1,0,3,4,55,59,66]
# result=secondHighestNumber(user)
# print(result)

def secondHighestNumber(numbers):
    num=list(set(numbers))
    num.remove(max(num))
    return max(num)
user=[1,0,3,4,55,59,66]
result=secondHighestNumber(user)
print(result)