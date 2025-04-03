import psycopg2

# PostgreSQL 接続設定
DB_CONFIG = {
    "host": "localhost",        # データベースホスト
    "port": 5432,               # デフォルトポート
    "user": "your_username",    # ユーザー名
    "password": "your_password",# パスワード
    "dbname": "your_database"   # データベース名
}

def fetch_data():
    connection = None
    try:
        # データベースに接続
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        print("Connected to the database.")

        # SELECT クエリを実行
        query = "SELECT * FROM users;"  # 適切なテーブル名に変更してください
        cursor.execute(query)

        # データを取得
        rows = cursor.fetchall()
        print("Data retrieved:")

        # データを返す
        return rows
    except Exception as e:
        print("Error:", e)
    finally:
        # 接続を閉じる
        if connection:
            connection.close()
            print("Database connection closed.")

# 実行
if __name__ == "__main__":
    rows = fetch_data()
    for row in rows:
        print(row)