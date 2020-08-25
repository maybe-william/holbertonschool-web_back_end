#!/usr/bin/env python3
""" Test the utils """


import requests
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ Test the nested map and access to it """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test the access to a nested map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map,
                                         path,
                                         expected):
        """ Test the access to a nested map """
        self.assertRaises(expected)


class TestGetJson(unittest.TestCase):
    """ Test that json can be got """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test the got json """
        result = Mock()
        result.json = Mock(return_value=test_payload)
        with patch('requests.get', return_value=result):
            self.assertEqual(get_json(test_url), test_payload)
            requests.get.assert_called_once_with(test_url)
