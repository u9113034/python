str1 = 'Python 入門到高手之路 '
str2 = '作者:洪錦魁 '
str3 = '深石數位科技 '
str4 = 'DeepStone Corporation'
str5 = 'Deep Learning'

with open('ex3_1.txt', 'w') as fn:
    fn.write(str1 + '\n')
    fn.write(str2 + '\n')
    fn.write(str3 + '\n')
    fn.write(str4 + '\n')
    fn.write(str5)