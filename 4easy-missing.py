# This Python file uses the following encoding: utf-8
import time
from random import choice

a = ["ta","da","sa","za","ke","ge","so","zo"]

b= ["たタ","だダ","さサ","ざザ","きキ","ぎギ","けケ","げゲ","そソ","ぞ",]


while True:
    print(choice(a))
    time.sleep(3)
    print(choice(b))
    time.sleep(3)
