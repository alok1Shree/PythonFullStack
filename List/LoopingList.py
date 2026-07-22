marks = [45, 78, 90, 33, 67]

for m in marks:
    status = "Pass" if m >= 40 else "Fail"
    print(f"{m} -> {status}")

# with index, when you need position too
for i, m in enumerate(marks):
    print(f"Student {i+1}: {m}")