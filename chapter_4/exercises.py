# Chapter 4 Exercises

# Ex 4.1: Write out the code for the earlier sum function

def sum(nums):
    if not nums:
        return 0
    if len(nums) < 2:
        return nums[0]
    return nums[0] + sum(nums[1:])

print(sum(range(1,6)))

# Ex 4.2: Write a recursive function to count the number of items in a list.

def count(nums):
    if len(nums) < 2:
        return 1
    return 1 + count(nums[1:])

print(count(range(10)))

# Ex 4.3: Can you come up with the base case and recursive case for binary search?

# We pass low and high pointers so we don't have to slice the array
def binary_search(nums, target, low=0, high=None):
    if high is None:
        high = len(nums) - 1
        
    if low > high:
        return None
        
    mid = (low + high) // 2
    
    if nums[mid] == target:
        return mid
    
    elif nums[mid] > target:
        return binary_search(nums, target, low, mid - 1)
    
    else:
        return binary_search(nums, target, mid + 1, high)

print(binary_search(list(range(100)), 48))

"""
MORE EXERCISES: How long would each of these operations take in Big O notation?

4.5: Printing the value of each element in an array.

4.6: Doubling the value of each element in an array.

4.7: Doubling the value of just the first element in an array.

4.8: Creating a multiplication table with all the elements in the array. So
if your array is [2, 3, 7, 8, 10], you first multiply every element by 2,
then multiply every element by 3, then by 7, and so on.
"""

items = [2, 3, 7, 8, 10]

# Solution 4.5

for item in items:
    print(item)

# It will take O(n) time- depends on the no of items in the array.

# Solution 4.6

items_doubled = [item * 2 for item in items]
# Once again, for loop, each item in list is accessed- O(n) time

# Solution 4.7

items_1 = items[:]
items_1[0] = 2 * items[0]
print(items_1)

# Just 1 element is changed, access time is 0(1).

# Solution 4.8

print()
for i in range(len(items)):
    for j in range(len(items)):
        print(f"{items[i]} * {items[j]} = {items[i] * items[j]}")
    print()

# Two for loops- each loop going through all the  item in the items_arr
# O(n**2)