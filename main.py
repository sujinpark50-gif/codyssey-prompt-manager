prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "주어진 주제에 대해 서론, 본론, 결론 구조의 블로그 글을 작성한다.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "이미지 생성 프롬프트",
        "content": "제품이나 서비스의 특징을 반영한 이미지 생성 프롬프트를 작성한다.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "AI 뉴스 요약 프롬프트",
        "content": "AI 뉴스 기사를 핵심 내용 중심으로 3줄 이내로 요약한다.",
        "category": "자동화",
        "favorite": True
    }
]


def show_menu():
    print("\n===== 나만의 프롬프트 관리 =====")
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

    choice = input("선택: ")

    if choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("아직 구현되지 않은 기능입니다.")