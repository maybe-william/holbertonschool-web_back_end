#!/usr/bin/env python3
""" Test the utils """


import requests
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
import utils
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
import client


class TestGithubOrgClient(unittest.TestCase):
    """ Test that json can be got """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        get_patch.return_value = expected
        """ Test the org of the client """
        x = GithubOrgClient(org)
        self.assertEqual(x.org, expected)
        get_patch.assert_called_once_with("https://api.github.com/orgs/"+org)

    def test_public_repos_url(self):
        """ test that _public_repos_url works """
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        to_mock = 'client.GithubOrgClient.org'
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("x")
            self.assertEqual(cli._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """ test the public repos """
        jeff = {"name": "Jeff", "license": {"key": "a"}}
        bobb = {"name": "Bobb", "license": {"key": "b"}}
        to_mock = 'client.GithubOrgClient._public_repos_url'
        get_json_mock.return_value = [jeff, bobb]
        with patch(to_mock, PropertyMock(return_value="www.yes.com")):
            x = GithubOrgClient("x")
            self.assertEqual(x.public_repos(), ['Jeff', 'Bobb'])
            self.assertEqual(x.public_repos("a"), ['Jeff'])
            self.assertEqual(x.public_repos("c"), [])
            get_json_mock.assert_called_once_with("www.yes.com")
