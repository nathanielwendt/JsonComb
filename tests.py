from comb import find_tokens
import unittest


class TestFindTokens(unittest.TestCase):
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

    def test_list(self):
        source = [
            "a",
            "b",
            ["!","a","b","c"]
        ]

        expected = [
            ["a","b","a"],
            ["a","b","b"],
            ["a","b","c"],
        ]

        res = find_tokens(source)
        self.assertListEqual(res, expected)

    def test_multiple_same_level(self):
        source = {
            "eval": "StdInsert",
            "dbName": "StdInsert",
            "numPoints": "20000",
            "file": "new_abboip.txt",
            "smartIns": ["!","true","false"],
            "smartInsVal": "1.0",
            "kdTree": "true",
            "type": ["!","StdTable","SQLiteRTree"],
            "dataType": "cabs",
        }

        expected = [{
            "eval": "StdInsert",
            "dbName": "StdInsert",
            "numPoints": "20000",
            "file": "new_abboip.txt",
            "smartIns": "true",
            "smartInsVal": "1.0",
            "kdTree": "true",
            "type": "StdTable",
            "dataType": "cabs"
        },{
            "eval": "StdInsert",
            "dbName": "StdInsert",
            "numPoints": "20000",
            "file": "new_abboip.txt",
            "smartIns": "true",
            "smartInsVal": "1.0",
            "kdTree": "true",
            "type": "SQLiteRTree",
            "dataType": "cabs"
        },{
            "eval": "StdInsert",
            "dbName": "StdInsert",
            "numPoints": "20000",
            "file": "new_abboip.txt",
            "smartIns": "false",
            "smartInsVal": "1.0",
            "kdTree": "true",
            "type": "StdTable",
            "dataType": "cabs"
        },{
            "eval": "StdInsert",
            "dbName": "StdInsert",
            "numPoints": "20000",
            "file": "new_abboip.txt",
            "smartIns": "false",
            "smartInsVal": "1.0",
            "kdTree": "true",
            "type": "SQLiteRTree",
            "dataType": "cabs"
        }]

        res = find_tokens(source)
        self.assertListEqual(res, expected)

    def test_nested(self):
        source = {
            "first": [
                "!",
                "a",
                "b",
                {
                    "1": "one",
                    "2": "two",
                    "3": ["!", "three", "threeve","peeve"]
                }
            ],
            "second": 2
        }

        expected = [
            {
                "first": "a",
                "second": 2
            },
            {
                "first": "b",
                "second": 2
            },
            {
                "first": [{
                    "1": "one",
                    "2": "two",
                    "3": "three"
                },
                {
                    "1": "one",
                    "2": "two",
                    "3": "threeve"
                },
                {
                    "1": "one",
                    "2": "two",
                    "3": "peeve"
                }],
                "second": 2
            },
        ]

        res = find_tokens(source)
        self.assertListEqual(res, expected)