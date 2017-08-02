# -*- coding: utf-8 -*-
"""
python2实现命令行动态载入的显示效果
https://www.zhihu.com/question/21100416
"""

import sys
import time
import random
from string import ascii_letters

print 'Loading....  ',
sys.stdout.flush()

i = 0
spins = ['/', '-', '\\', '|']

while i <= 10:
    sys.stdout.write('\b{}'.format(spins[i%4]))
    sys.stdout.flush()
    time.sleep(0.2)
    i += 1

print
print 'Loading....  ',
sys.stdout.flush()
i = 0
length = 1

while i <= 10:
    l = random.randint(1, 10)
    num = ''.join(random.sample(ascii_letters, l))
    sys.stdout.write('{}{}\033[K'.format('\b' * length, num))
    sys.stdout.flush()
    time.sleep(0.2)
    length = l
    i += 1

print u"嗯哼？"
