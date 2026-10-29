def selection_sort(nums):
    for i in range(len(nums)):
        smallest = i
        for j in range(i + 1,len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums       
print(selection_sort([29, 10, 14, 37, 13]))   # expected: [10, 13, 14, 29, 37]
print(selection_sort([5, 1, 4]))              # expected: [1, 4, 5]