import tkinter as tk #makes it possible to use tkinter to create a gui
from tkinter import *

detail_file = "details.txt"
positions = {}
linecount = 0
lines = []
hire_correct = False

def view_in_fields(event):

    selected = listbox_of_hires.curselection()
    if not selected:
        return
    index = selected[0]

    with open(detail_file, "r") as f:
        lines = f.readlines()

    client_data = [lines[index * 5 + i][:-1] for i in range(4)]

    def change_entry(entry, value, placeholder_text):
        entry.delete(0, END)
        entry.insert(0, value)
        entry.config(fg="white")

    change_entry(name_field, client_data[0], "Name")
    change_entry(receipt_field, client_data[1], "Receipt")
    change_entry(item_field, client_data[2], "Item")
    change_entry(quantity_field, client_data[3], "Quantity")

def refresh():
    listbox_of_hires.delete(0, tk.END)
    with open(detail_file, "r") as f:
        lines = f.readlines()
    for i in range(0, len(lines), 5):
        listbox_of_hires.insert("end", (lines[i])[:-1])

def new_hire(): #When someone hires something new this code will run and ensure that the correct details are put in
    name = ""
    receipt = 0
    item = ""
    quantity = 0
    hire_correct = True

    if name_field.get().strip() == "":
        veiwable_text.set("Name cannot be empty")

    elif receipt_field.get().strip() == "":
        veiwable_text.set("Receipt cannot be empty")

    elif receipt_field.get().isdigit() == False:
        veiwable_text.set("Receipt must be a number")

    elif item_field.get().strip() == "":
        veiwable_text.set("Item cannot be empty")

    elif quantity_field.get().strip() == "":
        veiwable_text.set("Quantity cannot be empty")

    elif quantity_field.get().isdigit() == False:
        veiwable_text.set("Quantity must be a number")

    elif int(quantity_field.get()) < 0 or int(quantity_field.get()) > 500:
        veiwable_text.set("Quantity must be 0-500")

    else:
        print(f"Name: {name_field.get()}, Receipt: {receipt_field.get()}, Item: {item_field.get()}, Quantity: {quantity_field.get()}")
        with open(detail_file, "a") as f:
            f.write(f"{name_field.get()}\n{receipt_field.get()}\n{item_field.get()}\n{quantity_field.get()}\n\n")
        name_field.delete(0, END)
        receipt_field.delete(0, END)
        item_field.delete(0, END)
        quantity_field.delete(0, END)
        veiwable_text.set("Hire added successfully")
        refresh()

def delete():
    selected = listbox_of_hires.curselection()
    if not selected:
        return
    selected = selected[0]

    listbox_of_hires.delete(selected)

    with open(detail_file, "r") as f:
        lines = f.readlines()

    start = selected * 5
    end = start + 5

    del lines[start:end]

    with open(detail_file, "w") as f:
        f.writelines(lines)

def placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg="grey")

    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, END)
            entry.config(fg="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder_text)
            entry.config(fg="grey")
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

root = tk.Tk()
root.title("Julie's Party Hire") #creates blank window named Julies party hire
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(0, weight=0)


veiwable_text = tk.StringVar()
veiwable_text.set("")

action_bar = tk.Frame(root)
action_bar.grid(row=0, column=0, columnspan=2, sticky="ew")

action_bar.columnconfigure(0, weight=1)

content = tk.Frame(root)
content.grid(row=1, column=0, columnspan=2, sticky="nsew")

fields = tk.Frame(content)
fields.grid(row=0, column=0, sticky="n")

name_field = tk.Entry(fields)
name_field.grid(row=0, column=0)
placeholder(name_field, "Name")

receipt_field = tk.Entry(fields)
receipt_field.grid(row=1, column=0)
placeholder(receipt_field, "Receipt")

item_field = tk.Entry(fields)
item_field.grid(row=2, column=0)
placeholder(item_field, "Item")

quantity_field = tk.Entry(fields)
quantity_field.grid(row=3, column=0)
placeholder(quantity_field, "Quantity")



all_hires = Frame(content)
all_hires.grid(row=0, column=1, sticky="nsew")

listbox_of_hires = Listbox(all_hires)
listbox_of_hires.grid(row=0, column=0, sticky="nsew")

content.columnconfigure(1, weight=1)
content.rowconfigure(0, weight=1)

all_hires.columnconfigure(0, weight=1)
all_hires.rowconfigure(0, weight=1)

delete_button = Button(action_bar, text="delete", command=delete)
delete_button.grid(row=0, column=0, sticky="ew")

add_hire_button = Button(action_bar, text="add", command=new_hire)
add_hire_button.grid(row=0, column=1, sticky="ew")

action_bar.columnconfigure(1, weight=1)
action_bar.columnconfigure(2, weight=1)

refresh_button = Button(action_bar, text="refresh", command=refresh)
refresh_button.grid(row=0, column=2, sticky="ew")

text = tk.Label(fields, textvariable=veiwable_text)
text.grid(row=4, column=0)

listbox_of_hires.bind("<<ListboxSelect>>", view_in_fields)

refresh()
#text_list = tk.Listbox(frame2)
#text_list.grid(row=1, column=0, columnspan=2, sticky="nsew")
root.mainloop() #stops window from immediatly closing

