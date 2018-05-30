# -*- coding: utf-8 -*-
'''
Don Cruver
May 15, 2018
CPSC51100 - Statistical Programming, Lewis University
Summer 2018
Programming Assignment 1 – Descriptive Statistics
'''

class OnlineStats:
    """A class that implements running mean and running variance functions"""
    
    def __init__(self):
        self.mean = 0
        self.variance = 0
        self.n = 0
    
    # Accepts a statistic value, recalculates the running mean and variance
    # and returns those in a tuple: (mean, variance).
    def record_statistic(self, x):
        # Preserve the previous mean and variance to be
        # used in calculating current values
        previous_mean = self.mean
        previous_variance = self.variance
        
        # Update class members based on new statistic value
        self.n = self.n + 1
        self.mean = previous_mean + ((x - previous_mean) / float(self.n))
        
        if self.n > 1:
            self.variance = ((self.n - 2)/float((self.n - 1)) * 
                             previous_variance + (x - previous_mean)**2 / self.n)
            
        return(self.mean, self.variance)
        
    # This transformation function reads data from 'input_fn', passes those values
    # to an OnlineStats object and sends the resulting mean and variance 
    # values to 'output_fn'. 
    def stream(self, input_fn, output_fn):
        online_stats = OnlineStats()
        x = input_fn()
    
        while (x >= 0):
            stats = online_stats.record_statistic(x)
            output_fn(stats[0], stats[1])
            x = input_fn()

# Default input function for reading from console
def read_console_input():
    while True:
        try:
            x = float(raw_input("Enter a number: "))
            return x;
        except ValueError:
            print "Please enter numeric values only."

# Default output function for writing to console
def write_console_output(mean, variance):
    print "Mean is  {m:s}  variance is  {v:s}".format(
        m = str(mean), 
        v = str(variance))
    

if __name__ == "__main__":
    # Print heading info
    print "CPSC-51100, Summer 2018"
    print "NAME: Don Cruver"
    print "PROGRAMMING ASSIGNMENT #1"
    
    # Create an instance of the class and pass the default (console) input and
    # output functions to 'stream()'.
    OnlineStats().stream(read_console_input, write_console_output)
    