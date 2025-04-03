# サンプルプロジェクト

このプロジェクトでは、以下の4つのプログラムを含みます。

1. **PostgreSQL データベースに接続してデータを取得する CUI プログラム**
2. **PostgreSQL データベースに接続してデータを取得し、`tkinter` を使用して表示する GUI プログラム**
3. **`paramiko` を使用して Linux サーバー上のファイルを操作する CUI プログラム**
4. **`paramiko` を使用して Linux サーバー上のファイルを操作し、`tkinter` を使用して表示する GUI プログラム**

---

## 1. PostgreSQL データ取得 (CUI)

### 概要
このプログラムは、`psycopg2` ライブラリを使用して PostgreSQL データベースに接続し、`SELECT` 文を実行してデータを取得します。取得したデータはコンソールに表示されます。

### ファイル
- **`db_query.py`**

### 必要なライブラリ
- `psycopg2`

### 実行方法
1. 必要なライブラリをインストールします。
   ```bash
   pip install psycopg2
   ```
2. `db_query.py` を実行します。
   ```bash
   python db_query.py
   ```

---

## 2. PostgreSQL データビューア (GUI)

### 概要
このプログラムは、`tkinter` を使用して GUI を作成し、`psycopg2` ライブラリを使用して PostgreSQL データベースに接続します。`SELECT` 文を実行してデータを取得し、結果を GUI 上に表示します。

### ファイル
- **`db_gui.py`**

### 必要なライブラリ
- `psycopg2`
- `tkinter`（標準ライブラリ）

### 実行方法
1. 必要なライブラリをインストールします。
   ```bash
   pip install psycopg2
   ```
2. `db_gui.py` を実行します。
   ```bash
   python db_gui.py
   ```

### 使用方法
- プログラムを起動すると、データベースから取得したデータが表形式で表示されます。
- 「データを更新」ボタンをクリックすると、データを再取得して表示を更新します。

---

## 3. ファイル転送ツール (CUI)

### 概要
このプログラムは、`paramiko` を使用して Linux サーバーに接続し、指定されたファイルをダウンロードします。ダウンロードしたファイルの内容をコンソールに表示し、別のパスにアップロードします。

### ファイル
- **`file_transfer.py`**

### 必要なライブラリ
- `paramiko`

### 実行方法
1. 必要なライブラリをインストールします。
   ```bash
   pip install paramiko
   ```
2. `file_transfer.py` を実行します。
   ```bash
   python file_transfer.py
   ```

---

## 4. ファイル転送ツール (GUI)

### 概要
このプログラムは、`paramiko` を使用して Linux サーバーに接続し、指定されたファイルをダウンロードします。ダウンロードしたファイルの内容を `tkinter` の GUI に表示し、別のパスにアップロードします。

### ファイル
- **`file_transfer_gui.py`**

### 必要なライブラリ
- `paramiko`
- `tkinter`（標準ライブラリ）

### 実行方法
1. 必要なライブラリをインストールします。
   ```bash
   pip install paramiko
   ```
2. `file_transfer_gui.py` を実行します。
   ```bash
   python file_transfer_gui.py
   ```

### 使用方法
1. 「ファイルをダウンロード」ボタンをクリックすると、指定されたリモートファイルがダウンロードされ、その内容が表示されます。
2. 「ファイルをアップロード」ボタンをクリックすると、ダウンロードしたファイルが別のリモートパスにアップロードされます。

---

## 注意事項

### PostgreSQL プログラム
- **接続情報の設定**:
  `db_query.py` および `db_gui.py` 内の `DB_CONFIG` に正しいデータベース接続情報を設定してください。
- **テーブル名とカラム名**:
  `users` テーブルやカラム名（`id`, `name`, `email`）は、実際のデータベース構造に合わせて変更してください。

### ファイル転送プログラム
- **接続情報の設定**:
  `file_transfer.py` および `file_transfer_gui.py` 内の `SERVER_CONFIG` に正しいサーバー接続情報を設定してください。
- **ファイルパスの設定**:
  `REMOTE_FILE_PATH`, `LOCAL_DOWNLOAD_PATH`, `REMOTE_UPLOAD_PATH` を適切なパスに変更してください。
- **SSH 鍵の使用**:
  パスワード認証ではなく SSH 鍵を使用する場合は、`SERVER_CONFIG` に `key_filename` を追加してください。
  ```python
  "key_filename": "/path/to/private_key"
  ```

---

## ライセンス
このプロジェクトは自由に使用、変更、配布することができます。
