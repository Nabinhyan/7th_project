fields = ('Date','Quantity')
def database_saving(entries, called_item):
   date = str(entries['Date'].get())
   quantity = float(entries['Quantity'].get())
   database(date, quantity, called_item)

def makeform(root, fields, called_item):
   entries = {}
   root.title("Add New Data of "+called_item)
   root.resizable(0,0)
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=7, text=field+": ", anchor='w')
      ent = Entry(row)
      # ent.insert(0,"0")
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = LEFT, expand = YES, fill = X)
      entries[field] = ent
   return entries

def adding_popup(called_item):
	# print(passed_value)

	root = Tk()
	ents = makeform(root, fields, called_item)
	root.bind('<Return>', (lambda event, e = ents: fetch(e)))
	b1 = Button(root, text = 'Add Data',
	  command=(lambda e = ents: database_saving(e, called_item)))
	b1.pack(side = LEFT, padx = 5, pady = 5)
	b3 = Button(root, text = 'Cancel Addition', command = root.destroy)
	b3.pack(side=RIGHT, padx=5, pady=5)
	root.mainloop()





def calling_process(passed_value, called_item, model_status):
    
#    model_staus = menu_status
    print(model_status)
    print(passed_value)
    if(passed_value == "Add Data"):
        adding_popup(called_item)
    elif(passed_value == "Reload Model"):
        model_status = model_calll(screen, called_item, model_status, passed_value)
        print(model_status)
    else:
        model_status = model_calll(screen,
                               called_item, model_status, passed_value)
        print(model_status)
        return model_status
#    elif(passed_value == "Line Graph"):
#        model_status = model_calll(screen, model_status,called_item, "Line Graph")
#        return model_status
def design_menu(note_status, menu_status, called_item,welcome_note):
    global screen
    print(called_item)
    for x in range(len(welcome_note)):
        welcome_note[x].destroy()

    if len(note_status) != 0:
        for x in range(len(note_status)):
            note_status[x].destroy()
        
        
        
    button_title = ['Add Data','Scatter Graph', 'Line Graph','Reload Model']
    for button_title_content in range(len(button_title)):
#        padding_value = padding_value + 90
        btn = Button(command =partial(calling_process, button_title[button_title_content], called_item, menu_status), height=0, width = 11, relief=RIDGE, text=button_title[button_title_content], bd = 3)
        btn.grid(row=0, column=button_title_content, padx = 3)
        buttons.append(btn)
    print(menu_status)
    
    if called_item == 'Rice':   
        lbl2 = Label(screen, text="This is rice Label", fg='red', bg = 'gray', font=("-weight bold", 16, "bold"), padx = 20, pady = 40)
        lbl2.grid(columnspan = 4)
        note_status.append(lbl2)
        return note_status
    if called_item == 'Potato':
        lbl2 = Label(screen, text="This is potato Label", fg='red', bg = 'gray', font=("-weight bold", 16, "bold"), padx = 20, pady = 40)
        lbl2.grid(columnspan = 4)
        note_status.append(lbl2)
        return note_status
    if called_item == 'Apple':   
        lbl2 = Label(screen, text="This is apple Label", fg='red', bg = 'gray', font=("-weight bold", 16, "bold"), padx = 20, pady = 40)
        lbl2.grid(columnspan = 4)
        note_status.append(lbl2)
        return note_status
    
    
def homepage(screen):
    lbl1=Label(screen, text="This is Label widget", fg='red',bg = 'gray', font=("-weight bold", 16, "bold"), padx = 20, pady = 20)
    lbl2 = Label(screen, text="This is Label widget", fg='red', bg = 'gray', font=("-weight bold", 16, "bold"), padx = 20, pady = 40)
    lbl1.grid()
    lbl2.grid()
    welcome_note = [lbl1, lbl2]
    return welcome_note


from headers import *

buttons = []
note_status = []
screen = Tk()
screen.configure(bg = 'gray')
welcome_note = homepage(screen)


screen.title("Import & Export of Agricultural Product")
screen.geometry("460x400")
menu = Menu(screen)
screen.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
submenu_imp=Menu(filemenu)
submenu_imp.add_command(label="Rice", command = partial(design_menu, note_status, 0,"Rice",welcome_note))
submenu_imp.add_command(label="Potato", command = partial(design_menu,note_status, 0,"Potato",welcome_note))
submenu_imp.add_command(label="Apple", command = partial(design_menu,note_status, 0,"Apple",welcome_note))
submenu_imp.add_separator()
filemenu.add_cascade(label='Import', menu=submenu_imp, underline=0) 
submenu_exp=Menu(filemenu)
submenu_exp.add_command(label="Alaichi")
submenu_exp.add_separator()
filemenu.add_cascade(label='Export', menu=submenu_exp, underline=0) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=screen.destroy) 
helpmenu = Menu(menu) 
menu.add_command(label='About')
menu.add_command(label = 'Contact Us') 

screen.resizable(0, 0) 
screen.mainloop()

