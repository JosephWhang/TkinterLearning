import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')


l = tk.Label(
    window,
    width=20,
    bg='yellow'
)
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='l only love Python')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='l only love C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='l do not love either')
    else:
        l.config(text='l love both')


var1 = tk.IntVar()
cbtn1 = tk.Checkbutton(
    window,
    text='Python',
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=print_selection
)
var2 = tk.IntVar()
cbtn2 = tk.Checkbutton(
    window,
    text='Python',
    variable=var2,
    onvalue=1,
    offvalue=0,
    command=print_selection
)
cbtn1.pack()
cbtn2.pack()


window.mainloop()