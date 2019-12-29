
from .Config import DATABASE_Fields

"""
    get sql
"""



def get_sql_query_all_data(table_name):

    """
    :param table_name:  表名
    :return:
    """

    QUERY_ALL_DATA = "select * from {table_name}".format(table_name=table_name)

    return QUERY_ALL_DATA


def get_sql_insert(table_name, data_fields, data_dic={}):

    """
        function: 推理 SQL 插入指令
    :param table_name:  插入的表名
    :param data_dic:    插入的数据-字典形式
    :return:  得到sql 指令
    """

    SQL = "INSERT INTO {table_name}(".format(table_name=table_name)

    SQL += (", ".join(data_fields))
    SQL += ") VALUES ('{"
    SQL += "}', '{".join(data_fields)
    SQL += "}')"

    SQL = SQL.format(**data_dic)

    return SQL

