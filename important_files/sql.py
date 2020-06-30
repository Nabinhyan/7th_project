def database(root, d,q,main_passed):
   global db_table
   import pymysql
   from tkinter import messagebox
   global database_status 
   print(d[4:5])
   db = pymysql.connect("localhost","root","","test" )
   cursor = db.cursor()
   cursor.execute("SELECT VERSION()")
   data = cursor.fetchone()
   def sql_commit(sql):
      
      try:
         
         if (d[4:5]!='-'):
            root.withdraw()
            messagebox.showerror('Failed', 'You must add - after year')
         elif(int(d[5:])>12):
            root.withdraw()   
            messagebox.showerror('Failed','You have entered month > 12')
         else:
            cursor.execute(sql)
            db.commit()
            database_status = 1   
            return database_status
      except:
         db.rollback()
         database_status = 0
         return database_status
      db.close()

   if (main_passed == "Rice"):
      database_status = sql_commit("INSERT INTO rice VALUES( '%s', '%s')" %(d, q))



   if (main_passed == "Potato"):
      database_status = sql_commit("INSERT INTO rice VALUES( '%s', '%s')" %(d, q))


   if (main_passed == "Apple"):
      database_status = sql_commit("INSERT INTO rice VALUES( '%s', '%s')" %(d, q))


   root.withdraw()
   if (database_status == 1):
      messagebox.showinfo('Sucessed',"Your data has been recorded!")
   elif (database_status == 0):
      messagebox.showerror('Failed',"Failed to record your data!\n\nYour date must be in YYYY-MM format\n\nAnd your quantity must be in whole number")

   
   # db.close()
   