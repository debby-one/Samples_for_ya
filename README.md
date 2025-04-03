# サンプルプロジェクト

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