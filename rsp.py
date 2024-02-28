import random

random_rsc = ["가위", "바위", "보"]


def retry(user_input):
    user_input = input("다시 하시겠습니까? (y/n): ")
    if user_input == "y" or user_input == "Y":
        return True
    elif user_input == "n" or user_input == "N":
        return False


def rsc_game():
    win = 0
    lose = 0
    draw = 0
    while True:
        choicelists = random.choice(random_rsc)
        user_input = input("가위, 바위, 보 중 하나를 내세요!: ")

        if not user_input in random_rsc:
            print('잘못된 입력: "가위", "바위" "보"만 입력하십시오.')

        if user_input == choicelists:
            print("무")
            draw = draw + 1
            continue

        if user_input == "가위" and choicelists == "보":
            print("승")
            win = win + 1
            if retry(user_input) == True:
                continue
            else:
                print("승:", win, "패:", lose, "무:", draw)
                break

        if user_input == "바위" and choicelists == "가위":
            print("승")
            win = win + 1
            if retry(user_input) == True:
                continue
            else:
                print("승:", win, "패:", lose, "무:", draw)
                break

        if user_input == "보" and choicelists == "바위":
            print("승")
            win = win + 1
            if retry(user_input) == True:
                continue
            else:
                print("승:", win, "패:", lose, "무:", draw)
                break

        if user_input == "가위" and choicelists == "바위":
            print("패")
            lose = lose + 1
            if retry(user_input) == True:
                continue
            else:
                print("승:", win, "패:", lose, "무:", draw)
                break

        if user_input == "바위" and choicelists == "보":
            print("패")
            lose = lose + 1
            if retry(user_input) == True:
                continue
            else:
                print("승:", win, "패:", lose, "무:", draw)
                break

        if user_input == "보" and choicelists == "가위":
            print("패")
            lose = lose + 1
            if retry(user_input) == True:
                continue
            else:
                print("승:", win, "패:", lose, "무:", draw)
                break


rsc_game()
