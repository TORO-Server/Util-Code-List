from urllib import request
import json
from sys import argv
import hashlib
import os


# jarファイルパス
PATH = argv[1] if len(argv) != 1 else ""


def getBuildObj(Name: str):
    # 最新のバージョン 取得
    with request.urlopen(f"https://api.papermc.io/v2/projects/{Name}") as response:
        data = json.load(response)
        VERSION = data["versions"][-1]
    # 最新のビルド 取得
    with request.urlopen(f"https://api.papermc.io/v2/projects/{Name}/versions/{VERSION}/builds") as response:
        data = json.load(response)
        item = [item for item in data["builds"]
                if item["channel"] == "default"][-1]
        BUILD = item["build"]
        FILE = item["downloads"]["application"]["name"]
        SHA256 = item["downloads"]["application"]["sha256"]
    # 最新バージョンの情報を出力
    return {
        "name": Name,
        "version": VERSION,
        "build": BUILD,
        "file": FILE,
        "sha256": SHA256
    }


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


def downloadLatest(LatestObj: object, path: str):
    # URL
    URL = f"https://api.papermc.io/v2/projects/{LatestObj['name']}/versions/{LatestObj['version']}/builds/{LatestObj['build']}/downloads/{LatestObj['file']}"
    # フォルダが存在しない場合は作成
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path) and not os.path.isfile(path):
        os.makedirs(dir_path)
    # ファイル ダウンロード
    binary = request.urlopen(URL).read()
    download_path = os.path.join(dir_path, LatestObj["file"])
    with open(download_path, mode="wb") as f:
        f.write(binary)
    if path != download_path and os.path.isfile(path):
        os.remove(path)

    return download_path


LatestObj = getBuildObj("velocity")

# 最新版の Velocity のファイルのハッシュ値
sha256_cloud = LatestObj["sha256"]

# ローカルにある Velocity のファイルのハッシュ値
sha256_local = getFile_sha256(PATH)

# 最新版の Velocity とローカルにある Velocity のハッシュ値が違っていたら
if sha256_cloud != sha256_local:
    # ダウンロードする
    print(f"{LatestObj["file"]} Download...")
    path = downloadLatest(LatestObj, PATH)
    print(f"{path} Done")
