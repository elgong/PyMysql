import MySQLdb

from .Config import USER_NAME, PASSWORD, HOST, PORT
from .Format import format


class DBConnection(object):

    connection = None

    def __init__(self):
        try:
            self.connection = MySQLdb.connect(HOST, USER_NAME, PASSWORD, "cmc")
        except MySQLdb.Error:
            print("Can not connect the database !")

    def query_data_by_sql(self, sql=None):

        cur = self.connection.cursor()

        cur.execute(sql)

        raw_data = cur.fetchall()

        data = format(raw_data)

        return data

    def insert_data_by_sql(self, sql=None):

        pass



