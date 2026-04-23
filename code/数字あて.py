import random


answer = random.randint(1, 10)
tries = 5

while tries > 0:
    guess = int(input("数字を入力: "))
    if guess == answer:
        print("正解!")
        break
    elif guess < answer:
        print("もっと大きい")
    else:
        print("もっと小さい")

    tries -= 1
    print("残り回数:", tries)

if tries == 0:
    print("ゲームオーバー。正解は", answer)
