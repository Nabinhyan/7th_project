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
  for x in range(len(graph_status)):
    graph_status[x].get_tk_widget().grid_forget()
  graph_status = []

def canvas_show_information(image_to_open, text_to_show):
  pic = Image.open(image_to_open)
  pic.putalpha(80)
  pic = pic.filter(ImageFilter.GaussianBlur(2))
  pic = ImageTk.PhotoImage(pic.resize((460,400)))
  canvas.create_image((0,28), image = pic, anchor = NW)
  canvas.image = pic
  text_id = canvas.create_text((1, 38),font = ("verdana", 11, "bold"), text = text_to_show, fill = 'green', anchor = 'nw')
  coords = canvas.bbox(text_id)
  xOffset = (460 / 2) - ((coords[2] - coords[0]) / 2)
  canvas.move(text_id, xOffset, 0)
  canvas.grid(columnspan = 4)
  return canvas

def clearing_canvas(canvas):
  if (len(graph_status) != 0):
    clearing_graph(graph_status)
  canvas.delete("all")  

def design_menu(canvas, graph_status, menu_status, called_item):
  global  canvass
  clearing_canvas(canvas)
  x_axis = 57
  y_axis = 13
  button_title = ['Add Data', 'Scatter Graph', 'Line Graph', 'Reload Model']
  for button_title_content in range(len(button_title)):
    btn= Button(command =partial(calling_process,button_title[button_title_content], called_item, menu_status, graph_status), height=0, width = 11, text=button_title[button_title_content], bd = 3)
    btn.grid(row = 0, column = button_title_content, padx = 3)
    canvas1 = canvas.create_window(x_axis , y_axis, window = btn)
    x_axis += 115
    button.append(btn) 
  if called_item == 'Rice':   
    screen.title("Prediction of Rice Import")
    c1 = canvas_show_information('imgs/imp_rice.jpg', rice)
  if called_item == 'Potato':   
    screen.title("Prediction of Potato Import")
    c1 = canvas_show_information('imgs/imp_potato.jpg', potato)
  if called_item == 'Apple':   
    screen.title("Prediction of Apple Import")
    c1 = canvas_show_information('imgs/imp_apple.jpg', apple)

def homepage(canvas, graph_status):
  clearing_canvas(canvas)
  _welcome=("verdana", 32, "bold")
  _prediction=("verdana", 28, "bold")
  _import_export=("verdana", 36, "bold")
  _to=("verdana", 24)
  pic = Image.open('imgs/img.jpg')
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

def about_us(canvas, graph_status):
  clearing_canvas(canvas)
  pic = Image.open('imgs/aboutus.jpg')
  pic.putalpha(80)
  pic = pic.filter(ImageFilter.GaussianBlur(2))
  pic = ImageTk.PhotoImage(pic.resize((460,400)))
  canvas.create_image((0,0), image = pic, anchor = NW)
  canvas.image = pic
  text_id = canvas.create_text((5, 9),font = ("verdana", 11, "bold"), text = about, fill = 'blue', anchor = 'nw')
  coords = canvas.bbox(text_id)
  xOffset = (460 / 2) - ((coords[2] - coords[0]) / 2)
  canvas.move(text_id, xOffset, 0)
  canvas.grid(columnspan = 4)


from headers import *
import os

button = []
graph_status = []
global canvas, canvass
screen = Tk()
screen.configure(bg = 'gray')
if 'nt' == os.name:
  screen.wm_iconbitmap('imgs/logo.ico')
else: 
  screen.wm_iconbitmap('@imgs/logo.xbm')
  
screen.title('Import Export Prediction System')
canvas = Canvas(screen, width = 460, height = 400)
canvas = homepage(canvas, graph_status)

menu = Menu(screen)
screen.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label = 'Home', command = partial(homepage, canvas, graph_status)) 
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
menu.add_command(label='About Us', command = partial(about_us, canvas, graph_status))
screen.resizable(0, 0) 
screen.mainloop()