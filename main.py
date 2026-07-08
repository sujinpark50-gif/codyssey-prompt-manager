def show_menu():
    print("===== 나만의 프롬프트 관리 =====")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

while True:
    show_menu()

    choice = input("선택 : ")

    if choice == "0":
        print("프로그램을 종료합니다.")
        break