import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')


def print_selection(v):
    l.config(text='you have selected ' + v)


l = tk.Label(
    window,
    width=20,
    bg='yellow',
)
l.pack()

s = tk.Scale(
    window,
    label='try me',
    from_=5, to=11,
    orient=tk.HORIZONTAL,
    length=200,
    showvalue=0,    # 不会显示选定的value
    tickinterval=2, # 隔多少长度显示一个数字
    resolution=0.01,    # 小数位数
    command=print_selection
)
s.pack()

window.mainloop()