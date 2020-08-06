def database(root, input_date, input_quantity,main_passed):
   import pymysql
   from tkinter import messagebox
   db = pymysql.connect("localhost","root","","test" )
   cursor = db.cursor()
   cursor.execute("SELECT VERSION()")
   data = cursor.fetchone()
   def sql_commit(sql):
      
      try:
         if(d[4:5]=='-' and int(d[5:]) <= 12 and int(d[5:]) > 0):
            cursor.execute(sql)
            db.commit()
            root.withdraw()
            messagebox.showinfo('Sucessed',"Your data has been recorded!")


         else:
            root.withdraw()
            messagebox.showerror('Filed', 'Some Parameter went wrong!!!')
      except:
         db.rollback()
         root.withdraw()
         messagebox.showerror('Failed',"Failed to record your data!\n\nYour date must be in YYYY-MM format\n\nAnd your quantity must be in whole number")

      db.close()

   if (main_passed == "Rice"):
      sql_commit("INSERT INTO rice VALUES( '%s', '%s')" %(input_date, input_quantity))

   if (main_passed == "Potato"):
      sql_commit("INSERT INTO rice VALUES( '%s', '%s')" %(input_date, input_quantity))

   if (main_passed == "Apple"):
      sql_commit("INSERT INTO rice VALUES( '%s', '%s')" %(input_date, input_quantity))

