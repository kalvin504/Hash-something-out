import time


# Create a hash table with linked lists 
def create_table(size):
    table = []
    for _ in range(size):
        table.append([])  # empty 
    return table

# hash function combine first char, last char, and length using strings
def hash_function(key, size):
    if len(key) == 0:
        return 0
    
    # combine first char, last char, and length as a string, then hash
    combined = key[0] + key[-1] + str(len(key))
    return hash(combined) % size

# Insert key value pair into linked list table
def insert(table, key, value, collisions):
    index = hash_function(key, len(table))
    collisions[0] += len(table[index])  # count collisions 
    table[index].append(value) #add to linked list

# Count wasted space
def wasted_space(table):
    count = 0
    for bucket in table:
        if len(bucket) == 0:
            count += 1
    return count



movies = []

with open("MOCK_DATA.csv", "r", errors="ignore") as file:
    header = file.readline() # skip header
    title_index = header.strip().split(',').index("movie_title")
    for line in file:
        columns = line.strip().split(',') # split line by comma
        title = columns[title_index]
        movies.append(title) # add title to list



size = len(movies)  # keep table size same as number of movies
title_table = create_table(size) #creates hash table
title_collisions = [0] #collisions counter

start = time.time() #starts time

for title in movies:
    insert(title_table, title, title, title_collisions) #inserts title into hash table 

end = time.time() #end time



print("Attempt 5 - Movie Title as Key Hash Table")

print("Collisions:", title_collisions[0])
print("Wasted Space:", wasted_space(title_table))
print("Construction Time:", end - start)
