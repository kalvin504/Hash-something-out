import time


# Create hash table linear probing
def hash_table(size):
    return [None] *size   # empty bucket 

# Hash function full quote
def hash_function(key, size):
    return hash(key) % size #use entire string for hash
def hash_function_2(key, size):
    return 1 + (hash(key[::-1]) % (size - 1)) #reverse string

# Insert using linear probing
def insert(table, key, value, collisions):
    size = len(table)
    index = hash_function(key, size)
    index2 = hash_function_2(key, size)
    start_index = index  # track starting position
    i = 0 #num of probes 

    while table[index] is not None: # collision moves forward
        collisions[0] += 1
        i += 1 
        index = (hash_function(key, size) + i * index2) % size
        if index == start_index: # table full
            print("Warning Hash table full", key)
            break
    if table[index] is None:  # insert if empty
        table[index] = value


# Count empty buckets (wasted space)
def wasted_space(table):
    count = 0
    for bucket in table:
        if bucket == None:
            count += 1
    return count



quotes = []

with open("MOCK_DATA.csv", "r", errors="ignore") as file:
    header = file.readline()  # skip header
    quote_index = header.strip().split(',').index("quote")  # find quote column

    for line in file:
        columns = line.strip().split(',')
        quote = columns[quote_index]   # extract quote
        quotes.append(quote)



size = int(len(quotes) * 1.5) # table size
quote_table = hash_table(size)
quote_collisions = [0]



start = time.time() #starts time

for quote in quotes:
    insert(quote_table, quote, quote, quote_collisions) #inserts quote into hash table 

end = time.time()  #end time



print("Attempt 5: Hash Table 2 Movie Quotes as key")
print("Collisions:", quote_collisions[0])
print("Wasted Space:", wasted_space(quote_table))
print("Construction Time:", end - start)
