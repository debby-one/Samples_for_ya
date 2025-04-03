import paramiko
import os

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

def transfer_file():
    try:
        # SSHクライアントを作成
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # サーバーに接続
        ssh.connect(**SERVER_CONFIG)
        print("Connected to the server.")

        # SFTPセッションを開始
        sftp = ssh.open_sftp()

        # ファイルをダウンロード
        print(f"Downloading file from {REMOTE_FILE_PATH} to {LOCAL_DOWNLOAD_PATH}...")
        sftp.get(REMOTE_FILE_PATH, LOCAL_DOWNLOAD_PATH)
        print("File downloaded successfully.")

        # ダウンロードしたファイルの内容を表示
        with open(LOCAL_DOWNLOAD_PATH, "r") as file:
            content = file.read()
            print("File content:")
            print(content)

        # ファイルを別のパスにアップロード
        print(f"Uploading file to {REMOTE_UPLOAD_PATH}...")
        sftp.put(LOCAL_DOWNLOAD_PATH, REMOTE_UPLOAD_PATH)
        print("File uploaded successfully.")

        # SFTPセッションを終了
        sftp.close()
    except Exception as e:
        print("Error:", e)
    finally:
        # SSH接続を閉じる
        ssh.close()
        print("Connection closed.")

# 実行
if __name__ == "__main__":
    transfer_file()