from tkinter import *
import random

top = Tk()
songList = []
myRolls = []
rollTimes = 0
dieType = 0



def printList():
    print(songList)

def exportList():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s\n" % item)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text= "block 5 gui projects")
    LMain.grid(column = 0, row = 1)
    
    B1Main = Button(text = "week one" , bg = "white", command = weekOne)
    B1Main.grid(column = 1, row = 1)
    
    B2Main = Button(text = "week two" , bg = "white", command = weekTwo)
    B2Main.grid(column = 1, row = 2)
    
    B3Main = Button(text = "week three" , bg = "white",)
    B3Main.grid(column = 1, row = 3)
    
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
    B1.grid(column= 3, row= 1)

    B2 = Button(text = " print playlist", bg = "skyBlue", command= printList)
    B2.grid(column= 1, row= 1)

    B3 = Button(text = "export", bg = "white", command= exportList)
    B3.grid(column= 1, row= 3)

    B4 = Button(text="main menu", bg = "yellow", command = mainMenu)
    B4.grid(column= 0, row= 4)

def weekTwo():
    def rollDice():
        #update data
        rollTimes = E2W2.get()
        dieType = E1W2.get()

        #clear window
        clearWindow()
        #calculate dice rolls
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))
        #display the roll
            L4W2 = label(top, text= "here are your rolls!")
            L4W2.grid(column= 0, row= 1)
            
            L5W2 = label(top, text= "{}".format(myRolls))
            L5W2.grid(column= 0, row= 2)
            
            B2W2 = Button(text= "mainMenu", bg = "yellow", command = mainMenu )
            

    clearWindow()

    L1W2 = Label(top, text="dice roller prog.")
    L1W2.grid(column=2, row=1)

    L2W2 = Label(top, text=" # of sides")
    L2W2.grid(column=0, row=2)

    L3W2 = Label(top, text=" # of rolls")
    L3W2.grid(column=3, row=2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column=0, row=3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column=3, row=3)

    B1W2 = Button(text = "roll em", bg = "sky blue", command = rollDice)
    B1W2.grid(column=2, row=4)

    B2W2 = Button(text = "mainmenu", bg = "yellow", command = mainMenu)
    B2W2.grid(column=2, row=5,)

if __name__ == "__main__":
    mainMenu()
    top.mainloop()


# problems
            #error : add entry
