# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 12:56:19 2018

comp_syntax
"""

from random import choice
from collections import defaultdict

class State(object):
    def __init__(self, POS, output, transitions):
        self.POS = POS
        self.output = output
        self.transitions = transitions
    def __repr__(self):
        return self.POS + "," + self.output + "," + str(self.transitions)
    def pick_transition(self):
        return choice(self.transitions)
        
        
def load_machine(filename):
    f = open(filename)
    states = {}
    for line in f:
        linelist = line.split()
        POS = linelist[0]
        output = linelist[1]
        transitions = linelist[2:]
        state = State(POS, output, transitions)
        states[POS] = state
    f.close()
    return states

def make_template(states):
    current_state = states["<START>"]
    template = []
    while current_state.POS != "<END>":
        template.append(current_state.output)
        current_state = states[current_state.pick_transition()]
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
        sentence +=choice(candidates)
    sentence = sentence.replace(sentence[0], sentence[0].upper())[:-1]
    sentence += choice([".", "!", "..."])
    return sentence
    

if __name__ == "__main__":
    states = load_machine("states.txt")
    lexicon = load_lexicon('lexicon.txt')
    print(lexicon)
    for i in range(10):
        template = make_template(states)
        print(make_sentence(template, lexicon))