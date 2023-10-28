import re
import sys


def edit_server_properties(file_path, property_key, new_value):
    # ファイルを開く
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # プロパティを探す
    for i, line in enumerate(lines):
        if line.startswith(property_key + "="):
            lines[i] = f"{property_key}={re.escape(new_value)}\n"
    # ファイルを更新する
    with open(file_path, 'w') as file:
        file.writelines(lines)


if __name__ == '__main__':
    # server.properties のファイルパス
    PATH = "server.properties"
    # 変更したいプロパティの名前
    KEY = sys.argv[1:]
    # プロパティに設定したい値
    VALUE = sys.argv[2:]

    edit_server_properties(PATH, KEY, VALUE)
