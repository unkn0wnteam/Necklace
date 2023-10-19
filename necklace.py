# -*- coding:utf -8 -*-
#!/usr/bin/python3
import random
print("> Necklace V2 <")
s = '123412343718372831234===---___QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm==-#@ajdkajfie'
o = 1
l = input('Password length?'+ "\n")
l = int(l)
for n in range(o):
    p =''
    for i in range(l):
        p += random.choice(s)
    print(p)