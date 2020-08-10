about = """Welcome to Import and Export Prediction System


This “Import and Export Prediction System” is 
prediction  system,  designed  to  predict  and
forecast the future import and export values of
various  agricultural  products  of Nepal. This 
system  evaluates  the   trend  of  import  and
exports of top listed  agricultural products on
basis  of time  series  since 2009.The data for
predicted  products  are  collected from Export
Import Data  Bank,  Undertaking  of  Trade  and
Export Promotion  Center Nepal. This  System is
simple prototype of time series trend  analysis
and prediction, proposed to visualize the trend
and predict values of agricultural goods coming
in and going out, using  the  concept  of ARIMA
model.   And  finally,   to   per-evaluate  the
increase in trade imbalance of the products.

This  is  proposed  and designed for the partial
fulfillment  of  requirements  for the degree of
Bachelor of Engineering in Computer Engineering.
All  the  feedback  and  comments  are  heartily
welcomed. Necessary features will be enhanced in

future.    """

rice = """              ---Import of Rice---              


Nearly 70  percent of Nepal's population depends
directly   on   agirculture,   and   the  sector
contributes more than a  quater of the country's
GDP - with  rice  making  up 21 percent of that.
Till as  late as 1985,  Nepal  used to  be a net
exproter  of  rice,  and  during  the  1960s the
country was  exporting $45 million worth of rice
to India every year. How the tables have turned,
in 2015 Neapl has to import 531,000 tons of rice
worth $210 million form India.

There are many reasons why Nepal’s production of
rice has not kept up with demand. The  foremost,
of course, is that the country’s  population has
doubled  in the  intervening years. Agricultural
land is  shrinking  because of urban sprawl, and
much  of  the  farms  are  fallow    because  of
outmigration.  The educated youth do not want to
live off the land anymore, and look for salaried
jobs in the  cities or abroad."""



potato = """             ---Import of Potato---              


Potato  is considered  as one of the fourth most
important  crops in the  world after wheat, rice
and maize. It is one of the important cash crops
to address  food  insecurity  and reduce poverty
among  smallholder  farmers  in  the  developing
countries like Nepal. Its cultivation is popular
among  farmers  due  to its  wider adaptability,
high  yield  potential  and  high  demand  which
contributes about  6.57 and 2.17 precent in AGDP
and GDP, respectively. Potato is cultivated as a
subsistence crop which is the best potential for
yield increment. 

Potatoes are used as  subsidiary food as part of
vegetables in Terai  region,  whereas  as staple
food in Hill and Mountain regions. The demand of
potato  in the form of  chips, fries  and mashed
potatoes  has widened  its scope  which helps to
uplift  the  economic condition  of  smallholder
farmers. """


apple = """             ---Import of Apple---              


Aside from seeing diverse landscape and abundant
wildlife  and   learning  about   vibrant  local
culture  and traditions, there is another reason
to  head  to  the  far-western Nepali highlands.
That is to enjoy locally-grown  apples and apple
products  direct from  the source, while walking
through  sloping  apple  orchards, picking fresh
apples, or munching on this  healthy fruit while
trekking.

The fact  that apple is a major import commodity
among  fruits  shows  the country  does not have
enough potential  to cater to  the local demand.
The country’s annual  production of apples stood
at 35,920 tonnes last fiscal, according to MoAD.
Apples are  cultivated in 48 districts, but five
districts   —  Jumla,  Humla,  Mugu,  Dolpa  and
Kalikot — contribute  41.2 percent  of the total
production."""

