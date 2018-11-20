# import mysql.connector
# from mysql.connector import errorcode

import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling


"""
    Define the configuration of the Window Pages (UIs)
"""
initialUIs ={
  "exitInitialUIs" : 0,
  "loginPage" : 1,
  "registration" : 2
  # 2: "visitorFunctionality"
  # 3: "staffFunctionality"
  # 4: "administratorFunctionality"
}

visitorUIs = {
  'visitorFunctionality' : 0,
  'visitorExhibitHistory' : 1,
  'visitorSearchAnimals' : 2,
  'visitorSearchExhibit': 3,
  'visitorSearchShow': 4,
  'visitorShowHistory': 5
}

staffUIs = {
  
}

adminUIs = {
  'administratorFunctionality' : 0,
  'adminAddAnimals' : 1,
  'adminAddShows' : 2,
  'adminViewAnimals' :3,
  'adminViewShows' : 4,
  'adminViewStaff' : 5,
  'adminViewVisitors' : 6
}

"""
  Definition of status
"""
statusDef = {
  'Error': -1,
  'Main' : 0,
  'Normal': 1
}

if __name__ == "__main__":
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="altantaZooPool",
                                                                  pool_size=5,
                                                                  pool_reset_session=True,
                                                                  host='academic-mysql.cc.gatech.edu',
                                                                  database='cs4400_group15',
                                                                  user='cs4400_group15',
                                                                  password='IlEboaZW',
                                                                  use_pure=True)
               
    state = 1
    status = 0
    arg = []
    loginIdentity = []
    # obtain the connection_object
    connection_object = connection_pool.get_connection()
    # these three lines of code is used for debugging: CHECK FOR CONNECTIONS
    if connection_object.is_connected():
        db_Info = connection_object.get_server_info()
    print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)

    # import all the intial UIs modules available here

    import loginPage, registration
    while(state == 1 or state == 2):
      if(state == 1):
        loginPage.render()
      elif(state == 2):
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

