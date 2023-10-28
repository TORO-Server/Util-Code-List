#!/usr/bin/env python3
import os
import sys

# ===== 説明 ===== start
# 現在のディレクトリ内の.jarファイルを検索し、
# ファイル名に指定した文字列 (第一引数) が含まれている
# 最初にヒットしたファイルを出力します。
# 該当するファイルが見つからない場合は、エラーメッセージを出力します。
# ===== 説明 ===== end

# 第一引数を取得
search_string = sys.argv[1]

# 同じ階層のjarファイルを検索
for file in os.listdir('.'):
    if file.endswith('.jar') and search_string in file:
        print(file)
        sys.exit(0)

# 該当するファイルが見つからなかった場合のメッセージ
print(f"No jar files found containing '{search_string}'")
