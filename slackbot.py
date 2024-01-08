#!/usr/bin/env python
# -*- coding: utf-8 -*-

#■基本的に下記のページの手順に沿って作成
#https://qiita.com/seratch/items/1a460c08c3e245b56441
#・必要なライブラリのインストールは、「pip install slack_bolt」でOK
#・以下のコマンドは、自分の環境ではうまく環境変数が設定できなかった
#>export SLACK_APP_TOKEN=xapp-<自分のトークンの値>
#>export SLACK_BOT_TOKEN=xoxb-<自分のトークンの値>
#→なので、「os.environ["SLACK_APP_TOKEN"]」の部分に直接トークンを記載した(本当はよくない)
#・「Enable Socket Mode」をONにした時に表示されるアプリレベルトークンを、
#”再度”取得する手順↓
#https://deep.tacoskingdom.com/blog/156

import logging
import os
from slack_sdk import WebClient
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import serial

logging.basicConfig(level=logging.DEBUG)

SLACK_APP_TOKEN="xapp-1-A06CU8YG1EW-6436314296066-02691e68f92fabac25d1ce48ef9c957fe8a97dd78d033ce0489cd2121b1943d5"
SLACK_BOT_TOKEN="xoxb-147057435126-6436243936467-e4rsayJyzVpJAc4Ljdo7cYWu"
Genkan_ch="G5KS3J8LF"

#シリアル通信をする場合に必要な処理：シリアル通信開始の処理
#各自の環境に応じてシリアル通信のポート名(「/dev/ttyUSB1」のところ)を設定すること
#ser = serial.Serial('/dev/ttyUSB1', 115200)
ser = serial.Serial('/home/dashi119/bin', 115200)


app = App(token=SLACK_BOT_TOKEN)
client = WebClient(SLACK_BOT_TOKEN)

# イベント API：受信したメッセージに含まれる文字列に応じた処理を実行
@app.message("はい")
def handle_messge_evnts(message, say):
#	ser.write("Open")#シリアル通信をする場合に必要な処理：コマンドをシリアル通信で送信
	say(f" <@{message['user']}> はい")
@app.message("いいえ")
def handle_messge_evnts(message, say):
#	ser.write("Close")#シリアル通信をする場合に必要な処理：コマンドをシリアル通信で送信
	say(f" <@{message['user']}> いいえ")

# ショートカットとモーダル：ショートカット操作に応じた処理を実行
@app.shortcut("unlock_door")
def handle_shortcut(ack, body: dict, client: WebClient, say):
	ack()
#	ser.write("Open")#シリアル通信をする場合に必要な処理：コマンドをシリアル通信で送信
	say(channel=Genkan_ch, text="unlocked")

@app.shortcut("lock_door")
def handle_shortcut(ack, body: dict, client: WebClient, say):
	ack()
#	ser.write("Close")#シリアル通信をする場合に必要な処理：コマンドをシリアル通信で送信
	say(channel=Genkan_ch, text="locked")
	
# ショートカットとモーダル：TODO：カギの開閉状況を何らかの方法で検出して送信
@app.shortcut("check_door")
def handle_shortcut(ack, body: dict, client: WebClient, say):
	ack()
	#say(channel=Genkan_ch, text="checked")
    #TODO：玄関の写真を撮影する処理
	#添付ファイルを送信する方法の例
	upload_text_file = client.files_upload(
		channels=Genkan_ch,
		title="Test text data",
		file="./genkan.jpg",
		initial_comment="checked:",
	)

if __name__ == "__main__":
	handler = SocketModeHandler(app,SLACK_APP_TOKEN)
	handler.start()