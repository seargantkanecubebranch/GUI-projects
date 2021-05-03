from tkinter import *

top = Tk()

L1 = Label(top, text="hello, world!")


L1.grid(column=0 , row=1 )

E1 = Enrty(top, bd = 5)

E1..grid(column=0 , row=2 )
# put line to use
print (E1.get())
top.mainloop
