#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pickle

custom_stopwords = pickle.load(open('my_stopword_removal.custom_stopwords.pickle'))

def stopword_removal(terms):
    """
    This function removes stop words from a list of terms
    Parameters
    ----------
    terms : list[str]
        a list of terms from which to remove stop words
    Returns
    ----------
    list[str]
        a list of terms with the stop words removed
    """
    return [s for s in terms if s not in custom_stopwords]


__all__ = ['stopword_removal', 'custom_stopwords']