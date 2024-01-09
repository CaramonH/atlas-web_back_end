#!/usr/bin/env python3

""" 0-simple_helper_function """


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of start and end indexes for a page and page size"""
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
