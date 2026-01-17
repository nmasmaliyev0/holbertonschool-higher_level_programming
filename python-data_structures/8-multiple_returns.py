#!/usr/bin/python3
def multiple_returns(sentence):
    first_letter = sentence[:1] or None

    return (len(sentence), first_letter)
