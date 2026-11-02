# attend.py - 스터디 출석부 프로그램
# 외부 라이브러리 없이 파이썬 기본 기능만 사용합니다.

import os  # 파일이 있는지 확인할 때 사용

FILENAME = "attendance.txt"  # 출석 기록을 저장할 파일 이름


def add_attendance():
    """날짜와 이름을 입력받아 출석을 기록(파일에 추가)합니다."""
    date = input("날짜를 입력하세요 (예: 2024-01-15): ").strip()
    name = input("이름을 입력하세요: ").strip()

    # 빈 값이 들어오면 저장하지 않고 돌아갑니다.
    if date == "" or name == "":
        print("날짜와 이름을 모두 입력해야 합니다.\n")
        return

    # "a" 모드 = append(기존 내용 뒤에 이어 쓰기)
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(date + "," + name + "\n")  # 날짜,이름 형태로 한 줄 저장

    print(f"출석 완료: {date} / {name}\n")


def show_list():
    """저장된 출석 기록 전체를 보여줍니다."""
    # 파일이 아직 없으면 기록이 없다는 뜻입니다.
    if not os.path.exists(FILENAME):
        print("아직 출석 기록이 없습니다.\n")
        return

    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()  # 모든 줄을 읽어옴

    if len(lines) == 0:
        print("아직 출석 기록이 없습니다.\n")
        return

    print("\n===== 출석 목록 =====")
    for i, line in enumerate(lines, start=1):
        line = line.strip()  # 줄 끝의 줄바꿈 제거
        if line == "":
            continue
        date, name = line.split(",")  # 쉼표 기준으로 날짜와 이름 분리
        print(f"{i}. {date}  -  {name}")
    print("====================\n")


def main():
    """프로그램의 시작점. 메뉴를 반복해서 보여줍니다."""
    while True:
        print("[스터디 출석부]")
        print("1. 출석 기록하기")
        print("2. 출석 목록 보기")
        print("3. 종료")
        choice = input("원하는 번호를 선택하세요: ").strip()

        if choice == "1":
            add_attendance()
        elif choice == "2":
            show_list()
        elif choice == "3":
            print("프로그램을 종료합니다. 수고하셨습니다!")
            break
        else:
            print("1, 2, 3 중에서 선택해 주세요.\n")


# 이 파일을 직접 실행했을 때만 main()이 돌아갑니다.
if __name__ == "__main__":
    main()
