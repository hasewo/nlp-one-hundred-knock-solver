#!/usr/bin/env python
# -*- coding: utf-8 -*-

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
split = sentence.split(" ")
number = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dic = {}

for value in range(len(split)):
    if value in number:
        key = split[value][0]
    else:
        key = split[value][0:2]
    data = {key: value}
    dic.update(data)

print(dic)