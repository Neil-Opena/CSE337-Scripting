import shelve
from tkinter import *
from tkinter import messagebox

data = shelve.open("phone_database")
root = Tk()
root.geometry("500x200")
root.title("CSE 337 Phonebook")


class Record():
    def __init__(self, name, phone, address, num_type):
        self.name = name
        self.phone = phone
        self.address = address
        self.num_type = num_type

    def display(self):
        temp = ""
        temp += "Name: " + self.name + "\n"
        temp += "Phone: " + self.phone + "\n"
        temp += "Address: " + self.address + "\n"
        temp += "Type: " + self.num_type
        return temp

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
        # verify that input is recieved
        name = name_entry.get()
        phone = phone_entry.get()
        address = address_entry.get()
        if(choice.get() == 0 or name == "" or phone == "" or address == ""):
            messagebox.showinfo("Error", "Please fill in all of the fields")
        else:
            if(choice.get() == 1):
                num_type = "Personal"
            else:
                num_type = "Business"
            data[name] = Record(name, phone, address, num_type)
            print("saved record")
            messagebox.showinfo("Success", "Database has been updated!")

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
    save_button.grid(row=4, column=0, columnspan=4)

def show_search():
    search_window = Toplevel(root)

    name_label = Label(search_window, text="Name")
    name_entry = Entry(search_window, width=40)
    search_result = Label(search_window, width=40, height=5, text="")

    def search_record():
        print("search record")
        if name_entry.get() == "":
            messagebox.showerror("Error", "Please fill in the entry")
        else:
            if name_entry.get() in data:
                to_display = "Record found\n" + data[name_entry.get()].display()
            else:
                to_display = "Record not found for: " + name_entry.get()
                messagebox.showerror("Error", "No record for: " + name_entry.get())
            search_result.config(text=to_display)

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
        if name_entry.get() == "":
            messagebox.showerror("Error", "Please fill in the entry")
        else:
            if name_entry.get() in data:
                del data[name_entry.get()]
                messagebox.showinfo("Success", "Record for " + name_entry.get() + " has been deleted!")
            else:
                messagebox.showerror("Error", "No record for: " + name_entry.get())

    delete_button = Button(delete_window, text="Delete record", command=delete_record)

    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1, columnspan=3)
    delete_button.grid(row=1, column=0, columnspan=4)

def show_display():
    display_window = Toplevel(root)

    for key in data:
        key_label = Label(display_window, text=data[key].display())
        key_label.pack()
        separator_label = Label(display_window, text="------------------------------------------------------------------------------------------------------------------------")
        separator_label.pack()

edit = Button(root, text="Create/Edit Record", command=show_edit, width=30)
search = Button(root, text="Search Record", command=show_search, width=30)
delete = Button(root, text="Delete Record", command=show_delete, width=30)
display = Button(root, text="Display Record(s)", command=show_display, width=30)

edit.pack()
search.pack()
delete.pack()
display.pack()

root.mainloop()
data.close()