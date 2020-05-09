import sqlite3

def CurrentCurrr():
    db = sqlite3.connect('myspendmate.db')
    cursor = db.cursor()
    cursor.execute("select * from Currency")
    Curr = cursor.fetchone()[0]
    cursor.close()
    db.commit()
    db.close()
    return Curr