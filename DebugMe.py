import MySQLdb
import datetime

def synchro(userID):
    dbDebian = MySQLdb.connect("localhost", "usrRemMeds", "azerty", "remmedsTest")
    cursorDebian = dbDebian.cursor()
    dbLocal = MySQLdb.connect("localhost", "usrRemMeds", "azerty", "remmeds")
    cursorLocal = dbLocal.cursor()




    cursorDebian.execute("select * from rm_user where us_id = %s ;", userID)
    # Fetch all row.
    data = cursorDebian.fetchall()
    #Add to local bdd
    cursorLocal.execute("""insert into rm_user  values %s;""", data)
    dbLocal.commit()

    dbLocal.close()

synchro(1)