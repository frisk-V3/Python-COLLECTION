import time
import random

print("3秒後にEnterキーを押せ！")
time.sleep(random.uniform(2, 4))

start = time.time()
input("今だ！")
end = time.time()

print("反射速度:", end - start, "秒" )
input("\n確認したらEnterを押してね")
