def selection_sort(nums):
    for i in range(len(nums)):
        smallest = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
        nums[i],nums[smallest] = nums[smallest], nums[i]
    return nums

def merge(left,right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i != len(left):
        result.append(left[i])
        i+=1
    while j != len(right):
        result.append(right[j])
        j+=1
    return result

def merge_sort(nums):
    if len(nums) == 0 or len(nums) == 1:
        return nums
    mid = len(nums) //2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left,right)
print(selection_sort([29, 10, 14, 37, 13]))   # expected: [10, 13, 14, 29, 37] 
print(merge_sort([5, 1, 4, 2, 8]))     # expected: [1, 2, 4, 5, 8]
print(merge_sort([]))               