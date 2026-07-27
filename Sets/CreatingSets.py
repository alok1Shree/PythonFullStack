# ============================================================
# WAYS TO CREATE A SET
# ============================================================

# Method 1: Curly brackets with values
skills = {"Python", "Java", "MySQL", "Flask", "React"}
print(skills)          # {'Python', 'Java', 'MySQL', 'Flask', 'React'}
print(type(skills))    # <class 'set'>

# Method 2: From a list (removes duplicates automatically!)
marks_list = [88, 92, 78, 92, 65, 88, 78, 95]
unique_marks = set(marks_list)
print("Original list:", marks_list)
print("Unique marks :", unique_marks)   # {65, 78, 88, 92, 95}

# Method 3: From a string (unique characters)
letters = set("hello world")
print("Unique chars:", letters)   # {' ', 'd', 'e', 'h', 'l', 'o', 'r', 'w'}

# Method 4: From a tuple
courses = set(("Python", "Java", "Python", "MySQL"))
print("Unique courses:", courses)

# Method 5: Empty set — MUST use set(), NOT {}
empty_set  = set()       # ✅ correct — empty set
empty_dict = {}          # ❌ this is an empty DICT, not set!
print(type(empty_set))   # <class 'set'>
print(type(empty_dict))  # <class 'dict'>   ← NOT a set!

# ── SETS AUTOMATICALLY REMOVE DUPLICATES ─────────────────────
roll_calls = ["Aman", "Riya", "Aman", "Zoya", "Riya", "Aman", "Kabir"]
print("\nRoll calls (with repeats):", roll_calls)
print("Unique attendees        :", set(roll_calls))

# ── SETS ARE UNORDERED — order changes each run ───────────────
nums = {5, 2, 8, 1, 9, 3}
print("\nSet (may print in any order):", nums)
# Output varies: {1, 2, 3, 5, 8, 9} or any other order
# NEVER rely on set order!

# ── VALID AND INVALID SET ITEMS ──────────────────────────────
# Set items MUST be hashable (immutable)
valid_set = {1, "hello", (1, 2), 3.14, True}   # ✅ all hashable

try:
    invalid = {1, 2, [3, 4]}   # ❌ list is not hashable
except TypeError as e:
    print(f"❌ Cannot add list to set: {e}")

try:
    invalid = {1, 2, {"a": 1}} # ❌ dict is not hashable
except TypeError as e:
    print(f"❌ Cannot add dict to set: {e}")