#!/usr/bin/env python3

def return_evens(num_list):
    evens = [i for i in num_list if i % 2 == 0]
    return evens

def make_exclamation(sentence_list):
    ex = [s + "!" for s in sentence_list]
    return ex