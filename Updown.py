import random  # 랜덤 숫자를 위한 패키지 임포트

ct = []


def number_game():
    random_number = random.randint(1, 100)
    count = 0
    while True:                            # 반복 입력을 위해 while문 사용
        try:
            user_input = int(input("숫자를 입력하세요.: "))

            if user_input < 1 or user_input > 100:       # 지정된 범위를 벗어난 숫자가 들어왔을 때 나오는 문구
                print("잘못된 범위 : 1 ~ 100 사이의 숫자를 입력해주세요.")
                continue

            if user_input != random_number or user_input == random_number:
                count += 1

            if user_input < random_number:
                print("업")
            elif user_input > random_number:
                print("다운")
            else:
                print("정답입니다!")
                print("당신이 시행한 횟수는: ", count)
                ct.append(count)
                print("당신의 최고 기록은: ", min(ct))
                user_input2 = input("재도전 하시겠습니까?(y/n)")
                if user_input2 == "y":
                    return number_game()

                elif user_input2 == "n":
                    print("당신의 최고 기록은: ", min(ct))
                    return
        except:
            print("숫자를 입력해주세요.")


number_game()
