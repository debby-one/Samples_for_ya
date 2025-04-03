import tkinter as tk
from tkinter import ttk, messagebox
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
    """データベースからデータを取得する関数"""
    try:
        # データベースに接続
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # SELECT クエリを実行
        query = "SELECT * FROM users;"  # 適切なテーブル名に変更してください
        cursor.execute(query)

        # データを取得
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        messagebox.showerror("Error", f"データベースエラー: {e}")
        return []
    finally:
        if connection:
            connection.close()

def display_data():
    """データを取得してGUIに表示する関数"""
    for row in tree.get_children():
        tree.delete(row)  # 既存のデータをクリア

    rows = fetch_data()
    for row in rows:
        tree.insert("", "end", values=row)

# GUIのセットアップ
root = tk.Tk()
root.title("PostgreSQL データビューア")

# フレームの作成
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# テーブル（Treeview）の作成
columns = ("id", "name", "email")  # 適切なカラム名に変更してください
tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# カラムヘッダーの設定
for col in columns:
    tree.heading(col, text=col.capitalize())
    tree.column(col, width=150)

# スクロールバーの追加
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

# 更新ボタン
refresh_button = ttk.Button(frame, text="データを更新", command=display_data)
refresh_button.grid(row=1, column=0, pady=10)

# ウィンドウのサイズ調整
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# アプリケーションの起動
display_data()  # 起動時にデータを表示
root.mainloop()