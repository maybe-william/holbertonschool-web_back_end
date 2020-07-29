#!/usr/bin/env python3
""" pagination """


def index_range(page, page_size):
    """ get the start and end range for two numbers """
    return ((page-1) * page_size, page * page_size)
