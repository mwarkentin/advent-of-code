#!/usr/bin/env python

import unittest

from p2 import parse_cmd


class TestParseCmd(unittest.TestCase):
    def test_valid_cmds(self):
        """
        Test a set of valid commands
        """
        cmds = ["up 1", "down 2", "forward 4"]

        self.assertEqual(parse_cmd(cmds[0]), ["aim", -1])
        self.assertEqual(parse_cmd(cmds[1]), ["aim", 2])
        self.assertEqual(parse_cmd(cmds[2]), ["forward", 4])


if __name__ == "__main__":
    unittest.main()
