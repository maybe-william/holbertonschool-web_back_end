#!/usr/bin/env python3
""" pagination """


from typing import Tuple, List, Dict, Any
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

    def get_hyper(self,
                  page: int = 1,
                  page_size: int = 10) -> Dict[str, Any]:
        """ get hypermedia """
        if not type(page) is int or not type(page_size) is int:
            raise AssertionError
        if page <= 0 or page_size <= 0:
            raise AssertionError

        data_range = index_range(page, page_size)
        data = self.dataset()
        ret_data = data[data_range[0]:data_range[1]]

        d = {}
        d["page_size"] = len(ret_data)
        d["page"] = page
        d["data"] = ret_data

        prev = page - 1
        if prev <= 0:
            prev = None
        d["prev_page"] = prev
        if (len(data) % page_size == 0):
            d["total_pages"] = len(data) // page_size
        else:
            d["total_pages"] = (len(data) // page_size) + 1

        nex = page + 1
        if nex > d["total_pages"]:
            nex = None

        d["next_page"] = nex

        return d


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ get the start and end range for two numbers """
    return ((page-1) * page_size, page * page_size)
