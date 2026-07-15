import json

prompts = [
    {
        "title": "요구사항 분석 전문가",
        "content": "당신은 10년 이상의 경력을 가진 서비스 기획자이자 요구사항 분석 전문가입니다. 사용자의 모호한 아이디어를 구조화하여 개발 가능한 요구사항으로 정리하는 역할을 수행합니다.",
        "category": "페르소나",
        "favorite": False,
        "views": 0
    },
    {
        "title": "의도노트AI 씬1 이미지 생성 프롬프트",
        "content": "늦은 밤의 조용한 작업 책상 장면을 만들어줘. 노트북 화면에는 빈 문서가 열려 있고, 문서 첫 줄에 커서만 깜빡이는 느낌이 보인다.사용자는 글을 써야 하지만 시작하지 못하고 있으며, 얼굴은 보이지 않고 키보드 위에 멈춘 손만 보인다.",
        "category": "이미지 생성",
        "favorite": False,
        "views": 0
    },
    {
        "title": "AI 뉴스 요약 프롬프트",
        "content": "AI 뉴스 기사를 핵심 내용 중심으로 3줄 이내로 요약한다.",
        "category": "자동화",
        "favorite": True,
        "views": 0
    }
]
def save_prompts():
    with open("prompts.json", "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)

def load_prompts():
    global prompts

    try:
        with open("prompts.json", "r", encoding="utf-8") as file:
            prompts = json.load(file)

    except FileNotFoundError:
        print("저장된 프롬프트가 없습니다.")

def show_menu():
    print("\n===== 나만의 프롬프트 관리 =====")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 수정")
    print("9. 조회수 상위 5 프롬프트")
    print("10. 프롬프트 삭제")
    print("11. Markdown으로 내보내기")
    print("0. 종료")


def add_prompt():
    print("\n===== 프롬프트 추가 =====")
    title = input("제목: ")
    content = input("내용: ")
    print("\n===== 카테고리 선택 =====")
    print("1. 텍스트 생성")
    print("2. 이미지 생성")
    print("3. 자동화")
    print("4. 페르소나")
    print("5. 영상 생성")
    print("6. 기타")
    category = input("선택: ")
    
    if category == "1":
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

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "views": 0
    }

    prompts.append(new_prompt)
    print("프롬프트가 추가되었습니다.")
    save_prompts()

def show_list():
    print("\n=== 프롬프트 목록 ===")
    
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        star = "⭐" if prompt["favorite"] else ""
        print(str(index) + ". [" + prompt["category"] + "] " + prompt["title"] + " " + star)

    print("총 " + str(len(prompts)) + "개의 프롬프트")

def show_category():
    print("\n===== 카테고리별 조회 =====")
    print("1. 텍스트 생성")
    print("2. 이미지 생성")
    print("3. 자동화")
    print("4. 페르소나")
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

def export_markdown(): 
    print("\n===== 카테고리별 Markdown으로 내보내기 =====")
    print("1. 텍스트 생성")
    print("2. 이미지 생성")
    print("3. 자동화")
    print("4. 페르소나")
    print("5. 영상 생성")
    print("6. 기타")
    print("0. 뒤로가기")
    category = input("내보낼 카테고리: ")
    
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

    filtered_category = []

    for prompt in prompts:
        if prompt["category"] == category:
            filtered_category.append(prompt)

    if len(filtered_category) == 0:
        print("해당 카테고리의 프롬프트가 없습니다.")
        return

    with open(category + ".md", "w", encoding="utf-8") as file:
        file.write("# " + category + " 프롬프트\n\n")
        for prompt in filtered_category:
            file.write("## " + prompt["title"] + "\n")
            file.write(prompt["content"] + "\n\n")
       
    print("Markdown 생성 완료")




