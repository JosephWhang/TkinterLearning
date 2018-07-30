import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('400x400')


def hit_me():
    tk.messagebox.showinfo(title='Hi', message='hhhh')
    tk.messagebox.showwarning(title='Hi', message='!!!!!')
    tk.messagebox.showerror(title='Hi', message='no error!')
    print(tk.messagebox.askquestion(title='Hi', message='huhuhuhu')) # return no/yes
    print(tk.messagebox.askyesno(title='Hi', message='huhuhuhu')) # return true/false
    print(tk.messagebox.askokcancel(title='Hi', message='hhhhhh')) # return true/false


tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()