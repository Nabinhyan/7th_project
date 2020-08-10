fields = ('Date : \nYYYY-MM : ','Quantity : \n(in Kg) : ')
def database_saving(root, entries, called_item):
   date = str(entries['Date : \nYYYY-MM : '].get())
   quantity = float(entries['Quantity : \n(in Kg) : '].get())
   database(root, date, quantity, called_item)


def makeform(root, fields, called_item):
   entries = {}
   root.title("Add New Data of "+called_item)
   root.resizable(0,0)
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=12, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side = TOP, fill = X, padx = 3 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = LEFT, expand = YES, fill = X)
      entries[field] = ent
   return entries

def adding_popup(called_item):
	root = Tk()
	ents = makeform(root, fields, called_item)
	root.bind('<Return>', (lambda event, e = ents: fetch(e)))
	b1 = Button(root, text = 'Add Data',command=(lambda e = ents: database_saving(root, e, called_item)))
	b1.pack(side = LEFT, padx = 5, pady = 5)
	b3 = Button(root, text = 'Cancel Addition', command = root.destroy)
	b3.pack(side=RIGHT, padx=5, pady=5)
	root.mainloop()

def calling_process(button_title, called_item, menu_status, graph_status):
  global canvass
  if(button_title == "Add Data"):
    adding_popup(called_item)

  elif(button_title == "Reload Model"):
    model_status, staus_of_graph = model_calll(canvas, called_item, menu_status, button_title, graph_status)
    return model_status

  else:
    model_status, status_of_graph = model_calll(canvas, called_item, menu_status, button_title, graph_status)
    return model_status

def clearing_graph(graph_status):
  len_of_graph_staus = len(graph_status)
  for x in range(0,len_of_graph_staus):
    graph_status[x].get_tk_widget().grid_forget()
  graph_status.clear()

def design_menu(canvas, graph_status, menu_status, called_item):
  global  canvass
  if (len(graph_status) != 0):
    clearing_graph(graph_status)

  canvas.delete("all")
  x_axis = 57
  y_axis = 13
  button_title = ['Add Data', 'Scatter Graph', 'Line Graph', 'Reload Model']
  for button_title_content in range(len(button_title)):
    btn= Button(command =partial(calling_process,button_title[button_title_content], called_item, menu_status, graph_status), height=0, width = 11, text=button_title[button_title_content], bd = 3)
    btn.grid(row = 0, column = button_title_content, padx = 3)
    canvas1 = canvas.create_window(x_axis , y_axis, window = btn)
    x_axis += 115
    button.append(btn)

  def canvas_show_information(image_to_open, text_to_show):
    pic = Image.open(image_to_open)
    pic.putalpha(80)
    pic = pic.filter(ImageFilter.GaussianBlur(3))
    pic = ImageTk.PhotoImage(pic.resize((460,400)))
    canvas.create_image((0,30), image = pic, anchor = NW)
    canvas.image = pic
    canvas.create_text((130, 80), text = text_to_show, fill = 'green', anchor = 'nw')
    canvas.grid(columnspan = 4)
    return canvas
   
  if called_item == 'Rice':   
    screen.title("Prediction of Rice Import")
    c1 = canvas_show_information('img.jpg', "Rice_Nabin_hyanmikha")
  if called_item == 'Potato':   
    screen.title("Prediction of Potato Import")
    c1 = canvas_show_information('img.jpg', "Potato_Nabin_hyanmikha")
  if called_item == 'Apple':   
    screen.title("Prediction of Apple Import")
    c1 = canvas_show_information('img.jpg', "Apple_Nabin_hyanmikha")




def homepage(graph_status):
  if (len(graph_status) != 0):
    clearing_graph(graph_status)
  canvas.delete('all')
  _welcome=("verdana", 32, "bold")
  _prediction=("verdana", 28, "bold")
  _import_export=("verdana", 36, "bold")
  _to=("verdana", 24)
  pic = Image.open('img.jpg')
  pic.putalpha(80)
  pic = pic.filter(ImageFilter.GaussianBlur(3))
  photo = ImageTk.PhotoImage(pic.resize((460,430)))
  canvas.create_image((0,0), image = photo, anchor = NW)
  canvas.image = photo
  canvas.create_text((130, 80), font=(_welcome), text = 'WELCOME', fill = 'green', anchor = 'nw')
  canvas.create_text((200, 130), font=(_to), text = 'to', fill = 'green', anchor = 'nw')
  canvas.create_text((20, 175), font=(_import_export), text = 'IMPORT', fill = 'green', anchor = 'nw')
  canvas.create_text((215, 185), font=(_to), text = '&', fill = 'green', anchor = 'nw')
  canvas.create_text((250, 175), font=(_import_export), text = 'Export', fill = 'green', anchor = 'nw')
  canvas.create_text((30, 250), font=(_prediction), text = 'Prediction System', fill = 'green', anchor = 'nw')
  canvas.grid()
  return canvas

from headers import *
button = []
graph_status = []
global canvas, canvass
screen = Tk()
screen.configure(bg = 'gray')
canvas = Canvas(screen, width = 460, height = 400)

canvas = homepage(graph_status)

menu = Menu(screen)
screen.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label = 'Home', command = partial(homepage, graph_status)) 
filemenu.add_separator()
submenu_imp=Menu(filemenu)
submenu_imp.add_command(label="Rice", command = partial(design_menu, canvas, graph_status, 0,"Rice"))
submenu_imp.add_command(label="Potato", command = partial(design_menu, canvas, graph_status, 0,"Potato"))
submenu_imp.add_command(label="Apple", command = partial(design_menu, canvas, graph_status, 0,"Apple"))
submenu_imp.add_separator()
filemenu.add_cascade(label='Import', menu=submenu_imp, underline=0) 
submenu_exp=Menu(filemenu)
submenu_exp.add_command(label="Tea")
submenu_exp.add_separator()
filemenu.add_cascade(label='Export', menu=submenu_exp, underline=0) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=screen.destroy) 
helpmenu = Menu(menu) 
menu.add_command(label='About')
menu.add_command(label = 'Contact Us') 
screen.resizable(0, 0) 
screen.mainloop()