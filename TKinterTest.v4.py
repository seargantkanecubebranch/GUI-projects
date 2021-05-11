from tkinter import *

top = Tk()
songList = []



def printList():
    print(songList)

def exportList():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s\n" % item)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy

def mainMenu():
    clearWindow()
    LMain = Label(top, text= "block 5 gui projects")
    LMain.grid(column = 0, row = 1)
    B1Main = Button(text = "week one" , bg = "white", command = weekOne)
    B1Main.grid(column = 0, row = 2)
    B2Main = Button(text = "week two" , bg = "white", command = weekTwo)
    B1Main.grid(column = 1, row = 2)
    B3Main
    B1Main.grid(column = 3, row = 2)
    
def weekOne():

    def addTrack():
        songList.append(E1.get())
        E1.delete(0, END)

    clearWindow()
        
    #lable widget
    L1 = Label(top, text="playlist generator")
    L1.grid(column=0 , row=1 )


    #this ia an entry widget ( for text response)
    E1 = Entry(top, bd = 5)
    E1.grid(column=0 , row=2 )

    #this is a button widget
    B1 = Button(text = " + ", bg = "white", command= addTrack)
    B1.grid(column= 1, row= 2)

    B2 = Button(text = " print playlist", bg = "skyBlue", command= printList)
    B2.grid(column= 1, row= 1)

    B3 = Button(text = "export", bg = "white", command= exprotList
    B3.grid(column= 1, row= 3)


def weekTwo():
    clearWindow()

    L1W2 = Label(top, text="dice roller prog.")
    L1W2.grid(column=2, row=1)

    L2W2 = Label(top, text=" # of sides")
    L2W2 = grid(column=0, row=2)

    L3W2 = Label(top, text=" # of rolls")
    L3W2 = grid(column=3, row=2)

    E1W2 = Entry(top, bd = 5)
    E1W2 = grid(column=0, row=3)

    E2W2 = Entry(top, bd = 5)
    E2W2 = grid(column=3, row=3)

    B1W2 = Button(text = "roll em", bg = "sky blue")
    B1W2 = grid(column=2, row=4)


if __name__ == "__main__":
top.mainloop()


# problems
            #error : B3 main syntax error
