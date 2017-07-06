#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import nltk
import pickle

from my_tokenize import *
from my_lemmatize import *
from my_stopword_removal import *

sent_detector = pickle.load(open('my_lemma_sentences.sent_detector.pickle'))

def lemma_sentences(job_description):
    """
    This function takes a job description and splits it into sentences
    Parameters
    ----------
    job_description : str
        The text of the job description
    Returns
    ----------
    list[str]
        the list of sentences
    """
    sentences = sent_detector.tokenize(job_description)
    return [stopword_removal(lemmatize(tokenize(sentence), english_lemmas)) for sentence in sentences]


__all__ = ['lemma_sentences', 'sent_detector']