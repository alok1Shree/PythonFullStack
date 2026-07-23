# ============================================================
# REAL-WORLD USE CASES FOR TUPLES
# ============================================================

# ── USE CASE 1: Student Record System ────────────────────────
print("==== STUDENT RECORDS ====")

# Each record is a tuple — fixed, read-only once created
student_records = [
    ("STU001", "Aman Kumar",   "Python Full Stack", 88.5, "2023-06-01"),
    ("STU002", "Riya Sharma",  "Java Full Stack",   92.0, "2023-06-01"),
    ("STU003", "Zoya Patel",   "Python Full Stack", 76.5, "2023-06-02"),
    ("STU004", "Kabir Singh",  "Data Science",      95.0, "2023-06-01"),
    ("STU005", "Meera Das",    "Python Full Stack", 60.0, "2023-06-03"),
]

# Header
print(f"{'ID':<10} {'Name':<18} {'Course':<22} {'Marks':>6} {'Grade':>6}")
print("─" * 68)

for sid, name, course, marks, date in student_records:   # unpacking
    grade = "A" if marks >= 90 else "B" if marks >= 75 else "C"
    print(f"{sid:<10} {name:<18} {course:<22} {marks:>6.1f} {grade:>6}")

# ── USE CASE 2: GPS Location System ──────────────────────────
print("\n==== GPS LOCATIONS ====")

locations = {
    "ACTE Bengaluru":  (12.9716, 77.5946),
    "ACTE Chennai":    (13.0827, 80.2707),
    "ACTE Hyderabad":  (17.3850, 78.4867),
    "ACTE Mumbai":     (19.0760, 72.8777),
}

def calculate_distance(loc1, loc2):
    """Simple distance approximation"""
    lat_diff = abs(loc1[0] - loc2[0])
    lon_diff = abs(loc1[1] - loc2[1])
    return round((lat_diff + lon_diff) * 111, 2)   # rough km

bengaluru = locations["ACTE Bengaluru"]
for city, coords in locations.items():
    lat, lon = coords    # unpacking
    dist = calculate_distance(bengaluru, coords)
    print(f"  {city:<22} | Lat: {lat:8.4f} | Lon: {lon:8.4f} | Dist from BLR: {dist} km")

# ── USE CASE 3: RGB Colour Palette ───────────────────────────
print("\n==== BRAND COLOURS ====")

# RGB colors as tuples — never change
brand_colors = {
    "Primary Blue":   (30,  58,  138),   # #1E3A8A
    "Secondary Blue": (37,  99,  235),   # #2563EB
    "Sky Blue":       (96,  165, 250),   # #60A5FA
    "Amber":          (245, 158, 11),    # #F59E0B
    "White":          (255, 255, 255),
    "Dark Text":      (30,  41,  59),
}

for name, (r, g, b) in brand_colors.items():   # unpacking in loop
    hex_code = f"#{r:02X}{g:02X}{b:02X}"
    print(f"  {name:<18} | RGB({r:3d},{g:3d},{b:3d}) | {hex_code}")

# ── USE CASE 4: Database Records ─────────────────────────────
print("\n==== DATABASE QUERY RESULTS ====")

# When you fetch from a database — rows come as tuples (read-only)
db_results = [
    (1, "Aman",  "Engineering",  65000.0, True),
    (2, "Riya",  "Marketing",    55000.0, True),
    (3, "Zoya",  "HR",           50000.0, False),
    (4, "Kabir", "Engineering",  72000.0, True),
]

total_salary = 0
active_count = 0

print(f"{'ID':>4} {'Name':<8} {'Dept':<15} {'Salary':>10} {'Active':>8}")
print("─" * 50)

for emp_id, name, dept, salary, is_active in db_results:
    status = "✅" if is_active else "❌"
    print(f"{emp_id:>4} {name:<8} {dept:<15} ₹{salary:>9,.2f} {status:>8}")
    total_salary += salary
    if is_active:
        active_count += 1

print("─" * 50)
print(f"{'TOTAL':<28} ₹{total_salary:>9,.2f}")
print(f"Active employees: {active_count}/{len(db_results)}")

# ── USE CASE 5: Function Returning Multiple Values ────────────
print("\n==== FUNCTION WITH MULTIPLE RETURNS ====")

def analyse_marks(subject, marks_list):
    """Returns multiple values as a tuple"""
    highest = max(marks_list)
    lowest  = min(marks_list)
    average = sum(marks_list) / len(marks_list)
    passers = sum(1 for m in marks_list if m >= 40)
    return highest, lowest, round(average, 2), passers  # tuple

python_marks = [88, 92, 45, 78, 60, 95, 38, 72, 85, 55]
java_marks   = [75, 82, 90, 65, 78, 88, 70, 92, 55, 45]

for subject, marks in [("Python", python_marks), ("Java", java_marks)]:
    high, low, avg, pass_count = analyse_marks(subject, marks)
    print(f"  {subject}:")
    print(f"    Highest: {high} | Lowest: {low} | Average: {avg}")
    print(f"    Passed : {pass_count}/{len(marks)} students")