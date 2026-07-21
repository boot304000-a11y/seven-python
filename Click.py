import tkinter
r = 0
num = 0
t = 16
def seven():
    global num, t
    print('Your score is adding.')
    num = num + 1
    t = int(t /2)


def move():
    global r, t
    r=r+1
    y.place(x = 100, y = r)
    root.after(t, move)
root = tkinter.Tk()
x= tkinter.Canvas(root, height = 1000, width = 500)
x.pack()
y = tkinter.Button(root, bg = 'red', height = 2, width = 20, command = seven)
y.place(x = 100, y = r)
move()
root.mainloop()