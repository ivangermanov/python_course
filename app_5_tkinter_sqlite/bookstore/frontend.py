from backend import Database
from tkinter import *

database=Database("books.db")

def view_all_command():
    list1.delete(0, END)
    for row in database.view_all():
        list1.insert(END, row)

def search_entry_command():
    list1.delete(0, END)
    for row in database.search_entry(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_entry_command():
    database.add_entry(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def get_selected_row(event):
    global selected_tuple 
    if list1.size() != 0:
        selected_tuple = list1.get(list1.curselection()[0])
        e_title.delete(0, END)
        e_title.insert(END, selected_tuple[1])
        e_author.delete(0, END)
        e_author.insert(END, selected_tuple[2])
        e_year.delete(0, END)
        e_year.insert(END, selected_tuple[3])
        e_isbn.delete(0, END)
        e_isbn.insert(END, selected_tuple[4])


def delete_selected_command():
    database.delete_selected(selected_tuple[0])

def update_selected_command():
    database.update_selected(selected_tuple[0], e_title.get(), e_author.get(), e_year.get(), e_isbn.get())

window=Tk()

window.wm_title("Bookstore")

lbl_title = Label(window, text="Title")
lbl_title.grid(row=0, column=0)

lbl_author = Label(window, text="Author")
lbl_author.grid(row=0, column=2)

lbl_year = Label(window, text="Year")
lbl_year.grid(row=1, column=0)

lbl_isbn = Label(window, text="ISBN")
lbl_isbn.grid(row=1, column=2)

title_text = StringVar()
e_title = Entry(window, textvariable=title_text)
e_title.grid(row=0, column=1)

author_text = StringVar()
e_author = Entry(window, textvariable=author_text)
e_author.grid(row=0, column=3)

year_text = StringVar()
e_year = Entry(window, textvariable=year_text)
e_year.grid(row=1, column=1)

isbn_text = StringVar()
e_isbn = Entry(window, textvariable=isbn_text)
e_isbn.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
list1.bind('<<ListboxSelect>>', get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b_view = Button(window, text="View all", width=12, command=view_all_command)
b_view.grid(row=2, column=3)

b_search = Button(window, text="Search entry", width=12, command=search_entry_command)
b_search.grid(row=3, column=3)

b_add = Button(window, text="Add entry", width=12, command=add_entry_command)
b_add.grid(row=4, column=3)

b_update = Button(window, text="Update", width=12, command=update_selected_command)
b_update.grid(row=5, column=3)

b_delete = Button(window, text="Delete", width=12, command=delete_selected_command)
b_delete.grid(row=6, column=3)

b_close = Button(window, text="Close", width=12, command=window.destroy)
b_close.grid(row=7, column=3)

window.mainloop()
