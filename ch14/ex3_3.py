str1 = 'Python 入門到高手之路 '
str2 = '作者:洪錦魁 '
str3 = '深石數位科技 '
str4 = 'DeepStone Corporation'
str5 = 'Deep Learning'

with open('ex3_3.txt', 'w') as fn:
    fn.write(str1 + ' ')
    fn.write(str2 + ' ')
    fn.write(str3 + ' ')
    fn.write(str4 + ' ')
    fn.write(str5)