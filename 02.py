#!/usr/bin/env python
# -*- coding: utf-8 -*-

word1 = "パトカー"
word2 = "タクシー"
combine = ""

for i, j in zip(word1, word2):
    combine += i
    combine += j

print(combine)