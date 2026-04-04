import time


# Create hash table linear probing
def hash_table(size):
    return [None] *size   # empty bucket 

# Hash function use last word of the quote
def hash_function(key, size):
    words = key.split()
    if len(words) == 0:
        return 0
    return hash(words[-1]) % size


# Insert using linear probing
def insert(table, key, value, collisions):
    index = hash_function(key, len(table))
    start_index = index  # track starting position

    while table[index] is not None: # collision moves forward
        collisions[0] += 1
        index = (index + 1) % len(table) # next bucket
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



size = len(quotes) * 2 # table size
quote_table = hash_table(size)
quote_collisions = [0]



start = time.time() #starts time

for quote in quotes:
    insert(quote_table, quote, quote, quote_collisions) #inserts quote into hash table 

end = time.time()  #end time



print("Attempt 3: Hash Table 2 Movie Quotes as key")
print("Collisions:", quote_collisions[0])
print("Wasted Space:", wasted_space(quote_table))
print("Construction Time:", end - start)
