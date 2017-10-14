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

