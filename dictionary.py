# cabinet = {3:"유재석", 100:"김태호"} # key : value
# print(cabinet[3])
# print(cabinet.get(3)) # 2번줄과 동일

# # print(cabinet[5])
# print(cabinet.get(5)) # 6번줄만 동작 : none
# print(cabinet.get(5, "사용 가능"))

cabinet = {"A":"유재석", "B":"김태호"}
# print(3 in cabinet) # True
# print(5 in cabinet) # False

print(cabinet)

cabinet["A"] = "김종국"
cabinet["C"] = "조세호"
print(cabinet)

del cabinet["A"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)