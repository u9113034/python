# ch26_1.py
import smtplib

from_addr = 'u9113034@gmail.com'              # 設定發信帳號
pwd = input('請輸入 %s 的密碼 : ' % from_addr)  # 要求輸入發信帳號密碼
to_addr_list = ['kuangmao_chou@chentai-tech.com.tw']      # 設定收件人
msg = 'Subject: My first mail using Python\n\
Email from Python'                              # 信件標題與內容
mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                            # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線

