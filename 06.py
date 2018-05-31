#!/usr/bin/env python
# -*- coding: utf-8 -*-

from func.bigram import bigram

sentence1 = "paraparaparadise"
sentence2 = "paragraph"

X = set(bigram(sentence1, "char"))
Y = set(bigram(sentence2, "char"))

# 和集合
union = X.union(Y)
print(union)

# 差集合
diff = X.difference(Y)
print(diff)
# 積集合
intersection = X.intersection(Y)
print(intersection)

# 'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
print('se' in intersection)
