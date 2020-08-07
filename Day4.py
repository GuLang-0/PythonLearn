#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#限制实例的属性(仅仅对当前类的实例起作用)
class Student(object):
    __slots__ = ('name')

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value


#   __str__()返回用户看到的字符串   __repr__()返回程序开发者看到的字符串
#   __iter__()返回一个迭代对象     __next__()拿到下一个值
#   __getitem__()实现像list那样按照下标取出元素
#   __getattr__()调用不存在的属性时
#   __call__()直接对实例进行调用    callable()判断是否是可调用的对象

#枚举类
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                       'Sep', 'Oct', 'Nov', 'Dec'))


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


#错误处理
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

#Python内置的logging模块--记录错误信息