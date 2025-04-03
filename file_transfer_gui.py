import tkinter as tk
from tkinter import ttk, messagebox
import paramiko

# サーバー接続情報
SERVER_CONFIG = {
    "hostname": "your_server_ip",  # サーバーのIPアドレスまたはホスト名
    "port": 22,                   # SSHのデフォルトポート
    "username": "your_username",  # サーバーのユーザー名
    "password": "your_password"   # パスワード（またはSSH鍵を使用する場合は省略）
}

# ファイルパス設定
REMOTE_FILE_PATH = "/path/to/remote/file.txt"  # サーバー上のファイルパス
LOCAL_DOWNLOAD_PATH = "/path/to/local/downloaded_file.txt"  # ローカルにダウンロードするパス
REMOTE_UPLOAD_PATH = "/path/to/remote/uploaded_file.txt"  # サーバー上にアップロードするパス

def download_file():
    """サーバーからファイルをダウンロードし、内容を表示する"""
    try:
        # SSHクライアントを作成
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # サーバーに接続
        ssh.connect(**SERVER_CONFIG)
        sftp = ssh.open_sftp()

        # ファイルをダウンロード
        sftp.get(REMOTE_FILE_PATH, LOCAL_DOWNLOAD_PATH)
        sftp.close()
        ssh.close()

        # ダウンロードしたファイルの内容を表示
        with open(LOCAL_DOWNLOAD_PATH, "r") as file:
            content = file.read()
            text_widget.delete("1.0", tk.END)  # 既存の内容をクリア
            text_widget.insert(tk.END, content)

        messagebox.showinfo("Success", "ファイルをダウンロードしました。")
    except Exception as e:
        messagebox.showerror("Error", f"ファイルのダウンロード中にエラーが発生しました: {e}")

def upload_file():
    """ローカルファイルをサーバーの別のパスにアップロードする"""
    try:
        # SSHクライアントを作成
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # サーバーに接続
        ssh.connect(**SERVER_CONFIG)
        sftp = ssh.open_sftp()

        # ファイルをアップロード
        sftp.put(LOCAL_DOWNLOAD_PATH, REMOTE_UPLOAD_PATH)
        sftp.close()
        ssh.close()

        messagebox.showinfo("Success", "ファイルをアップロードしました。")
    except Exception as e:
        messagebox.showerror("Error", f"ファイルのアップロード中にエラーが発生しました: {e}")

# GUIのセットアップ
root = tk.Tk()
root.title("ファイル転送ツール")

# フレームの作成
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# テキストウィジェット（ファイル内容表示用）
text_widget = tk.Text(frame, wrap="word", height=20, width=60)
text_widget.grid(row=0, column=0, columnspan=2, pady=10)

# ダウンロードボタン
download_button = ttk.Button(frame, text="ファイルをダウンロード", command=download_file)
download_button.grid(row=1, column=0, padx=5, pady=5)

# アップロードボタン
upload_button = ttk.Button(frame, text="ファイルをアップロード", command=upload_file)
upload_button.grid(row=1, column=1, padx=5, pady=5)

# ウィンドウのサイズ調整
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# アプリケーションの起動
root.mainloop()