# ch15_30.py
import logging

logging.basicConfig(filename='mydebug.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug('程式開始')

def sumrange(n):
    logging.debug('sumrange %s 計算開始' % n)
    ans = 1
    for i in range(1, n + 1):
        ans += i
        logging.debug('i = ' + str(i) + ', ans = ' + str(ans))
    logging.debug('sumrange %s 計算結束' % n)
    return ans

num = 100
print("sumrange(%d) = %d" % (num, sumrange(num)))
logging.debug('程式結束')




