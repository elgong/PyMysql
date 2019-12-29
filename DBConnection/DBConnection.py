import MySQLdb

from .Config import USER_NAME, PASSWORD, HOST, PORT, DATABASES_NAME
from .Format import format


class DBConnection(object):

    connection = None

    def __init__(self):
        try:
            self.connection = MySQLdb.connect(HOST, USER_NAME, PASSWORD, DATABASES_NAME)
        except MySQLdb.Error:
            print("Can not connect the database !")

    def query_data_by_sql(self, sql=None):
        """ function : 查询函数
        :param sql:  SQL语句
        :return:  查询结果
        """

        # 打开游标
        cur = self.connection.cursor()

        # 执行SQL语句
        cur.execute(sql)

        # 查询所有数据
        raw_data = cur.fetchall()

        # 关闭游标
        self.connection.cursor().close()

        # 格式化
        data = format(raw_data)

        return data

    def insert_data_by_sql(self, sql=None):
        """ function: 插入数据
        :param sql:  SQL语句
        :return:
        """
        # 打开游标
        cur = self.connection.cursor()

        # 执行SQL语句
        cur.execute(sql)

        # 提交
        self.connection.commit()

        # 关闭游标
        self.connection.cursor().close()

    def close(self):

        print("DB close")

        self.connection.close()



