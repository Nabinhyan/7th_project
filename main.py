from headers import *

fields = ('Date','Quantity')
def monthly_payment(entries, passed_value):
   # period rate:
   # principal loan:
   print(passed_value)
   date = str(entries['Date'].get())
   quantity = float(entries['Quantity'].get())
   database(date, quantity, passed_value)
   # return loan

def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      # ent.insert(0,"0")
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries[field] = ent
   return entries

def showimg(passed_value):
	# print(passed_value)
	root = Tk()
	ents = makeform(root, fields)
	root.bind('<Return>', (lambda event, e = ents: fetch(e)))
	b1 = Button(root, text = 'Final Balance',
	  command=(lambda e = ents: monthly_payment(e, passed_value)))
	b1.pack(side = LEFT, padx = 5, pady = 5)
	b3 = Button(root, text = 'Quit', command = root.destroy)
	b3.pack(side = LEFT, padx = 5, pady = 5)
	root.mainloop()



def menu_show(main_select):

	global main_pass
	main_pass = main_select
	toolbar=Frame(screen) 
	frame = Frame(screen)
	frame.pack(fill='both', expand=False)
	# print(main_select)
	# x = '{}{}'.format(main_select,1)
	button = Button(toolbar,text="Add New", compound = LEFT, command = partial(showimg,main_pass))
	button.pack(side=LEFT)
	
	button=Button(toolbar, text="Scatter Graph", compound = LEFT)
	button.pack(side=LEFT)

	button=Button(toolbar, text="Line Graph", compound = LEFT)
	button.pack(side=LEFT) 
	toolbar.pack(side=TOP, fill=X)
	canvas.pack()



	


def main_screen():
	global screen
	global canvas
	# global main_select
	screen = Tk()
	screen.title("xyz")
	screen.geometry("450x400")
	menu = Menu(screen)
	canvas = Canvas(screen, 
           width=450, 
           height=400)
	screen.config(menu=menu) 
	filemenu = Menu(menu) 
	menu.add_cascade(label='File', menu=filemenu) 

	submenu_imp=Menu(filemenu)
	submenu_imp.add_command(label="Rice", command = partial(menu_show,1))
	submenu_imp.add_command(label="something", command = partial(menu_show,2))
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

	screen.mainloop()

main_screen()