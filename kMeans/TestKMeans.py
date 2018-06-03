# -*- coding: utf-8 -*-
# Name: Don Cruver
# Date: May 15, 2018
# Course: CPSC51100 - Statistical Programming, Lewis University
# Term: Summer 2018
# Assignment Name: Programming Assignment 2 – k-Means Clustering

import unittest
from kMeans import initialize, rebalance, converge, groups

class TestKMeans(unittest.TestCase):
    def setUp(self):
        self.test_groups = (1.8, 4.5, 1.1, 2.1, 9.8, 7.6, 11.32, 3.2, 0.5, 6.5)
        
    def test_k_means(self):
        initialize(self.test_groups, 3)
        self.assertEqual(groups(), [[1.1, [1.1, 0.5], 2], [1.8, [1.8, 2.1], 0], [4.5, [4.5, 9.8, 7.6, 11.32, 3.2, 6.5], 1]])
        self.assertEqual(rebalance(), True)
        converge(self.output_fn)
        print(groups)

    def output_fn(self, l):
        print(l)

if __name__ == '__main__':
        unittest.main()