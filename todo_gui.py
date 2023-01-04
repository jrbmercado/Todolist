from tkinter import *

root = Tk()
root.geometry("500x200")
root.title("Reminders")

todoLabel = Label(text="Reminders", font=("Helvetica bold", 40))
todoLabel.pack()

frame = Frame(root)
frame.pack(pady=10)

myList = Listbox(
    frame,
    font="Helvetica",
    width=25,
    height=5,
    bd=0,
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none"
)

myList.pack(side=LEFT, fill=BOTH)
stuff = ["test1", "test2", "test3", "test4", "test5"]
for item in stuff:
    myList.insert(END, item)

myScrollbar = Scrollbar(frame)
myScrollbar.pack(side=RIGHT, fill=BOTH)

myList.config(yscrollcommand=myScrollbar.set)
myScrollbar.config(command=myList.yview)

myEntry = Entry(root, font=("Helvetica", 24))
myEntry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)


def deleteItem():
    pass


def addItem():
    pass


delButton = Button(button_frame, text="Delete item", command=deleteItem)
addButton = Button(button_frame, text="Delete item", command=addItem)

delButton.grid(row=0, column=0)
addButton.grid(row=0, column=1, padx=20)
root.mainloop()
