import sqlite3

def makedatabase():
    print('Making DataBase!!')
    db = sqlite3.connect('myspendmate.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS income (amount INT NOT NULL, date TEXT NOT NULL, description TEXT, category TEXT NOT NULL ,account_type TEXT NOT NULL,day INT NOT NULL,month INT NOT NULL,year INT NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS expense (amount INT NOT NULL, date TEXT NOT NULL, description TEXT, category TEXT NOT NULL ,account_type TEXT NOT NULL,day INT NOT NULL,month INT NOT NULL,year INT NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS goals (name TEXT NOT NULL , enddate TEXT NOT NULL, target_value INT NOT NULL, current_value INT NOT NULL, description TEXT,day INT NOT NULL,month INT NOT NULL,year INT NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS budget (amount INT NOT NULL, percentage INT NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS incomeCat (category TEXT NOT NULL UNIQUE)")
    cursor.execute("SELECT * FROM incomeCat")
    status1 = cursor.fetchone()[0]
    if(status1=='None'):
        cursor.execute("insert into incomeCat values('%s')"%('Salary'))
    cursor.execute("CREATE TABLE IF NOT EXISTS expenseCat (category TEXT NOT NULL UNIQUE)")
    cursor.execute("SELECT * FROM incomeCat")
    status2 = cursor.fetchone()[0]
    if(status2=='None'):
        cursor.execute("insert into expenseCat values('%s')"%('HealthCare'))
    cursor.execute("CREATE TABLE IF NOT EXISTS Account (category TEXT NOT NULL UNIQUE)")
    cursor.execute("SELECT * FROM incomeCat")
    status3 = cursor.fetchone()[0]
    if(status3=='None'):
        cursor.execute("insert into Account values('%s')"%('Cash'))
    cursor.close()
    db.commit()
    db.close()
