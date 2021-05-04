from tkinter import *

top = Tk()
songList = []

def addTrack():
    songList.append(E1.get())

def printList():
    print(songList)
    

#lable widget
L1 = Label(top, text="playlist generator")
L1.grid(column=0 , row=1 )


#this ia an entry widget ( for text response)
E1 = Entry(top, bd = 5)
E1.grid(column=0 , row=2 )

#this is a button widget
B1.Button(text = " add to playlist", bg = "white", command= addTrack)
B1.grid(column= 1, row= 2)

B2.Button(text = " add to playlist", bg = "white", command= printList)
B2.grid(column= 1, row= 1)


top.mainloop


# problems name error : name B1 is not defined
