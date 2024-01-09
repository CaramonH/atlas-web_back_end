#!/usr/bin/env python3

"""
2-hypermedia_pagination
"""


import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ init """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get the page of the dataset based on pagination"""
        assert isinstance(page, int) and page > 0, (
            "Page must be a positive integer"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be a positive integer"
        )
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start:end] if start < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Get hypermedia information for the dataset page """
        data_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_info = {
            'page_size': len(data_page),
            'page': page,
            'data': data_page,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

        return hyper_info
