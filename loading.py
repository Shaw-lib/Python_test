# -*- coding: utf-8 -*-
# 电脑“想了想”,然后发出了疑惑“嗯哼？”

from time import sleep
import sys

itime = 0

while itime < 3:
    for i in r'\|/-|/':
        sys.stdout.write(i + '\r')
        sleep(0.08)
        itime += 0.08

print u"嗯哼？"
