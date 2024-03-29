#!/usr/bin/env python3
"""
3-hypermedia_del_pagination

Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Get hypermedia information for the indexes dataset page """
        assert index is None or (isinstance(index, int) and 0 <= index < len(self.__indexed_dataset)), "Invalid index"
        assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be positive integer"
        )
        next_index = index + page_size
        data_page = [self.__indexed_dataset[i] for i in range(index, next_index) if i in self.__indexed_dataset]

        hyper_info = {
            'index': index,
            'page_size': page_size,
            'data': data_page,
            'next_index': next_index if data_page else None,
        }

        return hyper_info
