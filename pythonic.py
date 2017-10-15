# 遍历一个范围内的数字
for i in range(10):
    print(i)

#遍历一个集合
colors = ['red', 'orange', 'blue', 'yellow']
for color in colors:
    print(color)


#反向遍历

for color in reversed(colors):
    print(color)

#遍历一个集合及下标
for i, color in enumerate(colors):
    print(i, color)

#遍历两个集合
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

for name, color in zip(names, colors):
    print(name, '--->', color)


#有序的遍历
print(sorted(colors, key=len))
print(sorted(colors, key=len, reverse=True))

#调用一个函数直到遇到标记值
'''
blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)

'''
from functools import partial
import os
print(os.getcwd())

blocks = []
with open('./pythonic_style/README.md') as f:
    for block in iter(partial(f.read, 32), ''):
        blocks.append(block)

print(blocks)

#在循环内识别多个退出点
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

#遍历字典的key
d = {'matthew':'blue', 'rachel':'green', 'raymond':'red'}

for k in d:
    print(k)

for k in d.keys():
    if k.startswith('r'):
        print(k)

#遍历一个字典的key和value
for k, v in d.items():
    print(k, '--->', v)

#构建字典
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(zip(names, colors))
print(d)

#用字典计数
colors = ['red', 'green', 'red', 'blue', 'green', 'red']

d = {}

for color in colors:
    d[color] = d.get(color, 0) + 1

import collections

d = collections.defaultdict(int)    
for color in colors:
    d[color] += 1

#用字典分组

names = ['raymond', 'rachel', 'matthew', 'roger',
        'betty', 'melissa', 'judith', 'charlie']

d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)


d = collections.defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

#字典popitem是原子的
d = {'matthew':'blue', 'rachel':'green', 'raymond':'red'}
while d:
    key, value = d.popitem()
    print(key, '--->', value)

#连接字典
import argparse
defaults = {'color':'red', 'user':'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# d = defaults.copy()
# d.update(os.environ)
# d.update(command_line_args)

d = collections.ChainMap(command_line_args, os.environ, defaults)
print(d)

# 用关键字参数提高函数调用的可读性
#twitter_search('@obama', False, 20, True)

#better
#twitter_search('@obama', retweets=False, numtweets=20, popular=True)

#unpack序列
p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

fname, lname, age, email = p

print(fname, lname, age, email)
print(p)

#更新多个变量的状态
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        x, y = y, x + y

#连接字符串
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

print(', '.join(names))

#更新序列

names = collections.deque(['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie'])
del names[0]
print(names)
names.popleft()
print(names)
names.appendleft('mark')
print(names)

#打开关闭文件

with open('data.txt') as f:
    data = f.read()


#如何使用锁
#old method
import threading
lock = threading.Lock()

lock.acquire()
try:
    print('Critical section 1')
finally:
    lock.release()

#new method
with lock:
    print('Critical section 1')