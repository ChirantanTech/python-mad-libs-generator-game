from tkinter import *  #Import tkinter its already present in your library if not then type pip install tkinter in terminal.
root = Tk() 
root.geometry("720x480")

def s1():
    name = input("Enter someone name : ")
    obj = input("Enter a object might be a gift or something : ")
    said = input("Enter a reaction : ")
    verb = input("Enter a verb : ")
    print(f'''{name} really wanted a {obj} for Christmas.{name} parents said,santa will get for you.
    Then on Christmas morning when all the presents were under the tree,{name} asked if it was what he wanted 
    and they said,him to open it.So the last gift {name} opened was the best one.He said ({said}) 
    When he opened it he screamed in happiness,and {verb} around the house.That was the best Christmas of his life!''')

intro = Label(root, text="Hello welcome to the Mad Libs game by Chirantan Banerjee",
              bg="LemonChiffon", padx=13, pady=20,font= "garamond 11 bold",relief = RAISED)
intro.pack(fill = X)

b1 = Button(root,text ="STORY 1",command = s1,bg= "aliceblue",font = "garamond 10 bold",relief = RAISED).pack(fill = X)


root.mainloop()
