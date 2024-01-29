#!/usr/bin/env python3
"""Test for the GithubOrgClient class"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
import client


class TestGithubOrgClient(unittest.TestCase):
    """ Test for the GithubOrgClient class"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test that checks if org returns the correct value."""

        github_org_client = GithubOrgClient(org_name)

        github_org_client.org()

        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')
