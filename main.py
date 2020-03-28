# importing only those functions 
# which are needed 

from headers import *
canvas_width = 700
canvas_height =500


# creating tkinter window 
root =tk.Tk() 
menu = Menu(root) 
root.title("Import Export")
root.config(menu=menu) 
filemenu = Menu(menu) 
canvas = Canvas(root, 
           width=canvas_width, 
           height=canvas_height)

def show_entry_fields(e1,e2):
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))


def add_one():
	master = tk.Tk()
	tk.Label(master, 
	         text="First Name").grid(row=0)
	tk.Label(master, 
	         text="Last Name").grid(row=1)

	e1 = tk.Entry(master)
	e2 = tk.Entry(master)

	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)

	tk.Button(master, 
	          text='Quit', 
	          command=master.quit).grid(row=3, 
	                                    column=0, 
	                                    sticky=tk.W, 
	                                    pady=4)
	tk.Button(master, 
	          text='Show', command=show_entry_fields(e1,e2)).grid(row=3, 
	                                                       column=1, 
	                                                       sticky=tk.W, 
	                                                       pady=4)

	tk.mainloop()
menu.add_cascade(label='File', menu=filemenu) 

submenu_imp=Menu(filemenu)
submenu_imp.add_command(label="Rice")
submenu_imp.add_command(label="something")
submenu_imp.add_separator()

filemenu.add_cascade(label='Import', menu=submenu_imp, underline=0) 

submenu_exp=Menu(filemenu)
submenu_exp.add_command(label="Alaichi")
submenu_exp.add_separator()

filemenu.add_cascade(label='Export', menu=submenu_exp, underline=0) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.destroy) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 

toolbar=Frame(root) 
frame = tk.Frame(root)
frame.pack(fill='both', expand=False)

# Creating a photoimage object to use image 
photo = PhotoImage(file = "add.png") 
# Resizing image to fit on button 
photoimage1 = photo.subsample(6,6) 
# here, image option is used to set image on button compound option is used to align image on LEFT side of button 
#Button(root,text = 'Add Data', image = photoimage1, compound = LEFT).pack(side =LEFT) 
button = tk.Button(toolbar,image = photoimage1, compound = LEFT,command = add_one)
button.pack(side=tk.LEFT)
# Creating a photoimage object to use image 
photo = PhotoImage(file = r"scatter.png") 
# Resizing image to fit on button
photoimage2 = photo.subsample(12,12) 
# here, image option is used to set image on button compound option is used to align image on LEFT side of button 
button=tk.Button(toolbar, image = photoimage2, compound = LEFT)
button.pack(side=tk.LEFT)
# Creating a photoimage object to use image 
photo = PhotoImage(file = r"line.png") 
# Resizing image to fit on button
photoimage3 = photo.subsample(12,12) 
# here, image option is used to set image on button compound option is used to align image on LEFT side of button 
button=tk.Button(toolbar, image = photoimage3, compound = LEFT)
button.pack(side=tk.LEFT) 
toolbar.pack(side=TOP, fill=X)





canvas.pack()
root.mainloop() 