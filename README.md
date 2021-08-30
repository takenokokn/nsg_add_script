# nsg_add_script
# OCIのNSGにセキュリティ・ルールを追加するためのJSONファイルを作成するためのスクリプトです。
  
「list_nsg_add.txt」というテキストファイルを読み込んでJSONファイルを作成するスクリプトになっています。
「list_nsg_add.txt」は各項目を「｜」で区切っています。
項目については、左から順に
・説明
・プロトコル（６はTCP）
・CIDER
・ポートの上限
・ポートの下限
となっていて、1行ごとに1ルールとなっています。
  
## 事前準備
1．「nsg_add_script.py」と同じディレクトリに「list_nsg_add.txt」を配置する。
2．登録したいセキュリティ・ルールを「list_nsg_add.txt」に記載する。
3．「nsg_add_script.py」を実行する。
4．NSG_IDを入力するように言われるので、入力する。
5．完了すると同ディレクトリ内に「nsg_add_rule1.json」ファイルが作成される。

