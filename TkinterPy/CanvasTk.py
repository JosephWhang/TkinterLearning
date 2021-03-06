import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')


def moveit():
    canvas.move(rect, 0, 2)


canvas = tk.Canvas(
    window,
    bg='blue',
    height=100,
    width=200,
)
image_file = tk.PhotoImage(file='')
image = canvas.create_image(0, 0,
                            anchor='nw',
                            image=image_file)
x0, y0, x1, y1 = 50,50,80,80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
rect = canvas.create_rectangle(100,30,120,50)
canvas.pack()

btn = tk.Button(
    window,
    text='move',
    command=moveit
).pack()


window.mainloop()