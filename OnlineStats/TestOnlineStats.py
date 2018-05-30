# -*- coding: utf-8 -*-
# Name: Don Cruver
# Date: May 15, 2018
# Course: CPSC51100 - Statistical Programming, Lewis University
# Term: Summer 2018
# Assignment Name: Programming Assignment 1 – Descriptive Statistics

import unittest
from OnlineStats import OnlineStats

class TestOnlineStats(unittest.TestCase):
    def setUp(self):
        self.expected_means = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
        self.expected_variances = [0, 0.5, 1.0, 1.6666666666666665, 2.5, 3.5, 
                                   4.666666666666667, 6.0, 7.5, 9.166666666666666]
        self.x = 0

    def get_input(self):
        if (self.x == 10):
            self.x = -1
        else:
            self.x = self.x + 1
        
        return self.x

    def verify_output(self, mean, variance):
        self.assertEqual(mean, self.expected_means[self.x - 1])
        self.assertEqual(variance, self.expected_variances[self.x - 1])

    def test_streaming(self):
        OnlineStats().stream(self.get_input, self.verify_output)

if __name__ == '__main__':
        unittest.main()