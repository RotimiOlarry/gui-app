import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS olarry (id INTEGER PRIMARY KEY, item text, date integer , buying_price text, selling_price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM olarry")
        rows = self.cur.fetchall()
        return rows

    def insert(self, item,date,buying_price,selling_price):
        self.cur.execute("INSERT INTO olarry VALUES (NULL, ?,?,?,?)",(item,date,buying_price,selling_price))
        self.conn.commit()

    def remove (self,id):
        self.cur.execute(" DELETE FROM olarry WHERE id =?",(id,))
        self.conn.commit()

    def update(self,id,item,date,buying_price,selling_price):
        self.cur.execute("UPDATE olarry SET item = ? , date = ?, buying_price = ? , selling_price = ? WHERE id = ?",(item,date,buying_price,selling_price,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


