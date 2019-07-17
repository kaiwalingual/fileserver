# カイワリンガル ファイルサーバ

## 環境設定
必要なもの
 * python 3.6
  * pipenv
  
  ### pipenvのインストール
  ```bash
  $ pip install --user pipenv
  ```
  
  ## 実行方法
  githubからcloneします
  
  ```bash
  $ git clone git@github.com:kaiwalingual/fileserver.git
  $ cd fileserver
  ```
  
  次のコマンドで必要なパッケージをインストールします
  
  ```bash
  $ pipenv install .
```

次のコマンドで実行できます

```bash
$ pipenv run python main.py
# OR
$ pipenv shell
(something)$ python main.py
```

## API
エンドポイント | リクエスト | 引数、返り値 | 説明
---| --- | --- | ---
`/` | `POST` | `file`:送信する写真、返り値として`xxxxx.jpg`と名前を返す | 写真を送りつけます
`/xxxxxxx.jpg` | `GET` | | POSTしたときに受け取った名前で写真が取得できる
`/min/xxxxxxx.jpg` | `GET` | | POSTしたときに受け取った名前で**サイズを縮めた**写真が取得できる
