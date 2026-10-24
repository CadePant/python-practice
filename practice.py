import heapq

def smallest_two(nums):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    return [first, second]

print(smallest_two([8, 3, 10, 1, 6]))  # expected: [1, 3]