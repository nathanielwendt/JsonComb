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