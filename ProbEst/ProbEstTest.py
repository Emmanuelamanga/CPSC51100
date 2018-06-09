# -*- coding: utf-8 -*-
# Name: Don Cruver, Bill O'Keefe
# Date: Jun 9, 2018
# Course: CPSC51100 - Statistical Programming, Lewis University
# Term: Summer 2018
# Assignment Name: Programming Assignment 4 – Estimating Probabilities

import unittest
import pandas as pd
from pandas import DataFrame

import ProbEst as est

class TestProbEst(unittest.TestCase):
    def setUp(self):
        self.i = 0
        
        self.data = ['ford,mustang,coupe,A',
                        'chevy,camaro,coupe,B',
                        'ford,fiesta,sedan,C',
                        'ford,focus,sedan,A',
                        'ford,taurus,sedan,B',
                        'toyota,camry,sedan,B']
                        
        self.df = DataFrame(
            columns=['make', 'model', 'type', 'rating'],
            data=[{'make': 'ford', 'model':'mustang', 'type':'coupe', 'rating':'A'},
                    {'make': 'chevy', 'model':'camaro', 'type':'coupe', 'rating':'B'},
                    {'make': 'ford', 'model':'fiesta', 'type':'sedan', 'rating':'C'},
                    {'make': 'ford', 'model':'focus', 'type':'sedan', 'rating':'A'},
                    {'make': 'ford', 'model':'taurus', 'type':'sedan', 'rating':'B'},
                    {'make': 'toyota', 'model':'camry', 'type':'sedan', 'rating':'B'}])
                        
    def test_p(self):
        self.assertEquals(est.p(self.df, 'rating', 'A'), 2/6.0)
        self.assertEquals(est.p(self.df, 'rating', 'B'), 3/6.0)
        self.assertEquals(est.p(self.df, 'rating', 'C'), 1/6.0)
        self.assertEquals(est.p(self.df.loc[self.df.rating=='A'], 'type', 'coupe'), 1/2.0)
        self.assertEquals(est.p(self.df.loc[self.df.rating=='A'], 'type', 'sedan'), 1/2.0)
        self.assertEquals(est.p(self.df.loc[self.df.rating=='B'], 'type', 'coupe'), 1/3.0)
        self.assertEquals(est.p(self.df.loc[self.df.rating=='B'], 'type', 'sedan'), 2/3.0)
        self.assertEquals(est.p(self.df.loc[self.df.rating=='C'], 'type', 'coupe'), 0)
        self.assertEquals(est.p(self.df.loc[self.df.rating=='C'], 'type', 'sedan'), 1.0)
    
    def mock_input_fn(self):
        rating_list = self.data[self.i].split(",")
        self.i = self.i + 1
        return {'make':rating_list[0], 'model':rating_list[1], 'type':rating_list[2], 'rating':rating_list[3]}
        
    def test_load(self):
        df = est.load(len(self.data), self.mock_input_fn)
        
if __name__ == '__main__':
        unittest.main()