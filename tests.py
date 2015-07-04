from comb import find_tokens
import unittest


class MyTest(unittest.TestCase):
    def test_simple(self):
        source = [
            {
                "file": "new_abboip.txt",
                "smartIns": ["!","true","false"],
                "smartInsVal": 1
            }
        ]

        expected = [[
            {
                "file": "new_abboip.txt",
                "smartIns": "true",
                "smartInsVal": 1
            },
            {
                "file": "new_abboip.txt",
                "smartIns": "false",
                "smartInsVal": 1
            }
        ]]

        res = find_tokens(source)
        self.assertListEqual(res, expected)