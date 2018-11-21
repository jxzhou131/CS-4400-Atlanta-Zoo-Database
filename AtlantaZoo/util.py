def addWHERE(cmd, dictVar):
    """ 
        How to create dictVar outside of this function?
        -----------------------------------------------
        Email = self.emailLineEdit.text()
        Username = self.usernameLineEdit.text()

        dictVar = {"Email": Email, "Username": Username}

        IMPORTANT:
        the name of the variable must be the same as the attributes in the relational schema
        USER(Username, Password, Email, UserType)

        INPUTS
        =======
        cmd: command to be concatenated with WHERE conditions
        dictVar: contains {'name of attribute': "value of variable"}
    """
    numWhereClausesAdded = 0
    for name, value in dictVar.items():
        if(value.lstrip().rstrip() == ""):
            pass
        else:
            if(numWhereClausesAdded == 0):
                cmd += " WHERE "
            else:
                cmd += " AND "
            if(name == "DateTime"):
                cmd += ("STR_TO_DATE(\'" + value + "\', \'%m/%d/%Y %r\')")
            else:
                cmd += ( name + " = \'" + value + "\'")
            numWhereClausesAdded += 1
    cmd += " ;"
    return cmd