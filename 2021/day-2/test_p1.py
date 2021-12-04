#!/usr/bin/env python

import unittest

from p1 import parse_cmd


class TestParseCmd(unittest.TestCase):
    def test_valid_cmds(self):
        """
        Test a set of valid commands
        """
        cmds = ["up 1", "down 2", "backward 3", "forward 4"]

        self.assertEqual(parse_cmd(cmds[0]), ["depth", -1])
        self.assertEqual(parse_cmd(cmds[1]), ["depth", 2])
        self.assertEqual(parse_cmd(cmds[2]), ["horizontal", -3])
        self.assertEqual(parse_cmd(cmds[3]), ["horizontal", 4])


if __name__ == "__main__":
    unittest.main()
