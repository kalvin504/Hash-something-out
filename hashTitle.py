import time


#creates hash table with size buckets 
#each bucket is a list
def hash_table(size):
    return [[] for _ in range(size)]  

# New hash function for Attempt 2 use title length
def hash_function(key, size):
    return len(key) % size #length of title 

# Insert a key value pair into the hash table
def insert(table, key, value, collisions):
    index = hash_function(key, len(table)) # compute bucket index
    for item in table[index]:  # loop through bucket to count collisions
        collisions[0] += 1 
    table[index].append(value) # add value to bucket

#Counts empty buckets (wasted space)
def wasted_space(table):
    count = 0
    for bucket in table:
        if len(bucket) == 0:
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




print("Attempt 2 - Movie Title as Key Hash Table")
print("Collisions:", title_collisions[0])
print("Wasted Space:", wasted_space(title_table))
print("Construction Time:", end - start)
