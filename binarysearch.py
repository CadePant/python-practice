def binary_search(nums,target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
    return -1


nums = [3, 8, 12, 17, 25, 31, 40]
print(binary_search(nums, 25))   # expected: 4
print(binary_search(nums, 3))    # expected: 0
print(binary_search(nums, 99))   # expected: -1