def database(root, d,q,main_passed):
   import pymysql
   from tkinter import messagebox
   global database_status 
   db = pymysql.connect("localhost","root","","test" )
   cursor = db.cursor()
   cursor.execute("SELECT VERSION()")
   data = cursor.fetchone()
   def sql_commit(sql):
      
      try:
         if(d[4:5]=='-' and int(d[5:]) <= 12 and int(d[5:]) > 0):
            cursor.execute(sql)
            db.commit()
            database_status = 1
            return database_status
         else:
            root.withdraw()
            messagebox.showerror('Filed', 'Some Parameter went wrong!!!')
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
