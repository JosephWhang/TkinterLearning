import tkinter as tk


# 定义一个窗口
window = tk.Tk()
window.title('my window')
window.geometry('500x300')


# 定义输入框和text框以及对应的插入
e = tk.Entry(window, show=None)
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert',var)


def insert_end():
    var = e.get()
    t.insert('end',var)


# 定义两个button
btn1 = tk.Button(
    window,
    text='input point',
    width=15,
    height=5,
    command=insert_point
)
btn1.pack()
btn2 = tk.Button(
    window,
    text='input end',
    width=15,
    height=5,
    command=insert_end
)
btn2.pack()


t = tk.Text(
    window,
    height=2
)
t.pack()

window.mainloop()