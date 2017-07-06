#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import nltk
import pickle



def tokenize(job_description):
    """
    This function takes a job description and returns a list of tokens
    Parameters
    ----------
    job_description : str
        The text of the job description
    Returns
    ----------
    list[str]
        The list of tokens in the job description
    """
    return nltk.tokenize.regexp_tokenize(job_description, r'[$£€¥][\d,\.]+|\w+|[^\w\s]', gaps=False)


__all__ = ['tokenize']