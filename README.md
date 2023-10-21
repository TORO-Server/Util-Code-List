# Util-Code-List

TORO サーバーで使われている コードの一部

## [remove.sh](/remove.sh)

"01.zip"で終わるファイル名 以外の zip ファイルを削除する ShellScript

## [getJarFile.sh](/getJarFile.sh)

現在のディレクトリ内の.jar ファイルを検索し、

ファイル名に指定した文字列 (第一引数) が含まれている

最初にヒットしたファイルを出力します。

該当するファイルが見つからない場合は、エラーメッセージを出力します。

## [getLatestAssets.py](/getLatestAssets.py)

Github の API を利用して <https://github.com/TORO-Server/TORO-ResourcePack/releases>

の最新のリソースパックのダウンロード URL をコンソールに出力します。
