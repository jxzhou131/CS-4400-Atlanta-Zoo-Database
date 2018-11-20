def addWHERE(cmd, dictVar):
    """ 
        How to create dictVar outside of this function?
        -----------------------------------------------
        Email = self.emailLineEdit.text()
        Username = self.usernameLineEdit.text()

        dictVar = {"Email": Email, "Username": Username}

        INPUTS
        =======
        cmd: command to be concatenated with WHERE conditions
        dictVar: contains {'name of variable': "value of variable"}
    """
    numWhereClausesAdded = 0
    for name, value in dictVar.item():
        if(value.lstrip().rstrip() == ""):
            if(numWhereClausesAdded == 0):
                cmd += " WHERE "
            else:
                cmd += " AND "
            cmd += (name + " = " + value)
    cmd += " ;"