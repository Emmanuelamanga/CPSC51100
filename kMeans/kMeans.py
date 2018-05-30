# -*- coding: utf-8 -*-
# Name: Don Cruver
# Date: May 15, 2018
# Course: CPSC51100 - Statistical Programming, Lewis University
# Term: Summer 2018
# Assignment Name: Programming Assignment 2 – k-Means Clustering

def average(l):
    """Accepts a numeric list and returns the average of the values in that list.
       The data structure used to store the groups is a list where each element
       of the list is a list of two values. The first inner-list value is the 
       mean of the second inner-list value which is a list of the group members.

       example:
          [[4, [2, 4, 6]], [6, [3, 6, 9]], [10, [12, 8, 10, 12, 8]]...]
       """
    return sum(l)/float(len(l))
     
def distance(p, q):
    """Accepts values and returns the distance between them.
       The distance is always a positive integer. """
    return abs(p - q)
    
def initialize(values, k):
    """Accepts a numeric list and the number of groups to be created.
       Initializes the module based on the supplied values."""
    if k < len(values):
        global groups
        groups = [ [x, [x]] for x in values[0:k] ]
        groups.sort()
        
        for value in values[k:len(values)]:
            group = find_best_group(value, groups)
            group[1].append(value)
             
def find_best_group(p, l):
    """Given a value and a list, this function does a binary search to
       locate and return the group with the nearest mean value."""
    if len(l) == 1:
        return l[0];
        
    midpoint = (len(l)-1) / 2;
    d1 = distance(p, l[midpoint][0])
    d2 = distance(p, l[midpoint + 1][0])
    
    if d1 < d2:
        return find_best_group(p, l[0:midpoint + 1])

    return find_best_group(p, l[midpoint + 1:len(l)])
    
def recalculate_centroids():
    """Recalculates the mean for each group."""
    for group in groups:
        group[0] = average(group[1])           
    
def rebalance():
    """Iterates over the values in each inner-most list to find the
       group that's the closest fit. Returns a boolean indicating whether
       any points were moved between groups."""
       
    recalculate_centroids()    
    point_moved = False
    
    for group in groups:
        mean = group[0]
        values = group[1]
    
        for value in values:
            new_group = find_best_group(value, groups)
            
            if new_group[0] != mean:
                point_moved = True
                values.remove(value)
                new_group[1].append(value)
    
    return point_moved

def groups():
    """Returns the current state of the groups."""
    return groups

def converge(output_fn=None):
    """Calls 'rebalance()' repeatedly until convergence is reached. Optionally
       accepts a function that will be pasdsed the current state of 'groups' 
       on each iteration."""
    while (rebalance()):
        if output_fn:
            output_fn(groups)        
        
if __name__ == "__main__":
    print "CPSC-51100, Summer 2018"
    print "NAME: Don Cruver"
    print "PROGRAMMING ASSIGNMENT #2"
