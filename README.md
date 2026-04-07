# Hash Something Out Assignment  
**Kalvin Kheang**  
**4/4/2026**

**Files:**  
- `hashTitle.py` — Hash Table 1: Movie Title as Key  
- `hashQuote.py` — Hash Table 2: Movie Quote as Key  

---

## Reflection

### Hash Table 1: Movie Title as Key
For my first attempt was to do a simple linked list with the hash function using the first letter of the movie title. I multiplied the number of buckets by 2 so it’ll reduce the collisions. This attempt was just a base and test to see how much collision and waste it would cause.
When running it, the collision was 9734709 and wasted space was 29953. The construction time was around ~0.41 seconds. This sets up the next attempt to try to optimize this.

In the second attempt, I tried to decrease the collision by changing the hash function to use the length of the title instead of only using the first letter. I still stuck with the linked list. I didn't alter the program much but I was only trying to see how much this change could do. The program ended up with the Collision being 3799504 and wasted space of 29901 with the construction time of around ~0.16 seconds. Looking at that, the collision went down by a lot but it was still very high. The wasted space barely changed but the constructed time decreased.

In Attempt 3, my approach was to switch to linear probing. For the hash function I only went for the first two letters to see how much collision it can cause and how fast it is. With linear probing, it moves forwards in the table until it finds an empty spot. It’ll be interesting to see what that can do with many collisions. For this attempt, the collision was ~1680331, wasted space was 15000, and the time was ~0.25 seconds. Switching from linked list to linear probing helped the collision go down with wasted space also decreasing. But with those, the construction time went up a bit.

For attempt 4, I now try to decrease the collision mor., I used all letters of the title for the hash function. I experimented with the table size to see if the wasted space would decrease. I found that multiplying it by 2 makes the collision at around 16061 and wasted space at 1500 but when I lowered it and multiplied by 1.3, the collision was ~ 44794 and wasted space was 4500. This attempt is my best optimization yet seeing how these numbers decreased by a lot from last attempt.

In attempt 5, I wanted to go back to the linked list to see if I could optimize it better. My approach was for the hash function to use the first and last letter while also using the length of the title. Then with the size, I kept it the same size as the number of movies. I ended up with the collision being ~48730 and wasted space being ~10060 and the construction time being ~0.008. This is a huge improvement from the last time I used linked lists in attempt 2.

Overall. I think my Attempt 4 was the best optimization and I’ve noticed that my linear probing attempts work better than my linked list attempts.


### Hash Table 2: Movie Quote as Key
...
