message = "안녕하세요"
print(message)

name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))

print("안녕하세요 " + name + "님!")

if age >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")