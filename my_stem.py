#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import nltk
import pickle

stemmer = pickle.load(open('my_stem.stemmer.pickle'))

def stem(tokens):
    """
    This function will stem all the tokens in a given list with the Snowball English stemmer.
    Parameters
    ----------
    tokens : list[str]
        the list of tokens to be stemmed
    Returns
    ----------
    list[str]
        the list of stems with the non-alphabetic words removed
    """
    return [stemmer.stem(t) for t in tokens if t.isalpha()]


__all__ = ['stem', 'stemmer']