#!/usr/bin/python
#モジュール属性argvを取得するため
import sys
#sxapyモジュールのpromiscpingパッケージをインポート
from scapy.all import promiscping
#引数の個数が2未満なら、スクリプト自身とnet情報を出力する
if len(sys.argv) < 2:
 print sys.argv[0] + " <net>"
 sys.exit()
#1つ目の引数のリモートスニファを1ラインで検出する
promiscping(sys.argv[1])
