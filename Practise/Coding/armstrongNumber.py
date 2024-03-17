# def armstrongNumber(n):
#     b=len(n)
#     # a=[int(_) for _ in n]
#     count=0
#     for i in n:
#         count+=int(i)**b
#     return int(n)==count
# user=input()
# result=armstrongNumber(user)
# print(result)
#

# add = lambda x,y,c:x+y+c
# result = add(1,2,3)
# print(result)

















from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.geeksforgeeks.org/")

element = driver.find_element(By.ID,"gsc-i-id1")

element.send_keys("Arrays")