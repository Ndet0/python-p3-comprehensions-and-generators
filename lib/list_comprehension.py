#!/usr/bin/env python3

def return_evens(num_list):
    """Return a list of even numbers from num_list.

    Accepts any iterable of integers (e.g., list, range) and returns a list
    containing only the even values in the same order.
    """
    return [n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):
    """Append an exclamation mark to each sentence in sentence_list.

    Returns a new list where each string from sentence_list has '!' appended.
    """
    return [s + '!' for s in sentence_list]