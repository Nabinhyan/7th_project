fields = ('Date','Quantity')
def database_saving(entries, called_item):
   date = str(entries['Date'].get())
   quantity = float(entries['Quantity'].get())
   database(date, quantity, called_item)

def makeform(root, fields, called_item):
   entries = {}
   root.title("Add New Data of "+called_item)

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
	b3.pack(side = RIGHT, padx = 5, pady = 5)
	root.mainloop()





def calling_process(passed_value, called_item):
    global model_status

    if(passed_value == "Add Data"):
        adding_popup(called_item)
    else:
        model_status = model_calll(screen, model_status,called_item, passed_value)
        return model_status
#    elif(passed_value == "Line Graph"):
#        model_status = model_calll(screen, model_status,called_item, "Line Graph")
#        return model_status
def design_menu(menu_status, called_item):
    global screen
    print(called_item)
#    if(menu_status == 1):
#        for btn in buttons:
#            btn.destroy()
##        return menu_status

    button_title = ['Add Data', 'Scatter Graph', 'Line Graph']
    for button_title_content in range(len(button_title)):
#        padding_value = padding_value + 90
        btn = Button(command =partial(calling_process, button_title[button_title_content], called_item), height=0, width = 12, relief=RIDGE, text=button_title[button_title_content], bd = 2)
        btn.grid(row=0, column=button_title_content, padx = 2)
        buttons.append(btn)
    
    menu_status = 1
#    return menu_status

from headers import *

buttons = []
menu_status1 = 0
menu_status2 = 0
model_status = 0
screen = Tk()
screen.title("xyz")
screen.geometry("420x360")
menu = Menu(screen)
screen.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
submenu_imp=Menu(filemenu)
submenu_imp.add_command(label="Rice", command = partial(design_menu, menu_status1,"Rice"))
submenu_imp.add_command(label="Potato", command = partial(design_menu, menu_status2,"Potato"))
submenu_imp.add_command(label="Apple", command = partial(design_menu, menu_status2,"Apple"))
submenu_imp.add_separator()
filemenu.add_cascade(label='Import', menu=submenu_imp, underline=0) 
submenu_exp=Menu(filemenu)
submenu_exp.add_command(label="Alaichi")
submenu_exp.add_separator()
filemenu.add_cascade(label='Export', menu=submenu_exp, underline=0) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=screen.destroy) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About')
screen.resizable(0, 0) 
screen.mainloop()

