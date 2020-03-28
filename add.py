def add_one():
  import tkinter as tk
  master = tk.Tk()
  tk.Label(master, text="First Name").grid(row=0)
  tk.Label(master, text="Last Name").grid(row=1)
  e1 = tk.Entry(master)
  e2 = tk.Entry(master)
  e1.grid(row=0, column=1)
  e2.grid(row=1, column=1)
  tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
  tk.Button(master, text='Show', command=show_entry_fields(e1,e2)).grid(row=3, column=1, sticky=tk.W, pady=4)
  
  def show_entry_fields(e1,e2):
    # global e1
    # global e2
    import mysql.connector
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="test"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO testt VALUES (%s, %s)"
    val = (e1.get(), e2.get())
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    tk.mainloop() 
# print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
