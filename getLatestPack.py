from urllib import request
import json


def getLatest(User: str, Repository: str):
    # URL
    URL = f"https://api.github.com/repos/{User}/{Repository}/releases/latest"
    # GETリクエスト 送信
    with request.urlopen(URL) as response:
        data = json.load(response)
        return data["assets"][0]["browser_download_url"]


if __name__ == '__main__':
    # -----設定項目----- start
    User = "TORO-Server"
    Repository = "TORO-ResourcePack"
    # -----設定項目----- end
    print(getLatest(User, Repository))
