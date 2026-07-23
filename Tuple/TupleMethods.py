# ============================================================
# TUPLE METHODS — tuples only have 2 built-in methods
# (because they're immutable — no need for more)
# ============================================================

marks = (88, 92, 78, 92, 65, 92, 78)
    #     0   1   2   3   4   5   6

# ── count(value) — how many times a value appears ────────────
print("Count of 92:", marks.count(92))   # 3
print("Count of 78:", marks.count(78))   # 2
print("Count of 99:", marks.count(99))   # 0 (not found)

# ── index(value) — FIRST position of a value ─────────────────
print("First 92 at index:", marks.index(92))    # 1
print("First 78 at index:", marks.index(78))    # 2

# Search with start and end range index(value, startRange, endRange)
print("92 from index 2:", marks.index(92, 2))   # 3 (skips index 1)
print("78 from index 3:", marks.index(78, 3))   # 6

# ── OTHER USEFUL BUILT-IN FUNCTIONS ──────────────────────────
numbers = (40, 15, 70, 25, 60, 10, 90)

print("\nlen()     :", len(numbers))          # 7
print("max()     :", max(numbers))           # 90
print("min()     :", min(numbers))           # 10
print("sum()     :", sum(numbers))           # 310
print("sorted()  :", sorted(numbers))        # [10, 15, 25, 40, 60, 70, 90] ← list
print("sorted(↓) :", sorted(numbers, reverse=True))

# sorted() returns a LIST (not tuple) — convert if needed:
sorted_tuple = tuple(sorted(numbers))
print("as tuple  :", sorted_tuple)

# ── MEMBERSHIP TESTING ────────────────────────────────────────
fruits = ("apple", "mango", "banana", "orange")
print("\n'mango' in fruits  :", "mango" in fruits)    # True
print("'grape' in fruits  :", "grape" in fruits)     # False
print("'grape' not in    :", "grape" not in fruits)  # True

# ── CONCATENATION AND REPETITION ──────────────────────────────
t1 = (1, 2, 3)
t2 = (4, 5, 6)

combined  = t1 + t2          # creates NEW tuple
print("\nt1 + t2  :", combined)   # (1, 2, 3, 4, 5, 6)

repeated = t1 * 3            # creates NEW tuple
print("t1 * 3   :", repeated)    # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# ── TUPLE COMPARISON ─────────────────────────────────────────
print("\n(1,2,3) == (1,2,3):", (1,2,3) == (1,2,3))   # True
print("(1,2,3) == (1,2,4):", (1,2,3) == (1,2,4))    # False
print("(1,2) < (1,3)     :", (1,2) < (1,3))          # True (compares element by element)