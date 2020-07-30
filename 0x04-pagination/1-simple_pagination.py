#!/usr/bin/env python3
""" pagination """


from typing import Tuple
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        """ get a page of data """
        if not type(page) is int or not type(page_size) is int:
            raise AssertionError
        if page <= 0 or page_size <= 0:
            raise AssertionError

        data_range = index_range(page, page_size)
        data = self.dataset()
        return data[data_range[0]:data_range[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ get the start and end range for two numbers """
    return ((page-1) * page_size, page * page_size)
