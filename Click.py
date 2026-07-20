import tkinter
r = 0
num = 0
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
    y.place(x = 100, y = r)
    root.after(16, move)
root = tkinter.Tk()
x= tkinter.Canvas(root, height = 500, width = 500)
x.pack()
y = tkinter.Button(root, bg = 'red', height = 2, width = 20, command = seven)
y.place(x = 100, y = r)
move()
root.mainloop()