from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

def populate_list():
    item_list.delete(0,END)
    for row in db.fetch():
        item_list.insert(END, row)

def add_item():
    if item_text.get() == '' or date_text.get() == '' or buying_price_text.get() == '' or selling_price_text.get() == '':
        messagebox.showinfo('Required Fields','Please enter all fields')
        return
    db.insert(item_text.get(),date_text.get(),buying_price_text.get(),selling_price_text.get())
    item_list.delete(0,END)
    item_list.insert(END, (item_text.get(),date_text.get(),buying_price_text.get(),selling_price_text.get()))
    clear_text()
    populate_list()
    

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()
    
def update_item():
    db.update(selected_item[0],item_text.get(),date_text.get(),buying_price_text.get(),selling_price_text.get())
    populate_list()

def clear_text():
    item_entry.delete(0, END)
    date_entry.delete(0, END)
    buying_price_entry.delete(0, END)
    selling_price_entry.delete(0, END)

def select_item(event):
    try:
        global selected_item
        index = item_list.curselection()[0]
        selected_item = item_list.get(index)

        item_entry.delete(0, END)
        item_entry.insert(END, selected_item[1])

        date_entry.delete(0, END)
        date_entry.insert(END, selected_item[2])

        buying_price_entry.delete(0, END)
        buying_price_entry.insert(END, selected_item[3])
    except index:
        pass


    selling_price_entry.delete(0, END)
    selling_price_entry.insert(END, selected_item[4])

#Create Window Object 
app = Tk()

#Item 
item_text = StringVar()
item_label = Label(app, text= 'Item Name',font=('bold', 15), pady = 20)
item_label.grid(row = 0, column = 0)
item_entry = Entry(app, textvariable = item_text)
item_entry.grid(row = 0,column = 1,sticky = W)

#Date 
date_text = StringVar()
date_label = Label(app, text= 'Date',font=('bold', 15), pady = 20)
date_label.grid(row = 0, column = 2)
date_entry = Entry(app, textvariable = date_text)
date_entry.grid(row = 0,column = 3,sticky = W)

#Buying Price 
buying_price_text = StringVar()
buying_price_label = Label(app, text= 'Buying Price',font=('bold', 15), pady = 20)
buying_price_label.grid(row = 1, column = 0)
buying_price_entry = Entry(app, textvariable = buying_price_text)
buying_price_entry.grid(row = 1,column = 1,sticky = W)

#Selling Price 
selling_price_text = StringVar()
selling_price_label = Label(app, text= 'Selling Price',font=('bold', 15), pady = 20)
selling_price_label.grid(row = 1, column = 2)
selling_price_entry = Entry(app, textvariable = selling_price_text)
selling_price_entry.grid(row = 1,column = 3,sticky = W)

#Add Buttons
add_btn = Button(app, text= 'Add Item',width = 10, command= add_item, bg = 'blue')
add_btn.grid(row = 2, column = 0, pady = 20)

remove_btn = Button(app, text= 'Remove Item',width = 10, command= remove_item)
remove_btn.grid(row = 2, column = 1,)

update_btn = Button(app, text= 'Update Item',width = 10, command= update_item)
update_btn.grid(row = 2, column = 2)

clear_btn = Button(app, text= 'Clear Input',width = 10, command= clear_text)
clear_btn.grid(row = 2, column = 3)

#Item List
item_list = Listbox (app, height= 15, width = 60)
item_list.grid(row = 3, column = 0, pady=10,padx = 10 , columnspan= 5,rowspan = 7 )

#Bind selct item
item_list.bind('<<ListboxSelect>>', select_item)

#Creating a scrollbar
Scrollbar = Scrollbar(app)
Scrollbar.grid(row = 3, column = 5)

#Setting Scrolbar to listbox
item_list.configure(yscrollcommand = Scrollbar.set)
Scrollbar.configure(command=item_list.yview)


app.title('Olarry Tech Manager')
app.geometry('600x500')
app.configure(background="powder blue")

#Populating Data 
populate_list()
 
#Starting the program
app.mainloop()


