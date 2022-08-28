# print("백문이 불여일견\n백견이 불여일타") # \n : 줄바꿈

# print('저는 \"나도코딩\"입니다.') # \'도 동일

# print("C:\\Users\\NadoCoding\\Desktop") # \\ -> \

# print("Red Apple\rPine") # \r : 커서를 맨 앞으로 이동

# print("Redd\bApple") # \b : 한 글자 삭제

# print("Red\tApple") # \t : 탭

site_url = "http://naver.com"
site_url_http = site_url[7:-4]
pass1 = site_url_http[:3]
pass2 = str(len(site_url_http))
pass3 = str(site_url_http.count("e"))
password = pass1 + pass2 + pass3 + "!"
print(password)
print(f"{site_url}의 비밀번호는 {password}입니다.")