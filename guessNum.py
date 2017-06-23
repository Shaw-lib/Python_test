# -*- coding: utf-8 -*-
# author:shwb
# 二分法猜数字小游戏。
# 计算机科学和Python编程导论L3P9
print "Please think of a number between 0 and 100!"

high = 101 # 如果这里设置100，则猜测的最大值为99。
low = -1 # 如果这里设置0，则猜测的最小值为1。（我承认这是比较懒得做法。ORZ）
guess = 50

while True:
    choice = raw_input("Is your secret number %s?\n\
Enter 'h' to indicate the guess is too high.\
Enter 'l' to indicate the guess is too low.\
Enter 'c' to indicate I guessed correctly." % guess)

    if choice == 'h':
        high = guess
        guess = high - (high-low)/2
    elif choice == 'l':
        low = guess
        guess = low + (high-low)/2
    elif choice == 'c':
        print "Game over. Your secret number was: %s" % guess
        break
    else:
        print "Sorry, I did not understand your input."
