import pymysql

class Database(object):
    def __init__(self, host, user, passwd, db):
        self.conn = pymysql.connect(host=host, user=user, passwd=passwd, database=db)
        self.cursor = self.conn.cursor()

    def create_table(self, insert_query):
        self.cursor.execute(insert_query)

    def finish_transactions(self):
        self.conn.close()
