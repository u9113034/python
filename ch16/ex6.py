# ch16_39.py
import re

msg = '''txt@deepstone.com.tw kkk@gmail.com u9113034@gmail.com kuangmao_chou@chentai-tech.hinet.net'''
pattern = r'''(
    [a-zA-Z0-9_.]+                  # 使用者帳號
    @                               # @符號
    [a-zA-Z0-9-.]+                  # 主機域名domain
    [\.]                            # .符號
    [a-zA-Z]{2,4}                   # 可能是com或edu或其它
    ([\.])?                         # .符號, 也可能無特別是美國
    ([a-zA-Z]{2,4})?                # 國別
    )'''
eMails = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
print('你的郵件列表如下:')
for eMail in eMails:
    print(list(eMail)[0])



