# CS-4400-Atlanta-Zoo-Database
In this project, we constructed a relational database using python 3.5, qt designer and mysql. The mysql servers is a remote server setup by the Georgia Institute of Technology. Thus, after this Fall 2018 semester the database might not be able to be accessed anymore.

## Project Purpose  
Analyze, specify, design, implement, document and demonstrate an online system. You are required to use the classical methodology for database development. The system will be implemented using a relational DBMS that supports standard SQL queries. The TAs will provide you with information about how to access a college-managed MySQL server in order to implement your database and the application. We will also provide you with a list of approved technologies for your implementation, and the professor must approve the use of any other alternative technologies. Under no circumstances can you use a tool that automatically generates SQL or automatically maps programming objects into the database. You also cannot use any other software like Access or SQLite. Ask the professors or TAs if you have questions about which tools/languages/software are allowed. 

## EER Diagram
![alt text](/images/EER_Diagram.png?raw=true "EER Diagram")

## IFD Diagram
![alt text](/images/IFD_Diagram.png?raw=true "IFD Diagram")

## Setting up the enviroment for QTDesigner
1. [Download QT Designer](https://build-system.fman.io/qt-designer-download)

## Setting up the environment for Anaconda
1. [Download Anaconda](https://www.anaconda.com/download/)
2. [Create Virtual Environment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)

- For Mac, Go to Anaconda Navigator and create a python 3.5 virtual environment. Open the py35 virtual environment from Anaconda Navigator.

- For Windows, open anaconda prompt. 

  - i. Type `conda create -n py35 python=3.5 anaconda`

  - ii. To activate the environment, type `activate py35`

## Installing pyqt to the environment
1. Open your python 3.5 virtual environment.
2. Type `conda install -c anaconda pyqt`

## Installing packages for accessing remote MySQL server using python
1. Open your python 3.5 virtual environment.
2. Install mysql-connector-python. Type `pip install mysql-connector-python==8.0.11`.

References: 
+ [GeekforGeek](https://www.geeksforgeeks.org/mysqldb-connection-python/)
+ [MySQL Connector/Python Developer Guide](https://downloads.mysql.com/docs/connector-python-en.a4.pdf)
+ [TutorialPoints](https://www.tutorialspoint.com/python/python_database_access.htm)
+ [Installation](https://pynative.com/install-mysql-connector-python/)

## How to use the tools?
1. Open the QTDesigner. Complete your design. There are some [tutorials](https://www.youtube.com/watch?v=EkjaiDsiM-Q&list=PLS1QulWo1RIZiBcTr5urECberTITj7gjA) available in the youtube. This is one of the video that I found it very resourceful. After completing your design you can __Preview__ your ui through *From -> Preview* or *Ctrl + R*. Next, save your .ui file in the folder that you stores your github code.

2. Open your python 3.5 environment. Go to the directory that you have saved your .ui file. Then type `pyuic5 -x <nameOfTheUIFile> -o <nameOfTheUIFile>`. For example. `pyuic5 -x loginPage.ui -o loginPage.py`. The python file will be generated in the same folder as your .ui file.


