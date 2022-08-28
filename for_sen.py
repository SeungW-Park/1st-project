# for i in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(i + 1))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}님, 커피가 준비되었습니다.".format(customer))

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}님, 커피가 준비되었습니다.".format(customer))
#     index -= 1 # index = index - 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언 맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("성함이 어떻게 되세요?")

# absent = [2, 5] # 결석
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(no_book))
#         break
#     print("{0}번, 책 읽어보세요.".format(student))

# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# # students = [len(i) for i in students]
# print(students)
from random import *

time = []
for i in range(1, 51):
    time.append(randrange(5, 51))

num = 0
for i in range(0, 50):
    if 5 <= time[i] <= 15:
        num += 1


for i in range(1, 51):
    if 5 <= time[i - 1] <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time[i - 1]))
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time[i - 1]))
print("\n")

print("총 탑승 승객 : {0} 분".format(str(num)))