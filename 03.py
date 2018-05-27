#!/usr/bin/env python
# -*- coding: utf-8 -*-

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
replace_sentence = sentence.replace(",", "").replace(".", "")
split = replace_sentence.split(" ")

len_list = []

for word in split:
    len_list.append(len(word))

print(len_list)
