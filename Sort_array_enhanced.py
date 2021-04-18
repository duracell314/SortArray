#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 23:49:54 2021

@author: antoniovasile
"""
print("Welcome to array sort program");

import array as arr
import random
import datetime
import csv
#cazzodicane
def sort_array():
        for j in range(array_length):
            dummy_max = third_array[j];
            for i in range(j+1, array_length):
                if third_array[i] > dummy_max:
                    dummy_max = third_array[i] 
                    third_array[i] = third_array[j]
                    third_array[j] = dummy_max

def fill_random_array():
        for i in range(array_length):
            third_array[i] = random.randrange((array_max * -1), array_max)

array_min = 10
array_max = 100000


length = [5, 10, 15, 50, 100, 200, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 13000, 15000, 20000]
#length = [5, 10, 15, 50, 100, 200, 1000, 2000, 3000, 4000, 5000, 6000, 8000]
#length = [5, 10, 15, 20, 25]
times_elapsed = [0 for i in range(len(length))]        

for k in range(len(length)):
    array_length = length[k]
    third_array = [0 for i in range(array_length)]   

    fill_random_array()

    start_time = datetime.datetime.now()

#for i in range(j+1, array_length):
    #print(third_array)    
#Here we choose a second array algorithm    
    sort_array()
    
    end_time = datetime.datetime.now()
    print("We have sorted the array")
    #print(third_array)
    print("Arrays length", array_length)   
    time_elapsed = (end_time - start_time)
    print("Time elapsed",time_elapsed) 
    times_elapsed[k] = time_elapsed.microseconds + time_elapsed.seconds * 1000000
with open('time_sort_2.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(times_elapsed)
with open('time_sort_2.csv', 'a', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(length)          
print(times_elapsed)