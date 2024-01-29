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
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception_message):
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


class TestMemoize(unittest.TestCase):
    """ TestMemoize class for utils.py """

    def test_memoize(self):
        """ Testing the memoize method to return expected"""

        class TestClass:
            """TestClass"""
            def __init__(self):
                """ init method"""
                self.call_count = 0

            def a_method(self):
                """ a_method method method method method"""
                self.call_count += 1
                return 42

            @memoize
            def a_property(self):
                """ a_property method
                Args:
                    self (TestClass): the class itself
                """
                return self.a_method()

        # create a mock object
        with patch.object(
                TestClass, 'a_method', return_value=42) as mocked_method:
            test_instance = TestClass()
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mocked_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
