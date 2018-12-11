import shelve
from tkinter import *

data = shelve.open("database")
root = Tk()
root.geometry("500x200")
root.title("CSE 337 Phonebook")

def show_edit():
    edit_window = Toplevel(root)

    choice = IntVar()
    name_label = Label(edit_window, text="Name")
    name_entry = Entry(edit_window, width=40)
    phone_label = Label(edit_window, text="Phone")
    phone_entry = Entry(edit_window, width=40)
    address_label = Label(edit_window, text="Address")
    address_entry = Entry(edit_window, width=40)

    def save_record():
        print(choice.get(), "saved record")

    personal_radio = Radiobutton(edit_window, text="Personal", variable=choice, value=1)
    business_radio = Radiobutton(edit_window, text="Business", variable=choice, value=2)

    save_button = Button(edit_window, text="Save record", command=save_record)

    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1, columnspan=3)
    phone_label.grid(row=1, column=0)
    phone_entry.grid(row=1, column=1, columnspan=3)
    address_label.grid(row=2, column=0)
    address_entry.grid(row=2, column=1, columnspan=3)
    personal_radio.grid(row=3, column=1)
    business_radio.grid(row=3, column=2)
    # save_button.grid(row=4, column=1, columnspan=2)
    save_button.grid(row=4, column=0, columnspan=4)

def show_search():
    search_window = Toplevel(root)

    name_label = Label(search_window, text="Name")
    name_entry = Entry(search_window, width=40)
    search_result = Label(search_window, width=40, height=5, text="")

    def search_record():
        print("search record")
        search_result.config(text="bet")

    search_button = Button(search_window, text="Search record", command=search_record)

    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1, columnspan=3)
    search_result.grid(row=1, column=0, columnspan=4)
    search_button.grid(row=2, column=0, columnspan=4)

def show_delete():
    delete_window = Toplevel(root)

    name_label = Label(delete_window, text="Name")
    name_entry = Entry(delete_window, width=40)

    def delete_record():
        print("delete record")

    delete_button = Button(delete_window, text="Delete record", command=delete_record)

    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1, columnspan=3)
    delete_button.grid(row=1, column=0, columnspan=4)

edit = Button(root, text="Create/Edit Record", command=show_edit, width=30)
search = Button(root, text="Search Record", command=show_search, width=30)
delete = Button(root, text="Delete Record", command=show_delete, width=30)

edit.pack()
search.pack()
delete.pack()

root.mainloop()
data.close()