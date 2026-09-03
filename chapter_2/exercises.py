# Exercises from Chapter 2

"""
Ex 2.1: Suppose you’re building an app to keep track of your finances.

Every day, you write down everything you spent money on. At the
end of the month, you review your expenses and sum up how much
you spent. So, you have lots of inserts and a few reads. Should you
use an array or a list?
"""

"""
Solution:-

We'll use a Linked List here, coz >> insertions & << reads
"""

"""
Ex 2.2: Suppose you’re building an app for restaurants to take customer
orders. Your app needs to store a list of orders. Servers keep adding
orders to this list, and chefs take orders off the list and make them.

It’s an order queue: servers add orders to the back of the queue, and
the chef takes the first order off the queue and cooks it.
Would you use an array or a linked list to implement this queue?
(Hint: Linked lists are good for inserts/deletes, and arrays are good
for random access. Which one are you going to be doing here?)
"""

"""
Sol:-
I'll use Lists here, coz lots of insertions, at the end, and then items being
accessed from top of lists/head and deleted- by chef- Lists are an optimal
choice of Data Structure here.
"""

"""
Ex 2.3: 
Let’s run a thought experiment. Suppose Facebook keeps a list of
usernames. When someone tries to log in to Facebook, a search is
done for their username. If their name is in the list of usernames,
they can log in. People log in to Facebook pretty often, so there are
a lot of searches through this list of usernames. Suppose Facebook
uses binary search to search the list. Binary search needs random
access—you need to be able to get to the middle of the list of
usernames instantly. Knowing this, would you implement the list
as an array or a linked list?
"""

"""
Sol:-
Of course, knowing that a username search on Fb implements binary search, which
in turn needs random access of the elements, I'd use Arrays here. Especially since
once a person creates a profile & username there, they repeatedly login to access it
-> multiple accesses needed.
"""

"""
Ex 2.4: People sign up for Facebook pretty often, too. Suppose you decided
to use an array to store the list of users. What are the downsides
of an array for inserts? In particular, suppose you’re using binary
search to search for logins. What happens when you add new users
to an array?
"""

"""
Sol:-
As I stated in in response to previous problem, I'd use Arrays as the Data Structure
here. 

There're multiple downsides to having an array for inserts:-
1. Whenever a new username is added/ someone new signs up, first we'll need to 
find the position of where they'd be- binary search- sorted only

2. Then, we'll need to shift all the usernames afterwards by 1 place to the right

3. Also, we'll need to find a new place for the array in the memory, if the next
contiguous place is not empty.
"""

"""
Problem 2.5:
In reality, Facebook uses neither an array nor a linked list to store
user information. Let’s consider a hybrid data structure: an array
of linked lists. You have an array with 26 slots. Each slot points to a
linked list. For example, the first slot in the array points to a linked
list containing all the usernames starting with a. The second slot
points to a linked list containing all the usernames starting with b,
and so on.

Suppose Adit B signs up for Facebook, and you want to add them
to the list. You go to slot 1 in the array, go to the linked list for slot
1, and add Adit B at the end. Now, suppose you want to search for
Zakhir H. You go to slot 26, which points to a linked list of all the
Z names. Then you search through that list to find Zakhir H.

Compare this hybrid data structure to arrays and linked lists. Is it
slower or faster than each for searching and inserting? You don’t
have to give Big O run times, just whether the new data structure
would be faster or slower.
"""

"""
Solution:-

1. This hybrid data structure would be faster than arrays, and slower than Linked Lists
for inserting a new username/item.

2. Likewise, it'll be faster than Linked Lists, and slower than arrays, for
accessing a username.
"""