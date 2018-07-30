import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')


var1 = tk.StringVar()
lable = tk.Label(
    window,
    bg='yellow',
    width=4,
    height=3,
    textvariable=var1
)
lable.pack()


def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)


btn = tk.Button(
    window,
    text='print selection',
    width=20,
    height=3,
    command=print_selection
)
btn.pack()


var2 = tk.StringVar()
var2.set([11,34,57,12,88,12])
lb = tk.Listbox(
    window,
    listvariable=var2
)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

window.mainloop()