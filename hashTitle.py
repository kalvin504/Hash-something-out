import time


#creates hash table
def hash_table(size):
    return [None] * size  #empty

# Hash function first 2 letters
def hash_function(key, size):
    return hash(key[:2]) % size

# Insert using linear probing
def insert(table, key, value, collisions):
    index = hash_function(key, len(table))
    start_index = index #remeber starting index
    while table[index] is not None:
        collisions[0] += 1  # count collision since bucket is already filled
        index = (index + 1) % len(table) # move to next bucket
        if index == start_index:
            print("Warning Hash table is full", key)
            break
    else: # only insert if we found an empty spot
        table[index] = value #empty bucket then insert value

#Counts empty buckets (wasted space)
def wasted_space(table):
    count = 0
    for bucket in table:
        if bucket == None:
            count += 1
    return count



movies = []

with open("MOCK_DATA.csv", "r", errors="ignore") as file:
    header = file.readline()  # skip header
    title_index = header.strip().split(',').index("movie_title") # find index of title column
    for line in file:
        columns = line.strip().split(',') # split line by comma
        title = columns[title_index]
        movies.append(title) # add title to list



size = len(movies) * 2 #double the number of buckets to try to reduce collisions
title_table = hash_table(size) #creates hash table 
title_collisions = [0] #collisions counter

start = time.time() #starts time

for title in movies:
    insert(title_table, title, title, title_collisions) #inserts title into hash table 

end = time.time() #end time



print("Attempt 3 - Movie Title as Key Hash Table ")
print("Collisions:", title_collisions[0])
print("Wasted Space:", wasted_space(title_table))
print("Construction Time:", end - start)
