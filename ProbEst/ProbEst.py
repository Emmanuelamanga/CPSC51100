# -*- coding: utf-8 -*-
# Name: Don Cruver, Bill O'Keefe
# Date: Jun 9, 2018
# Course: CPSC51100 - Statistical Programming, Lewis University
# Term: Summer 2018
# Assignment Name: Programming Assignment 4 – Estimating Probabilities

from pandas import DataFrame

def p(df, key, value):
    return (df.loc[df[key].isin([value])]).index.size / float(df.index.size)

def read_instance():
    instance_list = raw_input("Enter the make,model,type,rating: ").split(",")
    return {'make':instance_list[0], 'model':instance_list[1], 'type':instance_list[2], 'rating':instance_list[3]}

def output_simple_probabilities(df, output_fn):
    for rating in sorted(set(df.rating)):
        p_rating = p(df, "rating", rating)
        output_fn("Prob(rating={}) = {:.6f}".format(rating, p_rating))

def output_conditional_probabilities(df, output_fn):
    for rating in sorted(set(df.rating)):
        dframe = df.loc[df.rating == rating]
        
        for car_type in sorted(set(df.type)):
            p_rating = p(dframe, 'type', car_type)
            print "Prob(type={}|rating={}) = {:.6f}".format(car_type, rating, p_rating)
        
def load(instances, input_fn):    
    df = DataFrame(columns=['make', 'model', 'type', 'rating'])

    for instance in range(instances):
        df = df.append(input_fn(), ignore_index=True)
        print
        
    return df
    
def print_to_console(x):
    print x

if __name__ == "__main__":
    print("CPSC-51100, Summer 2018")
    print("NAME: Don Cruver, Bill OKeefe")
    print( "PROGRAMMING ASSIGNMENT #3 \n")
    instances = int(raw_input("Enter the number of car instances: "))
    print
    df = load(instances, read_instance)
    print df
    print
    output_simple_probabilities(df, print_to_console)
    print
    output_conditional_probabilities(df, print_to_console)
    print
    