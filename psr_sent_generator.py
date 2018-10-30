# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:35:29 2018

Comp Syntax
used to make sentences with rules
"""

from random import choice
from collections import defaultdict
import sys

def load_grammar(filename):
    f = open(filename)
    rules = defaultdict(list)
    for line in f:
        lhs = line.split()[0]
        rhs = line.split()[2:]
        rules[lhs].append(rhs)
    return rules

def make_template(rules, root_symbol):
    template = []
    if root_symbol not in rules:
        return [root_symbol]
    else:
        template.append(root_symbol)
        rhs = choice(rules[root_symbol])
        for part in rhs:
            template.append(make_template(rules, part))
    return template

def load_lexicon(filename):
    f = open(filename)
    lexicon = defaultdict(list)
    lexicon["<NULL>"] = [""]
    for line in f:
        linelist = line.split()
        lexicon[linelist[1]].append(linelist[0] + " ")
    return lexicon
    
def make_sentence(template, lexicon):
    sentence = ""
    for POS in template:
        candidates = lexicon[POS]
        sentence += choice(candidates)
    sentence = sentence[0].upper() + sentence[1:]
    sentence += choice([".", "!", "..."])
    return sentence

if __name__ == "__main__":
    grammar = load_grammar('rules.txt')
    print(make_template(grammar, "S"))
