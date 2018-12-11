import shelve
from tkinter import *

data = shelve.open("database")
root = Tk()
root.geometry("500x250")
root.title("CSE 337 Phonebook")

def random():
    print("HI")

choice = IntVar()
edit = Button(root, text="Create/Edit Record", command=random)
search = Button(root, text="Search Record", command=random)

edit.pack(pady=5)
search.pack(pady=5)

root.mainloop()
data.close()