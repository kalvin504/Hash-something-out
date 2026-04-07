# Hash Something Out Assignment  
**Kalvin Kheang**  
**4/4/2026**

**Files:**  
- `hashTitle.py` — Hash Table 1: Movie Title as Key  
- `hashQuote.py` — Hash Table 2: Movie Quote as Key  
-  images folder — All 10 pictures.  
---

## Reflection

### Hash Table 1: Movie Title as Key
For my first attempt was to do a simple linked list with the hash function using the first letter of the movie title. I multiplied the number of buckets by 2 so it’ll reduce the collisions. This attempt was just a base and test to see how much collision and waste it would cause.
When running it, the collision was 9734709 and wasted space was 29953. The construction time was around ~0.41 seconds. This sets up the next attempt to try to optimize this.

In the second attempt, I tried to decrease the collision by changing the hash function to use the length of the title instead of only using the first letter. I still stuck with the linked list. I didn't alter the program much but I was only trying to see how much this change could do. The program ended up with the Collision being 3799504 and wasted space of 29901 with the construction time of around ~0.16 seconds. Looking at that, the collision went down by a lot but it was still very high. The wasted space barely changed but the constructed time decreased.

In Attempt 3, my approach was to switch to linear probing. For the hash function I only went for the first two letters to see how much collision it can cause and how fast it is. With linear probing, it moves forwards in the table until it finds an empty spot. It’ll be interesting to see what that can do with many collisions. For this attempt, the collision was ~1680331, wasted space was 15000, and the time was ~0.25 seconds. Switching from linked list to linear probing helped the collision go down with wasted space also decreasing. But with those, the construction time went up a bit.

For attempt 4, I now try to decrease the collision mor., I used all letters of the title for the hash function. I experimented with the table size to see if the wasted space would decrease. I found that multiplying it by 2 makes the collision at around 16061 and wasted space at 1500 but when I lowered it and multiplied by 1.3, the collision was ~ 44794 and wasted space was 4500. This attempt is my best optimization yet seeing how these numbers decreased by a lot from last attempt.

In attempt 5, I wanted to go back to the linked list to see if I could optimize it better. My approach was for the hash function to use the first and last letter while also using the length of the title. Then with the size, I kept it the same size as the number of movies. I ended up with the collision being ~48730 and wasted space being ~10060 and the construction time being ~0.008. This is a huge improvement from the last time I used linked lists in attempt 2.

Early attempts testing basic linked lists and simple hash functions resulted in high collisions and moderate wasted space, showing limited efficiency. Later attempts, especially with linear probing and more sophisticated hash functions, drastically reduced collisions and wasted space while speeding up construction. Attempt four was my best optimization in this hash table using titles. 




### Hash Table 2: Movie Quote as Key
In attempt 1 my first thought was to do something similar to my first attempt in the other hash table. I used linked lists and created a hash function system where it would cause collision and wasted space so I can see the main area to check. For the hash function I used the first word of the quote as there would be many of the same starting word in different quotes like “the”.  Collisions were ~677552, wasted space was 29358, and construction time was ~0.037 seconds. As for starting, it wasn’t too bad compared to hash table 1 attempt 1. 

For attempt 2, my approach was to stick with linked lists and again use how many words are in the quote for the hash function. My thought was most quotes won’t have the same length of word so it could distribute easier. The collision ended up being exactly 45891010 every time. The wasted space was 29993 and the constructed time was ~2 seconds. I found this very fascinating as the collision went up by a huge amount but the wasted space is not that high. The construction time was by far the longest I had and attempt 2 would make this the worst optimized attempt yet. 

For attempt 3 just like the last hash table, I switch to linear probing. For the hash function I used the last word of the quotes since compared to attempt 1 (where it uses the first word, which had a lot of repeats), I expected the last word of a quote would be in most cases different from each other. The collision was ~1288982, wasted space was 15000, and construction time was around ~0.16. I think it’s better to compare this attempt to attempt 1 instead of attempt 2. The only noticeable difference is that in attempt 3, the wasted space is a lot less but in attempt 1 the collision is less. 

In attempt 4, my main focus was to decrease the collision by a good bit and try to keep the wasted space like in attempt 3. Still with linear probing, for the hash function I used the entire string using the whole quote. I ended with the collision being ~35969, wasted space 15000, construction time ~0.009 seconds. This was a big improvement and my fastest construction time out of all attempts. The collision decreased by a lot without changing the wasted space. 

In my 5th attempt, I wanted to try to use two hash functions. The two hash functions with linear probing can improve collision handling and avoid clustering. I implement this by giving the hash functions two different individual keys for probing. For the first hash function, I stuck with using the entire string. For the second hash function, I reversed the string. I also went and changed the size of the table. First my experiment was to multiply the size by a high number like 2.5. My second experiment was to multiply with a smaller number like 0.9. I found out that if the table size is too small, many keys collide and slow construction. If the table size is too large, you waste memory. So I went to the middle ground and multiplied the size by 1.5. The collision was around ~28916, wasted space was 7503, and construction time was ~0.01. This makes for one of my best attempts. 

Overall, the early attempts using simpler hash functions and linked lists that led to high collisions or slow construction times was very interesting to see. Switching to linear probing and better hash functions significantly improved performance. By the final attempts, optimizing both the hash functions and table size resulted in much lower collisions, reduced wasted space, and faster construction, making attempt 4 and 5 the most efficient.


