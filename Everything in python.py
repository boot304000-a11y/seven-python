import tkinter
num = 0
def seven():
    global num
    if num < 3:
        print('yay')
        num = num + 1
    if num == 3:
        print('No')
        print('Do not press again.')
root = tkinter.Tk()
z = tkinter.Label(root, text = 'Pu-hungary-sh')
z.grid()
a = tkinter.Canvas(root, bg='red', width = 300, height = 100)
a.grid()
b = tkinter.Button(root, text = 'Push me', command = seven, height = 1, width = 6)
b.grid(pady = 37)
c = tkinter.Canvas(root, bg='green', width = 300, height = 100)
c.grid()
root.mainloop()