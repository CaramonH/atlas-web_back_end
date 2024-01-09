#!/usr/bin/env python3

import csv
import math
from typing import List
"""
1-simple_pagination

Module for paginating a database of popular baby names.
"""

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ init """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
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
