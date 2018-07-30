import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')


var = tk.StringVar()


def print_selection():
    lable.config(text='you have selected ' + var.get())


lable = tk.Label(
    window,
    width=20,
    text='empth',
    bg='yellow'
)
lable.pack()

rbtn1 = tk.Radiobutton(
    window,
    text='option A',
    variable=var,
    value='A',
    command=print_selection
)
rbtn1.pack()


rbtn2 = tk.Radiobutton(
    window,
    text='option B',
    variable=var,
    value='B',
    command=print_selection
)
rbtn2.pack()


rbtn3 = tk.Radiobutton(
    window,
    text='option C',
    variable=var,
    value='C',
    command=print_selection
)
rbtn3.pack()

window.mainloop()