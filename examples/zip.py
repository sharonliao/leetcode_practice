# 用zip同时遍历两个iterator
# 要求两个list的长度要一样，不然一个list耗尽zip就停止了
names = ['cecilia', 'lise', 'marie']
letters = [len(x) for x in names]
max_letters = 0
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

names.append('Rosalind')

import itertools

for name, count in itertools.zip_longest(names, letters):
    print(f"{name}:{count}")
"""
cecilia:7
lise:4
marie:5
Rosalind:None
"""
