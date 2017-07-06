#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pickle

english_lemmas = pickle.load(open('my_lemmatize.english_lemmas.pickle'))

def lemmatize(tokens, mapping):
    """
    This function takes tokens and returns the lemma of the word.
    Parameters
    ----------
    tokens : list[str]
        the list of tokens to be stemmed
    mapping : dict[str, str]
        the mapping from word to lemma
    Returns
    ----------
    list[str]
        for each token, either the lemma or the token
    """
    lemmas = []
    for token in tokens:
        if not token.isalpha():
            continue
        lowered_token = token.lower()
        lemmas.append(mapping.get(lowered_token, lowered_token))
    return lemmas


__all__ = ['lemmatize', 'english_lemmas']