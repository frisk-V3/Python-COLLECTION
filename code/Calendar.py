import tkinter as tk
import datetime
import calendar

def create_calendar():
    now = datetime.datetime.now()
    year = now.year
    month = now.month

    root = tk.Tk()
    root.title(f"{year}年 {month}月 カレンダー")

    # タイトル
    title = tk.Label(root, text=f"{year}年 {month}月", font=("Arial", 20))
    title.pack()

    frame = tk.Frame(root)
    frame.pack()

    # 曜日ヘッダー
    headers = ["日","月","火","水","木","金","土"]
    for i, h in enumerate(headers):
        color = "red" if i == 0 else "blue" if i == 6 else "black"
        lbl = tk.Label(frame, text=h, width=4, fg=color)
        lbl.grid(row=0, column=i)

    # 月初の曜日と日数
    first_day, days_in_month = calendar.monthrange(year, month)

    row = 1
    col = 0

    # 空白
    for _ in range(first_day):
        tk.Label(frame, text=" ", width=4).grid(row=row, column=col)
        col += 1

    # 日付
    for day in range(1, days_in_month + 1):
        weekday = (first_day + day - 1) % 7
        color = "red" if weekday == 0 else "blue" if weekday == 6 else "black"

        lbl = tk.Label(frame, text=str(day), width=4, fg=color)
        lbl.grid(row=row, column=col)

        col += 1
        if col >= 7:
            col = 0
            row += 1

    root.mainloop()

create_calendar()

#確認したら消す
input("\n確認したらEnterを押してね
