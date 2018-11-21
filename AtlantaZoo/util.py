def addWHERE(cmd, listTuple):
    """ 
        How to create dictVar outside of this function?
        -----------------------------------------------
        Email = self.emailLineEdit.text()
        Username = self.usernameLineEdit.text()

        listTuple = [("Email", Email), ("Username": Username)]

        IMPORTANT:
        the name of the variable must be the same as the attributes in the relational schema
        USER(Username, Password, Email, UserType)

        INPUTS
        =======
        cmd: command to be concatenated with WHERE conditions
        listTuple: contains {'name of variable': "value of variable"}

    """
    numWhereClausesAdded = 0
    for name, value in listTuple:
        if((type(value) is str) and value.lstrip().rstrip() == ""):
            pass
        else:
            if(numWhereClausesAdded == 0):
                cmd += " WHERE "
            else:
                cmd += " AND "
            if(name == "DateTime"):
                cmd += ("STR_TO_DATE(\'" + value + "\', \'%m/%d/%Y %r\')")
            elif("Min" in name):
                modifiedName = name.replace("Min",'')
                cmd += ( modifiedName + " BETWEEN " + str(value) )
            elif("Max" in name):
                cmd += ( str(value) )
            elif(name == "WaterFeature"):
                cmd += ( name + " = " + str(value) + " ")
            else:
                cmd += ( name + " = \'" + value + "\'")
            numWhereClausesAdded += 1
    cmd += " ;"
    return cmd
