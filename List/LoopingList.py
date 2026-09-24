"""marks = [45, 78, 90, 33, 67]

for m in marks:
    status = "Pass" if m >= 40 else "Fail"
    print(f"{m} -> {status}")

# with index, when you need position too
for i, m in enumerate(marks):
    print(f"Student {i+1}: {m}")"""

a = ['apple', 'banana', 'cherry', 'mango']
for item in a:
    a = 'Vibhu'
    print(item)

print(a)  # The original list remains unchanged because we are modifying the loop variable, not the list itself.