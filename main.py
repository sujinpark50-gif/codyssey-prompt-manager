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

def show_list():
    print("\n=== 프롬프트 목록 ===")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        star = "⭐" if prompt["favorite"] else ""
        print(str(index) + ". [" + prompt["category"] + "] " + prompt["title"] + " " + star)

    print("총 " + str(len(prompts)) + "개의 프롬프트")

def add_prompt():
    title = input("제목: ")
    content = input("내용: ")
    category = input("카테고리: ")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)
    print("프롬프트가 추가되었습니다.")

def show_category():
    print("\n===== 카테고리별 조회 =====")
    print("1. 텍스트 생성")
    print("2. 이미지 생성")
    print("3. 자동화")
    print("4. 프롬프트")
    print("5. 영상 생성")
    print("6. 기타")
    print("0. 뒤로가기")
    category = input("조회할 카테고리: ")
    
    if category == "0":
        return
    elif category == "1":
        category = "텍스트 생성"
    elif category == "2":
        category = "이미지 생성"
    elif category == "3":
        category = "자동화"
    elif category == "4":
        category = "페르소나"
    elif category == "5":
        category = "영상 생성"
    elif category == "6":
        category = "기타"
    else:
        print("잘못된 선택입니다.")
        return

    filtered_prompts = []

    for prompt in prompts:
        if prompt["category"] == category:
            filtered_prompts.append(prompt)

    if len(filtered_prompts) == 0:
        print("해당 카테고리의 프롬프트가 없습니다.")
        return

    print("\n=== " + category + " 프롬프트 목록 ===")
    for index, prompt in enumerate(filtered_prompts, start=1):
        star = "⭐" if prompt["favorite"] else ""
        print(str(index) + ". " + prompt["title"] + " " + star)



while True:
    show_menu()

    choice = input("선택: ")

    if choice == "0":
        print("프로그램을 종료합니다.")
        break
    elif choice == "1":
        add_prompt()
    elif choice == "2":
        show_list()
    elif choice == "3": 
        show_category()

    else:
        print("아직 구현되지 않은 기능입니다.")