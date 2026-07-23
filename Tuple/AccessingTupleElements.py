# ============================================================
# INDEXING AND SLICING — same as strings and lists
# ============================================================

employee = ("Aman", "Developer", "Python", 65000, "Bengaluru")
#  index:    0        1             2        3        4
#  neg idx: -5       -4            -3       -2       -1

# ── POSITIVE INDEXING ─────────────────────────────────────────
print(employee[0])   # Aman
print(employee[1])   # Developer
print(employee[3])   # 65000

# ── NEGATIVE INDEXING ─────────────────────────────────────────
print(employee[-1])  # Bengaluru (last item)
print(employee[-2])  # 65000
print(employee[-5])  # Aman (same as index 0)

# ── SLICING: tuple[start:stop:step] ──────────────────────────
print(employee[1:3])   # ('Developer', 'Python')
print(employee[:3])    # ('Aman', 'Developer', 'Python')
print(employee[2:])    # ('Python', 65000, 'Bengaluru')
print(employee[::2])   # ('Aman', 'Python', 'Bengaluru') — every 2nd
print(employee[::-1])  # reverse the tuple

# ── NESTED TUPLE ─────────────────────────────────────────────
college_data = (
    "ACTE Institute",
    ("Python", "Java", "Full Stack"),   # nested tuple
    ("Bengaluru", "Chennai", "Hyderabad")
)

print(college_data[0])       # ACTE Institute
print(college_data[1])       # ('Python', 'Java', 'Full Stack')
print(college_data[1][0])    # Python    ← accessing nested item
print(college_data[2][1])    # Chennai

# ── LOOPING THROUGH TUPLE ─────────────────────────────────────
print("\n==== Employee Details ====")
labels = ["Name", "Role", "Skill", "Salary", "City"]
for label, value in zip(labels, employee):
    print(f"  {label:8} : {value}")