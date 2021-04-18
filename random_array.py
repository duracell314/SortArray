print("Welcome to array sort program");

import array as arr
import random
import datetime
import csv
array_min = 10
array_max = 10000
# with open('time_sort.csv') as csvfile:
#      fieldnames = ['first_name', 'last_name']
#      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#      writer.writeheader()
#      writer.writerow(2)

#f = open('time_sort.csv', 'wt')
#myWriter = csv.writer(f)





length = [5, 10, 15, 50, 100, 200, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 13000, 15000, 20000]
#length = [5, 10, 15, 50, 100, 200, 1000, 2000, 3000, 4000, 5000, 6000, 8000]
#length = [5, 10, 15, 50, 60, 70, 80, 90, 100]
#with open('time_sort.csv', 'w', encoding='utf-8', newline='') as csvfile:
    #writer = csv.writer(csvfile)
    #writer.writerow(length)
times_elapsed = [0 for i in range(len(length))]        

for k in range(len(length)):
    array_length = length[k]
    third_array = [0 for i in range(array_length)]   
    
    #first_array = [0 for i in range(array_length)]
    #negative_array = [0 for i in range(array_length)]
    
    
    #print ("We define an array of", array_length, "random number picked from", array_min, "to", array_max)
    
    start_time = datetime.datetime.now()
    for i in range(array_length):
        # first_array[i] = random.randint(array_min, array_max)
        # negative_array[i] = random.randrange((array_max * -1), (array_min * -1))
        third_array[i] = random.randrange((array_max * -1), array_max)
    
                    
    #print(first_array)
    #print(negative_array)
    #print(third_array)
    
    #Now we start sorting the first ARRAY
    # for j in range(array_length):
    #     dummy_max = first_array[j];
    #     for i in range(array_length):
    #          if first_array[i] > dummy_max:
    #              dummy_max = first_array[i] 
    #              first_array[i] = first_array[j]
    #              first_array[j] = dummy_max
    
    # for j in range(array_length):
    #     dummy_max = negative_array[j];
    #     for i in range(array_length):
    #          if negative_array[i] > dummy_max:
    #              dummy_max = negative_array[i] 
    #              negative_array[i] = negative_array[j]
    #              negative_array[j] = dummy_max
    
    for j in range(array_length):
        dummy_max = third_array[j];
        for i in range(array_length):
             if third_array[i] > dummy_max:
                 dummy_max = third_array[i] 
                 third_array[i] = third_array[j]
                 third_array[j] = dummy_max
                 
    end_time = datetime.datetime.now()
    print("We have sorted the array")
    print("Arrays length", array_length)   
    time_elapsed = (end_time - start_time)
    print("Time elapsed",time_elapsed) 
    times_elapsed[k] = time_elapsed.microseconds + time_elapsed.seconds * 1000000
with open('time_sort.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(times_elapsed)
with open('time_sort.csv', 'a', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(length)          