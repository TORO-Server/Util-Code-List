# Util-Code-List

TORO サーバーで使われている コードの一部

## [remove.sh](/remove.sh)

"01.zip"で終わるファイル名 以外の zip ファイルを削除します。

```sh
bash remove.sh
```

## [getJarFile.py](/getJarFile.py)

現在のディレクトリ内の.jar ファイルを検索し、

ファイル名に指定した文字列 (第一引数) が含まれている

最初にヒットしたファイルをコンソールに出力します。

該当するファイルが見つからない場合は、エラーメッセージを出力します。

```sh
python3 getJarFile.py 含まれている文字列
```

```sh
# 現在のディレクトリに "test-001.jar" という jar ファイルがある場合
python3 getJarFile.py test
```

を実行すると`./test-001.jar`とコンソールに出力されます。

## [getLatestPack.py](/getLatestPack.py)

Github の API を利用して <https://github.com/TORO-Server/TORO-ResourcePack/releases>

の最新のリソースパックのダウンロード URL をコンソールに出力します。

```sh
python3 getLatestPack.py
```

## [editProperty.py](/editProperty.py)

Minecraft のサーバーの設定ファイル `server.properties` のプロパティを変更します。

```sh
python3 editProperty.py 変更したいプロパティ 設定したい値
```

## [getLatestGeyser.py](/getLatestGeyser.py)

最新の GeyserMC をダウンロードするスクリプト

すでに最新版を導入している場合はダウンロードされない

```sh
# Velocity版 GeyserMC をダウンロードする場合
python3 getLatestGeyser.py velocity ./plugins/Geyser-Velocity.jar
# Spigot版 GeyserMC をダウンロードする場合
python3 getLatestGeyser.py spigot ./plugins/Geyser-Spigot.jar
```
