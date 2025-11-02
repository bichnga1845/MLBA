from tkinter import *

# Danh sách các lựa chọn (ví dụ tên các model)
OPTIONS = [
    "model_1",
    "model_2",
    "model_3"
]

root = Tk()

variable = StringVar(root)
variable.set(OPTIONS[0])

w = OptionMenu(root, variable, *OPTIONS)
w.pack()

def ok():
    print("Value is:", variable.get())

button = Button(root, text="OK", command=ok)
button.pack(pady=5)

root.mainloop()
