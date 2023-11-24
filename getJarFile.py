#!/usr/bin/env python3
import os
from sys import argv

# ===== 説明 ===== start
# 現在のディレクトリ内の.jarファイルを検索し、
# ファイル名に指定した文字列 (第一引数) が含まれている
# 最初にヒットしたファイルを出力します。
# 該当するファイルが見つからない場合は、エラーメッセージを出力します。
# ===== 説明 ===== end


# 第一引数を取得
search_string = argv[1] if len(argv) != 1 else ""


# 指定された階層のjarファイルを検索して、
# 引数 search_string の文字が含まれていた場合、
# その jarファイルのパスを return する。
# なかった場合はエラーメッセージを return する。
def getJarPath(path: str, search_string=""):
    for file in os.listdir(path):
        if file.endswith('.jar') and search_string in file:
            return os.path.join(path, file)
    # 該当するファイルが見つからなかった場合のメッセージ
    return f"No jar files found containing '{search_string}'"


# コンソールに出力
print(getJarPath(".", search_string))
