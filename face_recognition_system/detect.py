import sqlite3

def getprofile(id):
    
    conn=sqlite3.connect(database="srms.db")
    cursor=conn.execute("select * from result where roll=?",(id,))
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile



