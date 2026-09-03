# Selection Sort Algorithm

def smallest_no(nums):
    min_num = nums[0]
    min_idx = 0
    for i in range(len(nums)):
        if nums[i] < min_num:
            min_num = nums[i]
            min_idx = i
    return min_idx


def selection_sort(nums):
    sorted_nums = []
    
    while nums:
        sorted_nums.append(nums.pop(smallest_no(nums)))
    return sorted_nums

sorted_arr = selection_sort([3,5,-1,2,200,45,8])
print(sorted_arr)