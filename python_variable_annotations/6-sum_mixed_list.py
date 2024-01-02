#!/usr/bin/env python3

"""function sum_miced_list that takes mxd_list and returns their sum"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats and return the result
    """
    return sum(mxd_lst)
