# Quick Sort Algorithm

def quick_sort(nums):
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [num for num in nums[1:] if num <= pivot]
        more = [num for num in nums[1:] if num > pivot]

        return quick_sort(less) + [pivot] + quick_sort(more)

print(quick_sort([3,5,1,-1,0,2,99,22]))