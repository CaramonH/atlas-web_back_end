#!/usr/bin/env python3

"""Annotate the function and return values with the appropriate types"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, each containing an element from the input list
       and its length"""
    return [(i, len(i)) for i in lst]
