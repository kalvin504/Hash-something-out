import time


# Create hash table linked list
def hash_table(size):
    return [[] for _ in range(size)]  # each bucket is a list

# Hash function use first word of the quote
def hash_function(key, size):
    return len(key.split()) %size

# Insert into linked list hash table
def insert(table, key, value, collisions):
    index = hash_function(key, len(table)) # find bucket
    for item in table[index]:  # count collisions
        collisions[0] += 1
    table[index].append(value) # insert into bucket

# Count empty buckets (wasted space)
def wasted_space(table):
    count = 0
    for bucket in table:
        if len(bucket) == 0:
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



print("Attempt 2: Hash Table 2 Movie Quotes as key")
print("Collisions:", quote_collisions[0])
print("Wasted Space:", wasted_space(quote_table))
print("Construction Time:", end - start)
