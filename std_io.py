# import sys

# print("python", "Java", file = sys.stdout)
# print("python", "Java", file = sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep = ":")

# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 :") # 문자열 형태로 저장
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")

print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

print("{0:_<+10}".format(500))

print("{0:,}".format(100000000000))

print("{0:+,}".format(100000000000))
print("{0:^<+30,}".format(100000000000))
# : 빈자리, 정렬, 부호, 자릿수, ',' 여부

print("{0:.2f}".format(5/3))