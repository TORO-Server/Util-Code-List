from urllib import request
import json

User = "TORO-Server"
Repository = "TORO-ResourcePack"

# URL
URL = f"https://api.github.com/repos/{User}/{Repository}/releases/latest"

# GETリクエスト 送信
with request.urlopen(URL) as response:
    data = json.load(response)
    print(data["assets"][0]["browser_download_url"])
