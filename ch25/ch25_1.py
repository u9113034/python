# ch25_1.py
from twilio.rest import Client

# 你從twilio.com申請的帳號
accountSid='AC6f4f27424638d82c6044d53cba1c57f7'
# 你從twilio.com獲得的圖騰
authToken='0147909b2ca14681b82eeafd62931747'

client = Client(accountSid, authToken)
message = client.messages.create (
            from_ = "+18327898876",         # 這是twilio.com給你的號碼
            to = "+886965709875",           # 全泰手機
            body = '''declare 宣布;宣稱
denounce 指責;譴責
denounciation 公開譴責;彈劾
depict 描繪;描述
deprive 剝奪;使喪失
despise 鄙視;嫌惡(=disdain)''' )       # 發送的訊息
