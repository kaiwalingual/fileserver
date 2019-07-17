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
