from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox

#colors
co0 = "#ffffff"
co1 = "#000000"
co2 = "#4456F0"

window = Tk()
window.title ("")
window.iconbitmap('D:\Dossier_Onedrive\OneDrive\Desktop')
window.geometry('485x450')
window.configure(background=co0)
window.resizable(width=False, height=False)

#frames
frame_up = Frame(window, width=500, height=50, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=500, height=150, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=500, height=100, bg=co0, relief="flat")
frame_table.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

#functions
def show():
    global tree

    list_header = ['Name', 'Gender', 'Telephone', 'Email']

    demo_list = view()

    tree = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show="headings")
    
    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    #tree head
    tree.heading(0, text='Name', anchor=NW)
    tree.heading(1, text='Gender', anchor=NW)
    tree.heading(2, text='Telephone', anchor=NW)
    tree.heading(3, text='Email', anchor=NW)

    #tree columns
    tree.column(0, width=120, anchor='nw')
    tree.column(1, width=50, anchor='nw')
    tree.column(2, width=100, anchor='nw')
    tree.column(3, width=180, anchor='nw')

    for item in demo_list:
        tree.insert('', 'end', values=item)

show()

def insert():
    Name = e_name.get()
    Gender = c_gender.get()
    Telephone = e_tel.get()
    Email = e_email.get()

    data = [Name, Gender, Telephone, Email]

    if Name == '' or Gender == '' or Telephone == '' or Email == '':
        messagebox.showwarning('data', 'Please, fill all the fields !')
    
    else:
        add(data)
        messagebox.showinfo('data', 'Data added succesfully')
        
        e_name.delete(0, 'end')
        c_gender.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_email.delete(0, 'end')
        
        show()

def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']

        Name = str(tree_list[0])
        Gender = str(tree_list[1])
        Telephone = str(tree_list[2])
        Email = str(tree_list[3])

        e_name.insert(0, Name)
        c_gender.insert(0, Gender)
        e_tel.insert(0, Telephone)
        e_email.insert(0, Email)

        def confirm():
            new_name = e_name.get()
            new_gender = c_gender.get()
            new_telephone = e_tel.get()
            new_email = e_email.get()

            data = [new_telephone, new_name, new_gender, new_telephone, new_email]

            update(data)

            messagebox.showinfo('Success', 'Data updated successfully !')

            e_name.delete(0, 'end')
            c_gender.delete(0, 'end')
            e_tel.delete(0, 'end')
            e_email.delete(0, 'end')

            for widget in frame_table.winfo_children():
                widget.destroy()

            b_confirm.destroy()

            show()

        b_confirm = Button(frame_down, text="Confirm", width=10, height=1, bg=co2, fg=co0, font=('Ivy 8 bold'), command=confirm())
        b_confirm.place(x=290, y=110)
    
    except IndexError:
        messagebox.showerror('Error', 'Select one item from the table')

#frame_up widgets

app_name = Label(frame_up, text="Phonebook", height = 1, font=('Verdana 17 bold'), bg=co2, fg = co0)
app_name.place(x=5, y=7)

#frame_dowm widgets
#label input1
l_name = Label(frame_down, text="Name *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_name.place(x=10, y=20)
#Entry input1
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_name.place(x=80, y=20)

#label input2
l_gender = Label(frame_down, text="Gender *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_gender.place(x=10, y=50)
#Entry input2
c_gender = ttk.Combobox(frame_down, width=27)
c_gender['values'] = ['', 'M', 'F', 'O']
c_gender.place(x=80, y=50)

#label input3
l_tel = Label(frame_down, text="Tel *", height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_tel.place(x=10, y=80)
#Entry input3
e_tel = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_tel.place(x=80, y=80)

#label input4
l_email = Label(frame_down, text="Email *", height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_email.place(x=10, y=110)
#Entry input4
e_email = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_email.place(x=80, y=110)

#search button
b_search = Button(frame_down, text="Search", height=1, bg=co2, fg=co0, font=('Ivy 8 bold'))
b_search.place(x=290, y=20)
e_search = Entry(frame_down, width=16, justify='left', font=('Ivy', 11), highlightthickness=1, relief="solid")
e_search.place(x=347, y=20)

#view button
b_view = Button(frame_down, text="View",width=10, height=1, bg=co2, fg=co0, font=('Ivy 8 bold'))
b_view.place(x=290, y=50)

#Add button
b_add = Button(frame_down, text="Add", width=10, height=1, bg=co2, fg=co0, font=('Ivy 8 bold'), command=insert)
b_add.place(x=400, y=50)

#Update button
b_update = Button(frame_down, text="Update", width=10, height=1, bg=co2, fg=co0, font=('Ivy 8 bold'), command=to_update)
b_update.place(x=400, y=80)

#Delete button
b_delete = Button(frame_down, text="Delete", width=10, height=1, bg=co2, fg=co0, font=('Ivy 8 bold'))
b_delete.place(x=400, y=110)

window.mainloop() 