tea = """             ---Export of Tea---              


Nepal  has  a  long  history of Tea cultivation,
initiated  with the  establishment  of  Ilam Tea
Estate  in the Hills of Ilam  District. Orthodox
and  CTC  are  major  varieties  of tea grown in
Nepal. Illam  tea  which is famous as high grown
orthodox    tea    is   popular  among  the  tea
connoisseur.  

Nepal’s total tea  production  amounts to 23,821
MT  annually.  Tea  is primarily  grown  in five
districts  in Eastern Nepal namely, Jhapa, Ilam,
Panchthar, Dhankuta, and  Terathum.  Jhapa is by
far  the largest  producer of tea accounting for
more than  75 percent  of  Nepal’s  tea produced
followed by Ilam  with produces around one-sixth
of  Nepal’s  total  tea  production.  The  major
export  market  of  Nepalese  tea  are  Germany,
Japan,   France,   Italy,   Hong   Kong,   U.K.,
Switzerland,   Australia,  Netherlands,  U.S.A.,
The medicated and  herbal tea of Nepal have been
very popular in these markets."""


alainchi = """             ---Export of Alainchi---              

 Nepal  has  a  long  history  of Tea cultivation,
 Nepali large cardamom  also known as 'black gold'
 or 'black cardamom' and  locally  called elaichi.
 Large cardamoms are spindle-shaped  pods that are
 light  to   dark   brown  in  color.   It  is  an
 evergreen, perennial  and herbaceous  plant grown
 on north-facing  hill slopes. This type  of large
 cardamom is grown mainly in the Himalayan  region
 of  Nepal,  Sikkim   and   Bhutan.  Nepali  black
 cardamom has a distinct  flavor  profile due to a
 specific method  of postharvest  drying in Bhatti
 ovens. 
 Cardamoms produced in Nepal are  entirely organic
 and provide income to  mostly low-income families
 in  rural  Nepal.  Large  cardamom  is the second
 largest  export  commodity  and the  largest agro
 based export  of Nepal. Large  cardamom  is grown
 predominantly   in    Eastern  Nepal  where  four
 districts    Taplejung,   Panchthar,   Ilam,  and
 Sankhuwasabha  account for  more  than 80 precent
 of  national  production.  India  is  the largest
 importer of large cardamom from  Nepal."""


herbs = """             ---Export of Herbs---              

Nepal,  a  small  country  in  middle of the great
Himalayan  range,   is  famous   for  her  natural
medicinal  plants and  herbs. Due to many climatic
conditions  from  east to west and north to south,
we  can  find almost all herbs. Nepalese herbs are
exported to third  countries  in large quantities.
We  can provide you  Nepalese herbs  as  per  your
requirements.

Nepali  herbs   and  herbal  products,  especially
herbal  tea, ayurvedic  medicine and aromatic oil,
are  now  exported   to  foreign  countries,  with
European  states being the major importers. Nepali
herbs  and  herbal  products are in high demand in
the  international  market. Of around  100 species
of herbs  produced in  the country,  30 are export
quality.  Nepal  is  famous  in  the world for its
aromatic oil. The Karnali region produces the most
high-value  herbs, followed  by Mid-Hill and Terai
regions. The  Terai alone  is capable of producing
20 varieties of aromatic oil."""



def database(root, input_date, input_quantity,main_passed):
   import pandas as pd
   from tkinter import messagebox
   new_data_to_save = [[input_date, input_quantity]]
   new_data_to_save = pd.DataFrame(new_data_to_save)
   def csv_writer(new_data_to_save, csv_storage_file):
      
      try:
         if(input_date[4:5]=='-' and int(input_date[5:]) <= 12 and int(input_date[5:]) > 0):
            new_data_to_save.to_csv(csv_storage_file, mode = 'a', header = False, index = False)
            root.withdraw()
            messagebox.showinfo('Sucessed',"Your data has been recorded!")
         else:
            root.withdraw()
            messagebox.showerror('Filed', 'Some Parameter went wrong!!!')
      except:
         root.withdraw()
         messagebox.showerror('Failed',"Failed to record your data!\n\nYour date must be in YYYY-MM format\n\nAnd your quantity must be in whole number")

   if (main_passed == "Rice"):
      csv_writer(new_data_to_save, 'dataset/rice.csv')
   elif (main_passed == "Potato"):
      csv_writer(new_data_to_save, 'dataset/potato.csv')
   elif (main_passed == "Apple"):
      csv_writer(new_data_to_save, 'dataset/apple.csv')
   elif (main_passed == "Tea"):
      csv_writer(new_data_to_save, 'dataset/tea.csv')
   elif (main_passed == "Alainchi"):
      csv_writer(new_data_to_save, 'dataset/alainchi.csv')
   elif (main_passed == "Herbs"):
      csv_writer(new_data_to_save, 'dataset/herbs.csv')





