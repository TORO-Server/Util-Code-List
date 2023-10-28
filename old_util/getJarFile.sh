#!/bin/bash

# ===== 説明 ===== start
# 現在のディレクトリ内の.jarファイルを検索し、
# ファイル名に指定した文字列 (第一引数) が含まれている
# 最初にヒットしたファイルを出力します。
# 該当するファイルが見つからない場合は、エラーメッセージを出力します。
# ===== 説明 ===== end

# 第一引数を取得
search_string=$1

# 同じ階層のjarファイルを検索
for file in ./*.jar; do
    # ファイル名に検索文字列が含まれているか確認
    if [[ $file == *"$search_string"* ]]; then
        echo $file
        exit 0
    fi
done

# 該当するファイルが見つからなかった場合のメッセージ
echo "No jar files found containing '$search_string'"
