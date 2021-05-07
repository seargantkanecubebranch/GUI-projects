from tkinter import *

top = Tk()
songList = []

def addTrack():
    songList.append(E1.get())
    E1.delete(0, END)

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
    B1Main.grid(column = 0, row = 
    B2Main
    B3Main
    
def weekOne():
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


if __name__ == "__main__":
top.mainloop()


# problems
            #error :
