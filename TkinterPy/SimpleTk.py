import tkinter as tk


# 定义一个窗口
window = tk.Tk()
window.title('my window')
window.geometry('500x300')


# 定义一个标签
var = tk.StringVar()
lable = tk.Label(
    window,
    textvariable=var,
    bg='green',
    font=('Arial',12),
    width=20,height=10
)
lable.pack()
on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('none')


# 定义一个按钮
btn = tk.Button(
    window,
    text='hit me',
    width=15,
    height=5,
    command=hit_me
)
btn.pack()

window.mainloop()