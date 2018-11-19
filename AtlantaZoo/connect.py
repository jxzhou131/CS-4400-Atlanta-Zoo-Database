# import mysql.connector
# from mysql.connector import errorcode
import sshtunnel
import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling
import importlib

"""  
    Parameters to connect to the database in the remote server.
    ----------
    username : gatech username
    password : gatech password
"""
ssh_username = 'ttan41'
ssh_password = 'Inova6626***'


"""
    Define the configuration of the Window Pages (UIs)
"""
initialUIs ={
  0: "loginPage",
  1: "registration"
  # 2: "visitorFunctionality"
  # 3: "staffFunctionality"
  # 4: "administratorFunctionality"
}

visitorUIs = {
  0: 'visitorFunctionality',
  1: 'visitorExhibitHistory',
  2: 'visitorSearchAnimals',
  3: 'visitorSearchExhibit',
  4: 'visitorSearchShow',
  5: 'visitorShowHistory'
}

staffUIs = {
  
}

adminUIs = {
  0: 'administratorFunctionality',
  1: 'adminAddAnimals',
  2: 'adminAddShows',
  3: 'adminViewAnimals',
  4: 'adminViewShows',
  5: 'adminViewStaff',
  6: 'adminViewVisitors'
}

"""
  Definition of status
"""
statusDef = {
  'Error': -1,
  'Normal': 1
}

if __name__ == "__main__":
  # with sshtunnel.SSHTunnelForwarder(
  #         ('academic-mysql.cc.gatech.edu', 22),
  #         ssh_username=ssh_username,
  #         ssh_password=ssh_password,
  #         remote_bind_address=('essay', 3306)
  # ) as tunnel:
    # connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="altantaZooPool",
    #                                                               pool_size=5,
    #                                                               pool_reset_session=True,
    #                                                               host='127.0.0.1',
    #                                                               database='cs4400_group15',
    #                                                               user='cs4400_group15',
    #                                                               password='IlEboaZW',
    #                                                               use_pure=True,
    #                                                               port = tunnel.local_bind_port)
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="altantaZooPool",
                                                                  pool_size=5,
                                                                  pool_reset_session=True,
                                                                  host='academic-mysql.cc.gatech.edu',
                                                                  database='cs4400_group15',
                                                                  user='cs4400_group15',
                                                                  password='IlEboaZW',
                                                                  use_pure=True)
               
    # print("before loginPage")
    state = 0
    status = 0
    arg = []
    loginIdentity = []
    module = None
    # obtain the connection_object
    connection_object = connection_pool.get_connection()
    # these three lines of code is used for debugging: CHECK FOR CONNECTIONS
    if connection_object.is_connected():
        db_Info = connection_object.get_server_info()
    print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)

    # import all the intial UIs modules available here

    import loginPage, registration
    while(state == 0 or state == 1):
      if(state == 0):
        loginPage.render()
      elif(state == 1):
        registration.render()

    # DEBUGGING USE
    # display current user data
    print("loginIdentity")
    print(loginIdentity)

    # close the cursor and connection
    if(connection_object.is_connected()):
        # cursor.close()
        connection_object.close()
        print("MySQL connection is closed")



    # if(status == -1):
    # # there is an error
    #   print("Error")
    # else:
    # # no error, proceed
    #   module = None
    #   if(loginIdentity[3] == "visitor"):
    #     while True:
    #       if(importlib.util.find_spec(visitorUIs[state])):
    #         module = importlib.reload(visitorUIs[state])
    #       else:
    #         module = importlib.import_module(visitorUIs[state])
    #       # uncommented in DEBUGGING MODE
    #       print("state")
    #       print(state)
    #       print("status")
    #       print(status)
    #       print("arg")
    #       print(arg)

    #   elif (loginIdentity[3] == "staff"):
    #     while True:
    #       if(importlib.util.find_spec(staffUIs[state])):
    #         module = importlib.reload(staffUIs[state])
    #       else:
    #         module = importlib.import_module(staffUIs[state])
    #       # uncommented in DEBUGGING MODE
    #       print("state")
    #       print(state)
    #       print("status")
    #       print(status)
    #       print("arg")
    #       print(arg)
    #   elif( loginIdentity[3] == "admin"):
    #     while True:
    #       if(importlib.util.find_spec(adminUIs[state])):
    #         module = importlib.reload(adminUIs[state])
    #       else:
    #         module = importlib.import_module(adminUIs[state])
    #       # uncommented in DEBUGGING MODE
    #       print("state")
    #       print(state)
    #       print("status")
    #       print(status)
    #       print("arg")
    #       print(arg)

    # print("state")
    # print(state)
    # print("status")
    # print(status)
    # print("arg")
    # print(arg)

