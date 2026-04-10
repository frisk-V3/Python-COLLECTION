import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter")

label = tk.Label(root, text="押してみ？")
label.pack(pady=10)

def clicked():
    label.config(text="押したな…？")

button = tk.Button(root, text="ボタン", command=clicked)
button.pack(pady=10)

root.mainloop()
