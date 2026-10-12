def halvings(n):
    if n == 1:
        return 0
    return 1 + halvings(n // 2)

print(halvings(8))      # 3   (8 → 4 → 2 → 1)
print(halvings(16))     # 4
print(halvings(1024))   # 10
print(halvings(1))      # 0   (already at 1, no halving needed)