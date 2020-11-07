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
            messagebox.showerror('Failed', 'Some Parameter went wrong!!!')
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

   