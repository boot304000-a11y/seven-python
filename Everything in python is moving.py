import tkinter
num = 0
r = 0
s = 0
def seven():
    global num
    if num < 3:
        print('yay')
        num = num + 1
    if num == 3:
        print('No')
        print('Do not press again.')
def move():
    global r
    r=r+1
    y.place(x = 0, y = r)
    root.after(16, move)
def moving():
    global s
    s=s+1
    x.place(x = 280, y = 280 - s)
    root.after(16, moving)
root = tkinter.Tk()
z = tkinter.Label(root, text = 'Pu-hungary-sh')
z.grid()
a = tkinter.Canvas(root, bg='red', width = 300, height = 100)
a.grid()
b = tkinter.Button(root, text = 'Push me', command = seven, height = 1, width = 6)
b.grid(pady = 37)
c = tkinter.Canvas(root, bg='green', width = 300, height = 100)
c.grid()
y = tkinter.Canvas(root, bg = 'red', height = 20, width = 20)
y.place(x = 0, y = r)
x = tkinter.Canvas(root, bg = 'green', height = 20, width = 20)
x.place(x = 280, y = s)
moving()
move()
root.mainloop()