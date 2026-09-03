def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            count +=1
            return mid,count
        elif nums[mid] > target:
            high = mid - 1
            count += 1
        elif nums[mid] < target:
            low = mid + 1
            count += 1
    return None

# Exercises

# Ques 1.1

list_128 = list(range(128))
mid, count = binary_search(list_128, list_128[-1])

print(f"""The maximum no of steps it would take to iterate a sorted list/array 
of 128 elements is {count}.""")

# Ques 1.2

list_256 = list(range(256))
mid, count = binary_search(list_256, list_256[-1])

print(f"""\nThe maximum no of steps it would take to iterate a sorted list/array 
of 256 elements is {count}.""")