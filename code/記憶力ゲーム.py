import random
import time

nums = [random.randint(0, 9) for _ in range(5)]
print("覚えて！", nums)
time.sleep(2)

print("\n" * 20)  # 画面を消す代わり
ans = input("数字を順番に入力: ")

if ans == "".join(map(str, nums)):
    print("正解！")
else:
    print("不正解… 正解は", nums)
