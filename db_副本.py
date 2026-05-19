import sqlite3
import os

DB_NAME = "pet.db"


def get_conn():
	# 1. 检查文件是否存在，不存在则打印提示
	if not os.path.exists(DB_NAME):
		print(f"📂 正在创建数据库文件: {DB_NAME}")

	try:
		# 2. 尝试建立连接
		conn = sqlite3.connect(DB_NAME)
		conn.row_factory = sqlite3.Row
		print(f"✅ 数据库连接成功: {DB_NAME}")  # 调试用，确认连上了
		return conn
	except Exception as e:
		print(f"❌ 数据库连接失败: {e}")
		return None


def init_db():
    conn = get_conn()
    if conn is None:
        return

    cursor = conn.cursor()

    # 👇 这段 SQL 必须在你的代码里被执行一次！
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nick_name TEXT,
        age TEXT,
        sex TEXT,
        weight TEXT
    );
    """

    try:
        cursor.execute(create_table_sql)
        conn.commit()  # 提交保存
        print("✅ 表 'pets' 创建成功！")
    except Exception as e:
        print(f"❌ 建表失败: {e}")
    finally:
        conn.close()