def search_prompt():
    keyword = input("검색어: ")

    filtered_prompts = []

    for prompt in prompts:
        if keyword in prompt["title"] or keyword in prompt["content"]:
            filtered_prompts.append(prompt)

    if len(filtered_prompts) == 0:
        print("검색 결과가 없습니다.")
        return

    print("\n=== 검색 결과 ===")
    for index, prompt in enumerate(filtered_prompts, start=1):
        star = "⭐" if prompt["favorite"] else ""
        print(str(index) + ". [" + prompt["category"] + "] " + prompt["title"] + " " + star)


def show_prompt_detail():
    show_list()
    index = int(input("상세보기할 프롬프트 번호: ")) - 1
    prompt = prompts[index]
    prompt["views"] += 1 
    save_prompts()

    if index < 0 or index >= len(prompts):
        print("잘못된 선택입니다.")
        return

    prompt = prompts[index]
    print("\n=== 프롬프트 상세 정보 ===")
    print("제목: " + prompt["title"])
    print("내용: " + prompt["content"])
    print("카테고리: " + prompt["category"])
    print("즐겨찾기 여부: " + ("예" if prompt["favorite"] else "아니오"))
    print("조회수: " + str(prompt["views"]))

def manage_favorites():
    show_list()
    index = int(input("즐겨찾기 관리할 프롬프트 번호: ")) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 선택입니다.")
        return

    prompt = prompts[index]
    prompt["favorite"] = not prompt["favorite"]
    print("즐겨찾기 상태가 변경되었습니다.")
    save_prompts()

def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")

    favorite_prompts = []

    for prompt in prompts:
        if prompt["favorite"] == True:
            favorite_prompts.append(prompt)

    if len(favorite_prompts) == 0:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(favorite_prompts, start=1):
        print(str(index) + ". [" + prompt["category"] + "] " + prompt["title"])

def update_prompts():
    show_list()
    index=int(input("수정할 프롬프트 번호:"))-1
    new_title=input("제목:") 
    new_content=input("내용:") 
    print("\n===== 카테고리 =====") 
    print("1. 텍스트 생성") 
    print("2. 이미지 생성") 
    print("3. 자동화") 
    print("4. 페르소나") 
    print("5. 영상 생성") 
    print("6. 기타") 
    new_category=input("카테고리 선택:") 
    if new_category == "0": 
        return 
    elif new_category == "1": 
        new_category = "텍스트 생성" 
    elif new_category == "2": 
        new_category = "이미지 생성" 
    elif new_category == "3": 
        new_category = "자동화" 
    elif new_category == "4": 
        new_category = "페르소나" 
    elif new_category == "5": 
        new_category = "영상 생성" 
    elif new_category == "6": 
        new_category = "기타" 
    else: 
        print("잘못된 선택입니다.") 
        return

    prompts[index]["title"]=new_title 
    prompts[index]["content"]=new_content 
    prompts[index]["category"]=new_category

    print("프롬프트가 수정되었습니다.")
    save_prompts()

def top_viewed_prompts():
    sorted_prompts = sorted(prompts, key=lambda prompt: prompt["views"], reverse=True)
    top_prompts = sorted_prompts[:5]

    print("\n=== 조회수 상위 5 프롬프트 ===")
    for prompt in top_prompts:
        print(prompt["title"], " (조회수:" + str(prompt["views"]) + ")")

def delete_prompt():
    show_list()
    index = int(input("삭제할 프롬프트 번호: ")) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 선택입니다.")
        return

    del prompts[index]
    print("프롬프트가 삭제되었습니다.")
    save_prompts()

load_prompts()

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
    elif choice == "4":
        search_prompt()
    elif choice == "5":
        show_prompt_detail()
    elif choice == "6":
        manage_favorites()
    elif choice == "7":
        show_favorites()
    elif choice == "8":
        update_prompts()
    elif choice == "9":
        top_viewed_prompts()
    elif choice == "10":
        delete_prompt()
    elif choice == "11":
        export_markdown()       
    else:
        print("아직 구현되지 않은 기능입니다.")