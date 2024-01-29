#!/usr/bin/env python3
"""
Generic utilities for github org client.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """access_nested_map test method, checks for expected result"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception_message):
        """checks if method raises the correct exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ TestGetJson class for utils.py """
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """check if the method returns the result as expected"""

        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get') as mock_get:
            mock_get.return_value = mock
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
