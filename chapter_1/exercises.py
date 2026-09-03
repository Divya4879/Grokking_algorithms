# Chapter 1 Exercises: Big O Notation
# Give the run time for each of these scenarios in terms of Big O.

# Ques 1.3: You have a name, and you want to find the person's phone number in the phone book.
ans_1_3 = "O(log n) - Binary search can be used because the names in a phone book are sorted alphabetically."

# Ques 1.4: You have a phone number, and you want to find the person's name in the phone book.
ans_1_4 = "O(n) - Simple search is required because the phone book is not sorted by phone numbers, so you may have to search the whole book."

# Ques 1.5: You want to read the numbers of every person in the phone book.
ans_1_5 = "O(n) - You must visit every single element once."

# Ques 1.6: You want to read the numbers of just the As.
ans_1_6 = "O(n) - Even though it is a fraction of the book (1/26), constants are ignored in Big O notation."

print("Exercise 1.3:", ans_1_3)
print("Exercise 1.4:", ans_1_4)
print("Exercise 1.5:", ans_1_5)
print("Exercise 1.6:", ans_1_6)