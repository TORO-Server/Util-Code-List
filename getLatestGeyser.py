from urllib import request
import json
import sys
import hashlib
import os


# どのサーバー用の GeyserMC をダウンロードするか
TPYE = sys.argv[1]
# GeyserMC の jarファイルパス
PATH = sys.argv[2]


def getLatest_sha256(type: str):
    # URL
    URL = f"https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest"
    # GETリクエスト 送信
    with request.urlopen(URL) as response:
        data = json.load(response)
    return data["downloads"][type]["sha256"]


def getFile_sha256(path: str):
    hash = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            # ファイルをチャンクごとに読み込んでハッシュを計算
            for byte_block in iter(lambda: f.read(4096), b""):
                hash.update(byte_block)
    except FileNotFoundError:
        return None
    # sha256 のハッシュ値を return
    return hash.hexdigest()


def downloadLatest(type: str, path: str):
    # URL
    URL = f"https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/{type}"
    # フォルダが存在しない場合は作成
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    # ファイル ダウンロード
    binary = request.urlopen(URL).read()
    with open(PATH, mode="wb") as f:
        f.write(binary)


sha256_cloud = getLatest_sha256(TPYE)
sha256_local = getFile_sha256(PATH)

if sha256_cloud != sha256_local:
    print(f"GeyserMC {TPYE.capitalize()} Download...")
    downloadLatest(TPYE, PATH)
    print(f"{PATH} Done")
