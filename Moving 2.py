import tkinter
r = 0
def move():
    global r
    r=r+1
    y.place(x = 100, y = r)
    root.after(16, move)
root = tkinter.Tk()
x= tkinter.Canvas(root, height = 1000, width = 200)
x.pack()
y = tkinter.Canvas(root, bg = 'red', height = 20, width = 20)
y.place(x = 100, y = r)
move()
root.mainloop()