#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#I/O
#Python is a dynamic language.
print('hello world')
print('100 + 200 =', 100 + 200)
print(r'///nnn')
print(r'''hello,\n
world''')
print('3.0//2.0 =', 3.0 // 2.0)
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.14159)

#name = input('please enter your name: ')
#print('name =', name)

#list and tuple
classNum = ['1st', '2nd', '3rd']
tuple1 = ('1', 2, '3')

#conditional judgment
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('<00')
else:
    print('>00')

#loop   for...in / while
#dict and set
d = {'bsr': 1, 'a': 2, 'c': 3}
print(d)
