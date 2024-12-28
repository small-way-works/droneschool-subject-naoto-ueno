# インストール
## クローン
$ git clone https://github.com/small-way-works/droneschool-subject-naoto-ueno.git

## ライブラリ追加
```
$ cd droneschool-subject-naoto-ueno
$ pip install -r requirements.txt
```
# 実行
## テスト実行
ハードコードされた樹木座標に基づき飛行します。
```
$ python exam_program.py
```

## データを渡して実行
JSONファイルに樹木座標を記載しそのデータに基づき飛行します。
```
$ python exam_program.py --tree_file example.json
```
JSONのフォーマットはexample.jsonを参照してください。

# プログラムの概要
このプログラムは、樹木の形状データ等を取得するため、樹木周囲を飛行することを想定しています。
1. 樹木の中心座標の配列をJSONファイルで渡します（--tree-fileオプション）。単位はメートル
2. 回転半径、高度は現在ハードコードされています。
3. フライトプロセス
  - GUIDEモードへ移行
  - アーム時にホームポジションの座標を原点に設定
  - 原点の緯度経度を用いて樹木位置の緯度経度を取得
  - 離陸
  - 樹木ごとのに周囲のウェイポイントを計算し飛行する
  - 全ての樹木の周囲を飛行したらRTLモードへ移行
  