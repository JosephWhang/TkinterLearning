import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x300')

'''
tk.Label(window,text='top').pack(side='top')
tk.Label(window,text='left').pack(side='left')
tk.Label(window,text='right').pack(side='right')
tk.Label(window,text='bottom').pack(side='bottom')
'''

'''
for i in range(4):
    for j in range(3):
        # pad单元左右间隔
        tk.Label(window, text=1).grid(row=i, column=j, ipadx=20, ipady=20)
'''

tk.Label(window, text=1).place(x=10, y=100, anchor='nw')


window.mainloop()