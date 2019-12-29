
from DBConnection.Query import get_sql_query_all_data,  get_sql_insert
from DBConnection.Config import DATABASE_Fields
from DBConnection.DBConnection import DBConnection




if __name__ == "__main__":

    # 建立数据库连接
    db = DBConnection()

    # 待插入的数据
    dic = {"name": "elgong", "address": "123", "city": 1, "email": "1552460315"}

    # 得到插入语句
    SQL = get_sql_insert("student", DATABASE_Fields, dic)
    print("SQL:  " + SQL)

    # 执行插入语句
    db.insert_data_by_sql(SQL)

    #　查询数据库
    data = db.query_data_by_sql(get_sql_query_all_data(table_name="student"))

    # 关闭数据库
    db.close()

    # 打印查询到的信息
    print("data: ")
    print(data)




