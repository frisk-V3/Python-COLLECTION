try:
    line = input("数値を入力: ")
    num = int(line)
    print(f"16進数: {hex(num).upper()}")
except EOFError:
    print("データが空だよ！")
except ValueError:
    print("数字を入れてね！")

# ここに追加！
input("\n確認したらEnterキーを押してね")
