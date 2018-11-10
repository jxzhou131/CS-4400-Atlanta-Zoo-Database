# import mysql.connector
# from mysql.connector import errorcode
import sshtunnel
import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling

"""
    
    Parameters to connect to the database in the remote server.
    ----------
    username : gatech username
    password : gatech password
"""
ssh_username = 'ttan41'
ssh_password = 'Inova6626***'


def displayLoginPage2():
  import sys
  import src.loginPage2 # run the file is called file
  from src.loginPage2 import status # getting any variables or objects from the loginPage2Module
  x = status
  del sys.modules["src.loginPage2"] # delete a module
  del src.loginPage2 # delete a module
  return x

def printOutput():
    print('10')

if __name__ == "__main__":
  with sshtunnel.SSHTunnelForwarder(
          ('academic-mysql.cc.gatech.edu', 22),
          ssh_username=ssh_username,
          ssh_password=ssh_password,
          remote_bind_address=('essay', 3306)
  ) as tunnel:
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="altantaZooPool",
                                                                  pool_size=5,
                                                                  pool_reset_session=True,
                                                                  host='127.0.0.1',
                                                                  database='cs4400_group15',
                                                                  user='cs4400_group15',
                                                                  password='IlEboaZW',
                                                                  use_pure=True,
                                                                  port = tunnel.local_bind_port)
    x = 0
    print("before loginPage")
    print(x)
    status = displayLoginPage2()
    status = displayLoginPage2()
    print(status)
    # import src.loginPage2 # run the file is called file
    # from src.loginPage2 import status
    # print(status)
    # import src.loginPage2 # run the file is called file
    # from src.loginPage2 import status
    # print(status)
    # exec(open('src/loginPage2.py').read()) # run the file as main
    print("after loginPage")
    print(x)
