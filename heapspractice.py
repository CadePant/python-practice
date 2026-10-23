import heapq

def k_smallest(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap,n)
    result = []
    for i in range(k):
        smallest = heapq.heappop(heap)
        result.append(smallest)
    return result

print(k_smallest([8, 3, 10, 1, 6], 3))   # expected: [1, 3, 6]
print(k_smallest([5, 2, 9], 1))          # expected: [2]