# NSGのルールを簡単に設定するためのスクリプト
import json
import os
import sys
from types import AsyncGeneratorType

# Python実行ファイルパスを指定
file_path = os.path.dirname(__file__)

# ファイルパスが格納できなかったときに処理を終了
if len(file_path) == 0:
    print("ファイルパスが格納できなかったので、処理を終了します。")
    sys.exit()
elif not os.path.exists(file_path + "/list_nsg_add.txt") :
    # 元になるlist_nsg_add.txtが存在しない場合、処理を終了
    print("「nsg_add_script.py」が配置されているディレクトリに「list_nsg_add.txt」が存在しません。\n手順に従って「list_nsg_add.txt」を配置して下さい。")
    sys.exit()

# NSGのIDの値を入力値から取得
nsg_id = input("ルールを追加するNSGのIDを入力してください： ")

# テキストファイルから1行ずつ読み込んだ後に、カンマごとに区切って多次元配列を作っている
list = []
with open(file_path + "/list_nsg_add.txt", encoding="utf_8") as f:
    for line in f:
        line_sp = line.split()
        for sp in line_sp:
            unit = sp.split("|")
            list.append(unit)

# 変わらない値を挿入する
add_list = []
for add in list:
    add.insert(1, "INGRESS")
    add.insert(2, "false")
    add_list.append(add)

# テキストファイルから読み込んだポート番号の値を整形する
tcp_list = []
for value in add_list:
    if value[5].lower() == "all":
        dic = {"tcpOptions": None}
    else:
        dic = {"tcpOptions": {"destinationPortRange": {"max": value[5], "min": value[6]}}}
    tcp_list.append(dic)

# 連想配列にするためのKeyを作成
key = ["description", "direction", "isStateless", "protocol", "source"]

# Keyを使用して、連想配列を作る
dic_list = [dict(zip(key, item)) for item in list]

# 最終の連結を行う
result_list = []
i = 0
for value in dic_list:
    value.update(tcp_list[i])
    result_list.append(value)
    i += 1

output = []
row_count = 0
i = 0

for n in range(len(result_list)):
    # 行数のカウント
    row_count += 1
    # リストを1行ずつ取り出す
    output.append(result_list[n])
    if row_count == 25 or n + 1 == len(result_list):
        dct = {"nsgId": nsg_id, "securityRules": output}
        # Json形式に変換
        jsonstr = json.dumps(dct, indent=4, ensure_ascii=False)
        i += 1
        # ファイルに出力
        with open(
            file_path + "/nsg_add_rule" + str(i) + ".json", "w"
        ) as f:
            f.write(jsonstr)
        # 変数を初期化
        output = []
        row_count = 0

print(file_path + "にファイルを出力しました。")
