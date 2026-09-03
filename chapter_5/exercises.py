"""
EXERCISES: Which of these hash functions are consistent?

5.1:- f(x) = 1
      Returns “1” for all input

5.2:- f(x) = rand()
      Returns a random number every time

5.3:- f(x) = next_empty_slot()
      Returns the index of the next empty slot in the hash table

5.4:- f(x) = len(x)
      Uses the length of the string as the index

"""

"""
SOLUTIONS:-

5.1:- Not ideal, since its always 1, you can just make a list of items
and return 1 for them all, but it's consistent & valid.

5.2:- Random no for same input- not consistent, not valid

5.3:- Can change, coz it depends on the next empty slot. Again, not consistent.

5.4:- len(str) is constant, so it'll return same output for same input.
Hence consistent.
"""

"""
EXERCISES: Which of these hash functions would provide a good distribution? 
Assume a hash table size of 10 slots.

Options:
A: f(x) = 1 (Returns "1" for all input)
B: f(x) = len(x) (Uses string length)
C: f(x) = first character of the string
D: f(x) = prime number modulo sum

5.5:- A phonebook where the keys are names: Esther, Ben, Bob, and Dan.
5.6:- A mapping from battery size to power: A, AA, AAA, and AAAA.
5.7:- A mapping from book titles to authors: Maus, Fun Home, and Watchmen.
"""

"""
SOLUTIONS:-

5.5:- C & D. 
A is obviously terrible.
B is bad because Ben, Bob, and Dan all have a length of 3 
-> massive collision on slot 3. 
C gives E, B, B, D (only one collision). D maps them broadly.

5.6:- B & D.
C fails horribly here because every single key starts with "A" 
-> all map to the exact same slot. 
B is perfect since the lengths are exactly 1, 2, 3, and 4. 
D distributes well too.

5.7:- B, C, & D.
They all start with completely different letters (M, F, W) so C works great.
Their lengths are different enough that B works, 
and D is mathematically robust as usual.
"""