def database(d,q,main_passed):
   global db_table
   import pymysql
   db = pymysql.connect("localhost","root","","test" )
   cursor = db.cursor()
   cursor.execute("SELECT VERSION()")
   data = cursor.fetchone()
   if (main_passed == "rice.csv"):
      sql = "INSERT INTO testt VALUES( '%s', '%s')" %(d, q)
      try:
         cursor.execute(sql)
         db.commit()
      except:
         db.rollback()


   if (main_passed == "potato.csv"):
      sql = "INSERT INTO testt1 VALUES( '%s', '%s')" %(d, q)
      try:
         cursor.execute(sql)
         db.commit()
      except:
         db.rollback()


   if (main_passed == "apple.csv"):
      sql = "INSERT INTO testt2 VALUES( '%s', '%s')" %(d, q)
      try:
         cursor.execute(sql)
         db.commit()
      except:
         db.rollback()
   db.close()
   