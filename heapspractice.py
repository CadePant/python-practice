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

PRIORITY = {"Critical": 1, "High": 2, "Medium": 3, "Low": 4}

tickets = [
    ("Low", "Change my email"),
    ("Critical", "Site is down"),
    ("Medium", "Refund not received"),
    ("High", "Can't log in"),
]

def next_tickets(tickets, k):
    heap = []
    for ticket in tickets:
        priority = PRIORITY[ticket[0]]
        heapq.heappush(heap, (priority,ticket[1]))
    result = []
    for i in range(k):
        variable = heapq.heappop(heap)
        result.append(variable[1])
    return result

print(next_tickets(tickets, 2))   # expected: ['Site is down', "Can't log in"]

print(k_smallest([8, 3, 10, 1, 6], 3))   # expected: [1, 3, 6]
print(k_smallest([5, 2, 9], 1))          # expected: [2]