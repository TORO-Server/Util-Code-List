import re
import sys
import hashlib


# server.properties のファイルパス
PATH = "server.properties"
# 変更したいプロパティの名前
KEY = sys.argv[1]
# プロパティに設定したい値
VALUE = sys.argv[2]


def edit_server_properties(file_path, property_key, new_value):
    # ファイルを開く
    with open(file_path, 'r') as file:
        lines = file.readlines()
    sha256_old = hashlib.sha256("\n".join(lines).encode()).hexdigest()

    # プロパティを探す
    for i, line in enumerate(lines):
        # プロパティを更新
        if line.startswith(property_key + "="):
            lines[i] = f"{property_key}={re.escape(new_value)}\n"
    sha256_new = hashlib.sha256("\n".join(lines).encode()).hexdigest()

    # もしファイルに変更がなかったら return
    if sha256_old == sha256_new:
        return

    # ファイルを更新する
    with open(file_path, 'w') as file:
        file.writelines(lines)


edit_server_properties(PATH, KEY, VALUE)
