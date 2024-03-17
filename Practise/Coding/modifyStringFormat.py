# def modifyStringFormat(string):
#     strg = ''
#     for i in string:
#         if i == " ":
#             strg += "_"
#         else:
#             strg += i
#     return strg
#
# user = input()
# result = modifyStringFormat(user)
# print(result)

def modifyStringFormat(string):
    string=string.replace(" ","_")
    return string

user = input()
result = modifyStringFormat(user)
print(result)
