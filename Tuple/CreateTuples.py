# ============================================================
# WAYS TO CREATE A TUPLE
# ============================================================

# Method 1: With round brackets
student = ("Aman", 22, "Python", 88.5)
print(student)         # ('Aman', 22, 'Python', 88.5)
print(type(student))   # <class 'tuple'>

# Method 2: Without brackets (tuple packing)
coordinates = 10, 20, 30
print(coordinates)     # (10, 20, 30)
print(type(coordinates))  # <class 'tuple'>

# Method 3: Empty tuple
empty = ()
print(empty)           # ()
print(type(empty))     # <class 'tuple'>

# Method 4: Single element tuple — THE MOST COMMON MISTAKE
wrong  = (42)     # NOT a tuple — just a number in brackets
correct = (42,)   # tuple — notice the TRAILING COMMA
also_correct = 42,  # also a tuple

print(type(wrong))        # <class 'int'>    ← NOT tuple!
print(type(correct))      # <class 'tuple'>  ← correct
print(type(also_correct)) # <class 'tuple'>  ← correct

# Method 5: Using tuple() constructor
from_list  = tuple([1, 2, 3, 4])
from_str   = tuple("hello")
from_range = tuple(range(1, 6))

print(from_list)   # (1, 2, 3, 4)
print(from_str)    # ('h', 'e', 'l', 'l', 'o')
print(from_range)  # (1, 2, 3, 4, 5)

# Method 6: Mixed data types — tuples can hold anything
mixed = ("Aman", 25, True, 3.14, [1, 2, 3], {"key": "val"})
print(mixed)