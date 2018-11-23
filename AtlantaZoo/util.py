# CONVERT DATETIME TO STRING
# Example
# print(record[0][1].strftime("%m/%d/%Y %I:%M:%S %p"))

# Try datetime
# print(time.strftime("%m/%d/%Y %I:%M:%S %p"))

def addWHERE(cmd, listTuple):
    """ 
        How to create dictVar outside of this function?
        -----------------------------------------------
        Email = self.emailLineEdit.text()
        Username = self.usernameLineEdit.text()

        listTuple = [("Email", Email, "DataType"), ("Username", Username, "DataType")]

        IMPORTANT:
        the name of the variable must be the same as the attributes in the relational schema
        USER(Username, Password, Email, UserType)

        INPUTS
        =======
        cmd: command to be concatenated with WHERE conditions

        listTuple: contains [("Name of attribute", attribute value, "DataType")]
                            [(<string>, <string var>, <string>)]

        List of DataType Handled
        ------------------------
        1) datatime
        2) str
        3) bool
        4) int
        5) NULL

    """
    numWhereClausesAdded = 0
    for name, value, dataType in listTuple:
        if(value.lstrip().rstrip() == ""):
            pass
        else:
            if(numWhereClausesAdded == 0):
                cmd += " WHERE "
            else:
                cmd += " AND "
            if(name == "DateTime"):
                cmd += (name + " = STR_TO_DATE(\'" + value + "\', \'%m/%d/%Y %r\')")
            elif("Min" in name):
                # MIN INTEGER
                modifiedName = name.replace("Min",'')
                cmd += ( modifiedName + " BETWEEN " + str(value) )
            elif("Max" in name):
                # MAX INTEGER
                cmd += ( str(value) )
            elif(dataType == "str"):
                # STRING
                cmd += ( name + " = \'" + value + "\'")
            else:
                # NON-STRING
                cmd += ( name + " = " + str(value) + " ")
            numWhereClausesAdded += 1
    return cmd
