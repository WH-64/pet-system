# import pymysql
#
# def get_conn():
#     return pymysql.connect(
#         host="localhost",
#         user="root",
#         password="WH1037702894",   # 别忘了改
#         database="pet_system",
#         charset="utf8mb4",
#         cursorclass=pymysql.cursors.DictCursor
#     )

import pymysql

def get_conn():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="WH1037702894",   # 记得改
        database="pet_system",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor   # ✅ 关键
    )