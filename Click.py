import tkinter
r = 0
num = 0
t = 16
f = False
def seven():
    global num, t
    print('Your score is adding.')
    num = num + 1
    print(num)
    t = int(t /2)


def move():
    global r, t, f
    if r == 900:
        f = True
    if r == 0:
        f = False
    if f == False:
        r=r+1
    if f == True:
        r = r-1
    y.place(x = 100, y = r)
    root.after(t, move)
root = tkinter.Tk()
x= tkinter.Canvas(root, height = 900, width = 500)
x.pack()
y = tkinter.Button(root, bg = 'red', height = 2, width = 20, command = seven)
y.place(x = 100, y = r)
move()
root.mainloop()