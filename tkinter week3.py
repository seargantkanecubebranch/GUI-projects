import tkinter
import turtle
import tkinter.message box

window = tkinter.Tk()

canvas = tkinter.canvas(master = window, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')
#draw, = turtle .turtle()
draw = turtle.RawTurtle(canvas)

def board(a, x, y, size):
    #draw.pu()
    draw.penup()
    draw.goto(x,y)
    #draw.pd()
    draw.pendown()
    for i in range (0,4):
        draw.forward(size)
        draw.right(90)

def board2():
    x =-40
    y = -40
    size = 40
    for i in range (0, 10):
        for j in range (0, 10):

def Buttonclick():
    tkinter.messagebox.showinfo("game", "tic tac toe")


#button = tkinter.Button(window, text = "play!", command = buttonclick
#button = tk.Button(window, text = "play!", command = buttonclick
#button.pack()
#
Play_Button = tkinter.Button(master = window, text ="play", command = Buttonclick)
Play_Button.config(bg="cyan", fg="black")
Play_Button.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

Board_Button = tkinter.Button(master = window, text
Board_Button
Board_Button



    
