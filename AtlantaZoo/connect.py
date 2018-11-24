# import mysql.connector
# from mysql.connector import errorcode

import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling
import importlib

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
  'visitorShowHistory': 5,
  'animalDetails': 6,
  'exhibitDetails': 7,
  'logout': -5
}

staffUIs = {
  'staffFunctionality': 0,
  'staffSearchAnimals': 1,
  'staffAnimalCare' : 2,
  'staffViewShows' : 3,
  'logout': -5
}

adminUIs = {
  'administratorFunctionality' : 0,
  'adminAddAnimals' : 1,
  'adminAddShows' : 2,
  'adminViewAnimals' :3,
  'adminViewShows' : 4,
  'adminViewStaff' : 5,
  'adminViewVisitors' : 6,
  'logout': -5
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
    import visitorFunctionality, visitorSearchShow, visitorSearchAnimals, visitorSearchExhibit
    import visitorFunctionality, visitorSearchShow, visitorSearchAnimals, exhibitDetails, visitorExhibitHistory, visitorShowHistory
    import staffFunctionality, staffViewShows, staffSearchAnimals, staffAnimalCare
    import visitorFunctionality, visitorSearchShow, visitorSearchAnimals, exhibitDetails
    import administratorFunctionality, adminViewShows, adminAddAnimals, adminViewVisitors, adminViewStaff, adminAddShows, adminViewAnimals
    import exhibitDetails

    # comment this if you use want a fast login
    # then uncomment the statement below it
    # while(state == 1 or state == 2):
    #   if(state == 1):
    #     loginPage.render()
    #   elif(state == 2):
    #     registration.render()

    # uncomment this too to skip login page
    # state = 0

    # #================ Parameters to run test case on AnimalCarePage =============
    # # state of animalcare page
    # state = 2
    # arg = [('Goldy', 'Goldfish', 'Fish',12,'Pacific')]

    # uncomment this if you need a visitor ID
    # loginIdentity = [('xavier_swenson', '34cc93ece0ba9e3f6f235d4af979b16c', 'xavierswenson@outlook.com', 'visitor')]


    # uncomment this if you need a staff ID

    # loginIdentity = [('martha_johnson', '7c6a180b36896a0a8c02787eeafb0e4c', 'marthajohnson@hotmail.com', 'staff')]


    # uncomment this if you need an admin ID
    # loginIdentity = [('admin1','e3274be5c857fb42ab72d786e281b4b8','adminemail@mail.com','admin')]

    # DEBUGGING USE
    # display current user data
    print("loginIdentity")
    print(loginIdentity)

    # close the cursor and connection
    if(connection_object.is_connected()):
        # cursor.close()
        connection_object.close()
        print("MySQL connection is closed")

    if(status == -1):
    # there is an error
      print("Error")
    else:
      while(state > -10 and state < 10 and status != -1):
        # comment this if you use want a fast login
        # then uncomment the statement below it
        while(state == 1 or state == 2):
          if(state == 1):
            loginPage.render()
          elif(state == 2):
            registration.render()

      # no error, proceed
        module = None
        if(loginIdentity[0][3] == "visitor"):
          while(state > -1 and state < 10 and status != -1):
            if(state == visitorUIs["visitorFunctionality"]):
              visitorFunctionality.render()
              pass
            elif(state == visitorUIs["visitorShowHistory"]):
              visitorShowHistory.render()
              pass
            elif(state == visitorUIs["visitorSearchShow"]):
              visitorSearchShow.render()
              pass
            elif(state == visitorUIs["visitorSearchExhibit"]):
              visitorSearchExhibit.render()
              pass
            elif(state == visitorUIs["visitorSearchAnimals"]):
              visitorSearchAnimals.render()
              pass
            elif(state == visitorUIs["visitorExhibitHistory"]):
              visitorExhibitHistory.render()
              pass
            elif(state == visitorUIs["animalDetails"]):
              animalDetails.render()
              pass
            elif(state == visitorUIs["exhibitDetails"]):
              exhibitDetails.render()
              pass
            # uncommented in DEBUGGING MODE
            print("state")
            print(state)
            print("status")
            print(status)
            print("arg")
            print(arg)

        elif (loginIdentity[0][3] == "staff"):
          while(state > -1 and state < 10 and status != -1):
            if(state == staffUIs["staffFunctionality"]):
              staffFunctionality.render()
              pass
            elif (state == staffUIs["staffViewShows"]):
              staffViewShows.render()
              pass
            elif(state == staffUIs["staffAnimalCare"]):
              staffAnimalCare.render()
              pass
            elif(state == staffUIs["staffSearchAnimals"]):
              staffSearchAnimals.render()
              pass
            # uncommented in DEBUGGING MODE
            print("state")
            print(state)
            print("status")
            print(status)
            print("arg")
            print(arg)

        elif( loginIdentity[0][3] == "admin"):
          while(state > -1 and state < 10 and status != -1):
            if(state == adminUIs["administratorFunctionality"]):
              administratorFunctionality.render()
              pass
            elif(state == adminUIs["adminViewVisitors"]):
              adminViewVisitors.render()
              pass
            elif(state == adminUIs["adminViewStaff"]):
              adminViewStaff.render()
              pass
            elif(state == adminUIs["adminViewShows"]):
              adminViewShows.render()
              pass
            elif(state == adminUIs["adminAddShows"]):
              adminAddShows.render()
              pass
            elif(state == adminUIs["adminAddAnimals"]):
              adminAddAnimals.render()
              pass
            elif(state == adminUIs["adminViewAnimals"]):
              adminViewAnimals.render()

            # uncommented in DEBUGGING MODE
            print("state")
            print(state)
            print("status")
            print(status)
            print("arg")
            print(arg)
        # if the state == -5, it means go back to login page
        # else state == -10, it means exit windows
        if(state == -5):
          state = 1

    # print("state")
    # print(state)
    # print("status")
    # print(status)
    # print("arg")
    # print(arg)
