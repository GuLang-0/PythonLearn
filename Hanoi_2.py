#汉诺塔的移动的实现。
def Hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        Hanoi(n - 1, a, c, b)
        Hanoi(1, a, b, c)
        Hanoi(n - 1, b, a, c)


# s = input()
# n = int(s)
# Hanoi(n, 'A', 'B', 'C')

#高级特性
#切片
#迭代(isinstance(),Iterable)
#列表生产式
list1 = [x * x for x in range(2, 6) if x != 4]
print(list1)
#生成器 generator 可迭代对象
g = (x * x for x in range(1, 5))
for n in g:
    print(n)
#迭代器 可以被next()函数调用并不断返回下一个值的对象 (isinstance() Iterator)

#Functional Programming
print(list(map(str, [1, 2, 3, 4, 5])))  #map()  reduce()


#filter() --过滤序列
#--回数--
def is_palindrome(n):
    x = str(n)
    for k in range(len(x) // 2):
        return x[k] == x[len(x) - 1 - k]


#sorted() --排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.upper, reverse=True))

#匿名函数  --lambda
#装饰器    decorator    @语法
import functools


def log(func):
    @functools.wraps(func)  #把原始函数的__name__等属性复制到wrapper()函数中
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2020-8-6')


#偏函数     functools.partial