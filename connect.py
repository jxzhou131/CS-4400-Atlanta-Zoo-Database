import mysql.connector
from mysql.connector import errorcode

"""
  Currently the Database atlanta_zoo is empty
  The existing tables are:
  admins
  animal
  exhibit
  note
  shows
  staff
  user
  visitexhibit
  visitshows
  visitor
"""

"""
    It connects to the database in the remote server.
    Parameters
    ----------
    username : gatech username
    password : gatech password
"""

def MySQLConnect(username, password):
  try:
  	cnx = mysql.connector.connect(user=username, password=password,host='127.0.0.1',database='atlanta_zoo')
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)

  return cnx
  

if __name__ == "__main__":

  cnx = MySQLConnect('ttan41', '')
  mycursor = cnx.cursor()

  #mycursor.execute("USE atlanta_zoo")

  #mycursor.execute("SELECT * from animal")

  #mycursor.execute("select * from employee")

  mycursor.execute("SELECT * FROM information_schema.tables")

  myresult = mycursor.fetchall()

  for x in myresult:
  	print(x)


