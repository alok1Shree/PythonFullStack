# ============================================================
# REAL-WORLD USE CASES FOR SETS
# ============================================================

# ── USE CASE 1: Remove Duplicates from Student List ──────────
print("==== 1. REMOVING DUPLICATES ====")

registrations = [
    "Aman Kumar",  "Riya Sharma",  "Aman Kumar",
    "Zoya Patel",  "Riya Sharma",  "Kabir Singh",
    "Aman Kumar",  "Meera Das",    "Zoya Patel",
]

print(f"Total registrations : {len(registrations)}")
unique_students = set(registrations)
print(f"Unique students     : {len(unique_students)}")
print(f"Duplicates removed  : {len(registrations) - len(unique_students)}")
print(f"Student list        : {sorted(unique_students)}")

# ── USE CASE 2: Attendance Tracking ──────────────────────────
print("\n==== 2. ATTENDANCE TRACKING ====")

all_students = {"Aman", "Riya", "Zoya", "Kabir", "Meera",
                "Rahul", "Priya", "Arun"}

day1_present = {"Aman", "Riya", "Zoya", "Kabir", "Rahul"}
day2_present = {"Aman", "Meera", "Zoya", "Priya", "Riya"}
day3_present = {"Aman", "Riya", "Kabir", "Arun", "Zoya"}

# Absent students each day
day1_absent = all_students - day1_present
day2_absent = all_students - day2_present
day3_absent = all_students - day3_present

print(f"Day 1 Absent: {sorted(day1_absent)}")
print(f"Day 2 Absent: {sorted(day2_absent)}")
print(f"Day 3 Absent: {sorted(day3_absent)}")

# Students present ALL 3 days
perfect_attendance = day1_present & day2_present & day3_present
print(f"\nPerfect Attendance : {sorted(perfect_attendance)}")

# Students absent at least once
at_least_once_absent = all_students - perfect_attendance
print(f"Absent At Least Once: {sorted(at_least_once_absent)}")

# Students who came at least one day
attended_atleast_one = day1_present | day2_present | day3_present
print(f"Attended ≥1 day    : {sorted(attended_atleast_one)}")

# ── USE CASE 3: E-Commerce — Unique Visitors ─────────────────
print("\n==== 3. WEBSITE UNIQUE VISITORS ====")

monday_visitors    = {"u001","u002","u003","u004","u005","u006"}
tuesday_visitors   = {"u002","u004","u007","u008","u001","u009"}
wednesday_visitors = {"u001","u003","u007","u010","u011","u005"}

# Total unique visitors across all days
all_unique = monday_visitors | tuesday_visitors | wednesday_visitors
print(f"Monday    visitors: {len(monday_visitors)}")
print(f"Tuesday   visitors: {len(tuesday_visitors)}")
print(f"Wednesday visitors: {len(wednesday_visitors)}")
print(f"Total unique users: {len(all_unique)}")

# Loyal visitors (came all 3 days)
loyal = monday_visitors & tuesday_visitors & wednesday_visitors
print(f"Loyal (3 days)    : {loyal}")

# New visitors each day (not seen before)
new_tue = tuesday_visitors   - monday_visitors
new_wed = wednesday_visitors - (monday_visitors | tuesday_visitors)
print(f"New on Tuesday    : {new_tue}")
print(f"New on Wednesday  : {new_wed}")

# ── USE CASE 4: Tag System (Blog/Product) ────────────────────
print("\n==== 4. BLOG TAG MATCHING ====")

blog_posts = {
    "Python Basics":     {"python", "beginner", "programming", "tutorial"},
    "Flask REST API":    {"python", "flask", "api", "backend", "intermediate"},
    "React Tutorial":    {"javascript", "react", "frontend", "tutorial"},
    "MySQL Advanced":    {"database", "mysql", "sql", "advanced"},
    "Full Stack Guide":  {"python", "react", "flask", "mysql", "fullstack"},
}

user_interests = {"python", "flask", "backend"}

print(f"User is interested in: {user_interests}")
print("\nRecommended posts:")

recommendations = []
for post, tags in blog_posts.items():
    match_count = len(tags & user_interests)   # intersection size
    if match_count > 0:
        recommendations.append((match_count, post, tags & user_interests))

recommendations.sort(reverse=True)   # sort by match count

for count, post, matched_tags in recommendations:
    print(f"  [{count} match] {post:<25} | Matched: {matched_tags}")

# ── USE CASE 5: Permission System ────────────────────────────
print("\n==== 5. PERMISSION SYSTEM ====")

PERMISSIONS = {
    "student":  {"view_course", "submit_assignment", "view_marks"},
    "trainer":  {"view_course", "create_content", "view_marks",
                 "grade_assignment", "create_announcement"},
    "admin":    {"view_course", "create_content", "view_marks",
                 "grade_assignment", "create_announcement",
                 "manage_users", "view_reports", "system_config"},
}

def check_access(user_role, required_permission):
    perms = PERMISSIONS.get(user_role, set())
    if required_permission in perms:
        return f"✅ {user_role} can '{required_permission}'"
    else:
        return f"❌ {user_role} cannot '{required_permission}'"

def get_extra_perms(role1, role2):
    """What can role2 do that role1 cannot?"""
    return PERMISSIONS[role2] - PERMISSIONS[role1]

tests = [
    ("student",  "submit_assignment"),
    ("student",  "grade_assignment"),
    ("trainer",  "grade_assignment"),
    ("trainer",  "system_config"),
    ("admin",    "system_config"),
]

for role, perm in tests:
    print(f"  {check_access(role, perm)}")

print(f"\nExtra powers of trainer over student:")
extra = get_extra_perms("student", "trainer")
for p in sorted(extra):
    print(f"  + {p}")

print(f"\nExtra powers of admin over trainer:")
extra = get_extra_perms("trainer", "admin")
for p in sorted(extra):
    print(f"  + {p}")