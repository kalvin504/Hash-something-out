import time


# Create a hash table with fixed size
def hash_table(size):
    return [None] * size  #empty

# Hash function 
#use entire title for better distribution
def hash_function(key, size):
    return hash(key) % size

# Insert using linear probing 
def insert(table, key, value, collisions, used_buckets):
    index = hash_function(key, len(table))
    start_index = index #remeber starting index
    while table[index] is not None:
        collisions[0] += 1  # count collision since bucket is already filled
        index = (index + 1) % len(table) # move to next bucket
        if index == start_index:
            print("Warning Hash table is full", key)
            break
    if table[index] == None:
        table[index] = value
        used_buckets.add(index)  # track used bucket

# Count wasted space by subtracting used buckets from table size
def wasted_space(table, used_buckets):
    return len(table) - len(used_buckets)

movies = []

with open("MOCK_DATA.csv", "r", errors="ignore") as file:
    header = file.readline()  # skip header
    title_index = header.strip().split(',').index("movie_title") # find index of title column
    for line in file:
        columns = line.strip().split(',') # split line by comma
        title = columns[title_index]
        movies.append(title) # add title to list


size = int(len(movies) * 1.3) # smaller table to reduce waste
title_table = hash_table(size) #creates hash table
title_collisions = [0]
used_buckets = set() # track which buckets are used

start = time.time()

for title in movies:
    insert(title_table, title, title, title_collisions, used_buckets) #inserts title into hash table 

end = time.time()




print("Attempt 4 - Movie Title as Key Hash Table")
print("Collisions:", title_collisions[0])
print("Wasted Space:", wasted_space(title_table, used_buckets))
print("Construction Time:", end - start)
