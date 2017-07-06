#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import nltk
import pickle



def ngram_func(n):
    """
    This function creates an ngram extracting function with an appropriate name.
    Parameters
    ----------
    n : int
        the n of the ngrams to be produced
    Returns
    ----------
    Callable[str] -> list[str]
        the ngram generating function
    """
    assert n>1, 'n must be greater than 1'
    def fun(sentences):
        return ['-'.join(ngram) for sentence in sentences for ngram in nltk.ngrams(sentence, n)]
    if n == 2:
        fun.func_name = 'bigrams'
    elif n == 3:
        fun.func_name = 'trigrams'
    else:
        fun.func_name = 'n_{}_grams'.format(n)
    return fun


__all__ = ['ngram_func']