def model_calll(window, called_item, model_status, passed_value, graph_status):
    global read_data, process_to_do, calling_status, graph_to_print, title_print_first_word, p, d, q, graph_staus
    # db = pymysql.connect("localhost","root","","7th_project" )
    if called_item == "Rice":
        read_data = pd.read_csv("dataset/rice.csv", index_col = 'Month', parse_dates = [0])
        title_print_first_word = "Import"
        p = 21
        d = 1
        q = 5

    elif called_item == "Potato":
        read_data = pd.read_csv("dataset/potato.csv", index_col = 'Month', parse_dates = [0])
        title_print_first_word = "Import"
        p = 21
        d = 1
        q = 4

    elif called_item == "Apple":
        read_data = pd.read_csv("dataset/apple.csv", index_col = 'Month', parse_dates = [0])
        title_print_first_word = "Import"
        p = 27
        d = 1
        q = 2

    elif called_item == "Tea":
        read_data = pd.read_csv("dataset/tea.csv", index_col = 'Month', parse_dates = [0])
        title_print_first_word = "Export"
        p = 14
        d = 1
        q = 4

    elif called_item == "Alainchi":
        read_data = pd.read_csv("dataset/alainchi.csv", index_col = 'Month', parse_dates = [0])
        title_print_first_word = "Export"
        p = 13
        d = 1
        q = 4
    
    elif called_item == "Herbs":
        read_data = pd.read_csv("dataset/herbs.csv", index_col = 'Month', parse_dates = [0])
        title_print_first_word = "Export"
        p = 20
        d = 1
        q = 8


    calling_status = model_status
    graph_type = passed_value

    data= read_data.reset_index()
    data['Month'] = pd.to_datetime(data["Month"])
    data.set_index("Month", inplace = True)
    training_data = data[:round(len(data)*0.85)]
    test_data = data[round(len(data)*0.85):]
    len_training = len(training_data)
    training_data_logscale = np.log(training_data)

    # training_data_logscale = np.log(training_data)
    movingavg = training_data_logscale.rolling(window=12).mean()
    movingstd = training_data_logscale.rolling(window=12).std()
    datasetlogscalemovingavg = training_data_logscale - movingavg
    datasetlogscalemovingavg.dropna(inplace=True)
    exp_decay_wt_avg = training_data_logscale.ewm(
        halflife=12, min_periods=0, adjust=True).mean()
    data_logscale_minus_moving_exp_decay_avg = training_data_logscale - exp_decay_wt_avg
    datasetlogdiffshifting = training_data_logscale - training_data_logscale.shift()
    datasetlogdiffshifting.dropna(inplace=True)



    def graph_print(called_status, graph_to_print, training_data, test_data, len_training, datasetlogdiffshifting):
        results_ar = ARIMAResults.load("trained_model/"+called_item+".pkl")
        global original_data_plot, predicted_data

        rss = np.log(sum((results_ar.fittedvalues-datasetlogdiffshifting["Quantity"])**2))
        if called_status == 0:

            #making prediction
            pred = results_ar.forecast(steps=60)[0]
            y = pred.tolist()
            s = pd.Series(y, copy=False)
            s = np.exp(s)
            training_data = training_data.reset_index()
            for x in range(len(s)):
                if(training_data.Month[len(training_data)-1].month < 12):
                    m = training_data.Month[len(training_data)-1].month + 1
                    y = training_data.Month[len(training_data)-1].year
                else:
                    y = training_data.Month[len(training_data)-1].year + 1
                    m = 1
                d = '{}-{}'.format(y, m)
                d = datetime.strptime(d, '%Y-%m')
                training_data = training_data.append(
                    {'Month': d, 'Quantity': s[x]}, ignore_index=True)
            training_data.set_index("Month", inplace=True)
            original_data_plot = training_data[:len_training]
            predicted_data = training_data[len_training:]
        fig = plt.figure(figsize=(4.5, 4), dpi=90)
        plt.title(f'{title_print_first_word} of {called_item} with RSS Error: {rss:.4f}')
        if(graph_to_print == "Line Graph"):
            plt.plot(original_data_plot, color='black', label="Training Data")
            plt.plot(test_data, color='blue', label="Actual Data")
            plt.plot(predicted_data, color='red', label="Predicted Data")
        elif(graph_to_print == "Scatter Graph"):
            plt.scatter(original_data_plot.index.values, original_data_plot['Quantity'], s=10, color='black', label="Training Data")
            plt.scatter(test_data.index.values, test_data['Quantity'], s=10, color='blue', label="Actual Data")
            plt.scatter(predicted_data.index.values, predicted_data['Quantity'], s=10, color='red', label="Predicted Data")
            rolmean = training_data.rolling(window = 12).mean()
            plt.plot(rolmean, color = 'green', label = "mean line")            

        plt.xlabel("Date")
        plt.ylabel("Quantity in Kg")
        plt.legend(loc='best')
        # You can make your x axis labels vertical using the rotation

        # specify the window as master
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=30, column=5, columnspan=4,
                                    padx=0, pady=0, ipadx = 27, ipady = 30)
        
        called_status = 1
        return called_status, canvas

    if(passed_value == "Reload Model"):
        graph_type = "Line Graph"
        
        model = ARIMA(training_data_logscale, order=(p, d, q))
        results_ar = model.fit(disp=-1)
        results_ar.save("trained_model/"+called_item+".pkl")


        model_status, canvas= graph_print(calling_status, graph_type, training_data, test_data, len_training, datasetlogdiffshifting)
        graph_staus.append("1")
        return model_status, graph_staus
    else:
        model_status, canvas= graph_print(calling_status, graph_type,training_data, test_data, len_training, datasetlogdiffshifting)
        graph_status.append(canvas)
        return model_status, graph_status






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
  elif called_item == 'Potato':   
    screen.title("Prediction of Potato Import")
    c1 = canvas_show_information('imgs/imp_potato.jpg', potato)
  elif called_item == 'Apple':   
    screen.title("Prediction of Apple Import")
    c1 = canvas_show_information('imgs/imp_apple.jpg', apple)
  elif called_item == 'Tea':   
    screen.title("Prediction of Tea Export")
    c1 = canvas_show_information('imgs/exp_tea.jpg', tea)
  elif called_item == 'Alainchi':   
    screen.title("Prediction of Alainchi Export")
    c1 = canvas_show_information('imgs/exp_alainchi.jpg', alainchi)
  elif called_item == 'Herbs':   
    screen.title("Prediction of Herbs Export")
    c1 = canvas_show_information('imgs/exp_herbs.jpg', herbs)

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

from tkinter import * 
import tkinter.font as tkFont
import sys
import numpy as np
import pandas as pd
from pandas import datetime
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA, ARIMAResults
from PIL import Image, ImageDraw, ImageFilter, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from functools import partial
from tkinter import messagebox
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
submenu_exp.add_command(label="Tea", command = partial(design_menu, canvas, graph_status, 0,"Tea"))
submenu_exp.add_command(label="Herbs", command = partial(design_menu, canvas, graph_status, 0,"Herbs"))
submenu_exp.add_command(label="Alainchi", command = partial(design_menu, canvas, graph_status, 0,"Alainchi"))
submenu_exp.add_separator()
filemenu.add_cascade(label='Export', menu=submenu_exp, underline=0) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=screen.destroy) 
helpmenu = Menu(menu) 
menu.add_command(label='About', command = partial(about_us, canvas, graph_status))
screen.resizable(0, 0) 
screen.mainloop()