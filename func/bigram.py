#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bigram(sentence, case):

    if case == "word" or "char":
        if case == "word":
            split = sentence.split(" ")
        elif case == "char":
            split = sentence.replace(" ", "")
        print(split)
        bigram = ''
        bigram_list = []

        for i in range(len(split)-1):
            bigram += split[i]
            if case == "word":
                bigram += ' ' + split[i+1]
            else:
                bigram += split[i+1]
            bigram_list.insert(i, bigram)
            bigram = ''

        return bigram_list
    else:
        print('error')

