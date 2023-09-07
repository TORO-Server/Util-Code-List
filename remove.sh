#!/bin/bash

# このshファイルがあるディレクトリに移動 (相対パスに対応させるため)
cd $(dirname $0)

# 設定されたディレクトリに移動
cd ここにディレクトリを書く

# "01.zip"で終わるファイル名 以外のzipファイルを削除
find . -type f ! -name "*01.zip" -name "*.zip" -delete

# ログ表示
echo 削除が完了しました
