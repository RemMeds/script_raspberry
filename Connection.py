import MySQLdb
import datetime


# Connexion locale
def conLocal():
    dbLocal = MySQLdb.connect("localhost", "usrRemMeds", "azerty", "remmeds")
    cursor = dbLocal.cursor()

    return "testLocal"


def conDebian():
    dbDebian = MySQLdb.connect("http://212.73.217.202:10080/", "root", "azerty", "remmeds_users")
    cursor = dbDebian.cursor()

    return "testDebian";


def addToBDD(cursorDebian, userID, cursorLocal, dbLocal, table):
    cursorDebian.execute("select * from "+table+" where us_id = "+userID+" ;")
    # Fetch all row.
    data = cursorDebian.fetchall()
    #Add to local bdd
    print(data)
    for row in data:
        cursorLocal.execute("insert into "+table+"  values "+row+";")
        dbLocal.commit()

def synchroBDD(userID):
    dbDebian = MySQLdb.connect("localhost", "usrRemMeds", "azerty", "remmedsTest")
    cursorDebian = dbDebian.cursor()
    dbLocal = MySQLdb.connect("localhost", "usrRemMeds", "azerty", "remmeds")
    cursorLocal = dbLocal.cursor()

    userID = str(userID)


    #For User
    cursorDebian.execute("select * from rm_user where us_id = %s ;", userID)
    # Fetch all row.
    data = cursorDebian.fetchall()
    #Add to local bdd
    print(data[0])
    cursorLocal.execute("insert into rm_user  values " + data[0])
    dbLocal.commit()


    """
    #For Compartment
    cursorDebian.execute("select * from rm_compartment where us_id = %s ;", userID )
    # Fetch all row.
    data = cursorDebian.fetchall()
    # Add all compartment to local bdd
    for row in data:
        for i in row:
            print(i)
        print("\n\n\n\n")
    """

        #cursorLocal.execute("""insert into rm_compartment  values %s;""", row)
        #dbLocal.commit()


    return "Synchro";

def resetBDD():
    dbLocal = MySQLdb.connect("localhost", "usrRemMeds", "azerty", "remmedsTest")
    cursor = dbLocal.cursor()
    cursor.execute("DELETE FROM rm_comp_preset;")
    cursor.execute("DELETE FROM rm_compartment;")
    cursor.execute("DELETE FROM rm_connect;")
    cursor.execute("DELETE FROM rm_historic;")
    cursor.execute("DELETE FROM rm_repertory;")
    cursor.execute("DELETE FROM rm_user;")
    dbLocal.commit()
    dbLocal.close()
    return "RESET";

def checkHour(numComp):
    date = datetime.datetime.now()
    hour = str(date.hour) # + ":" + str(date.minute)
    dbLocal = MySQLdb.connect("localhost", "usrRemMeds", "azerty", "remmeds")
    cursor = dbLocal.cursor()

    numComp = str(numComp)
    cursor.execute("select com_id from rm_compartment where com_num = " + numComp)

    idComp = cursor.fetchone()

    idComp = str(idComp[0])

    cursor.execute("select cpe_hour from rm_comp_preset where com_id = " + idComp)


    result = cursor.fetchall()
    bool = False

    for row in result:
        row = row[0]
        print(row)
        if(row == hour):
            bool = True
            break

    if(bool):
        return True
    else:
        return False


#print(resetBDD())

print(synchroBDD(2))


