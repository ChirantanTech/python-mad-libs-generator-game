from tkinter import *
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
def s2():
    adjective = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person = input('enter a person name : ')
    adjactive1 = input('enter a adjactive : ')
    insect = input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')
    print(f'''Last night I dreamed I was a {adjective} butterfly with {color} splocthes that looked like
            {thing}.I flew to {place} with my bestfriend and {person}
            who was a {adjactive1} {insect}.We ate some {food}
            When we got there and then decided to {verb} and the dream ended when I said-- lets {verb}.''')
def s3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')

    print('Today we picked apple from '+person + "'s Orchard. I had no idea there were so many different varieties of apples. I ate " + color + ' apples straight off the tree that tested like '+foods + '. Then there was a '+adjective + ' apple that looked like a ' + thing +
          '.When our bag were full, we went on a free hay ride to '+place + ' and back. It ended at a hay pile where we got to ' + verb + ' ' + adverb + '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food + ' and '+things+' pies!.')

intro = Label(root, text="Hello welcome to the Mad Libs game by Chirantan Banerjee",
              bg="LemonChiffon", padx=13, pady=20,font= "garamond 11 bold",relief = RAISED)
intro.pack(fill = X)

b1 = Button(root,text ="STORY 1",command = s1,bg= "aliceblue",font = "garamond 10 bold",relief = RAISED).pack(fill = X)
b2 = Button(root,text ="STORY 2",command = s2,bg= "antiquewhite",font = "garamond 10 bold",relief = RAISED).pack(fill = X)
b3 = Button(root, text="STORY 3", command=s3,bg= "lavender",font = "garamond 10 bold",relief = RAISED).pack(fill = X)


root.mainloop()
