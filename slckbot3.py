import re
import rpcar

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

SLACK_APP_TOKEN="xapp-1-A06CU8YG1EW-6436440292915-7076f73bc5f59398e1bab269c6c2812453eaa8cc1547862b38330452e4b43bdf"
SLACK_BOT_TOKEN="xoxb-147057435126-6436243936467-GBgCtofhUy5Ni1glEc3ELNI7"
# BotTokenの設定
app = App(token=SLACK_BOT_TOKEN)

@app.message(re.compile(r"^!fwbw ((.|\\s)*)$"))
def handle_message(message, say, context):
    # ユーザー名を取得
    user = message['user']
    # 会話メッセージを取得
    talk = context["matches"][0]
    # メッセージを投稿
    say(f"こんにちは! <@{user}>さん、あなたの会話内容は'" + talk + "'です")
    rpcar.fwbw(talk)

# アプリケーションの実行
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()