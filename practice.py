def most_common(types):
    counts = {}
    for t in types:
        if t in counts:
            counts[t] += 1
        else:
            counts[t] = 1
    best = None
    best_count = 0
    for key in counts:
        if counts[key] > best_count:
            best_count = counts[key]
            best = key
    return best

types = ["Refund", "Billing", "Refund", "Tech", "Billing", "Refund", "Tech"]
print(most_common(types))   # expected: Refund