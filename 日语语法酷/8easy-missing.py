# This Python file uses the following encoding: utf-8
import time
from random import choice

a = ["ta","da","sa","za","ki","gi","ti/chi","di","ke","ge","te","de","ko","go","so","zo"]

b= ["たタ","だダ","さサ","ざザ","きキ","ぎギ","ちチ","ぢヂ","けケ","げゲ","こコ","ごゴ","そソ","ぞ",]


while True:
    print(choice(a))
    time.sleep(3)
    print(choice(b))
    time.sleep(3)
