# ============================================================
# MODIFYING SETS
# ============================================================

enrolled_courses = {"Python", "MySQL", "HTML"}
print("Initial:", enrolled_courses)

# ── ADD: add ONE item ─────────────────────────────────────────
enrolled_courses.add("Flask")
print("\nAfter add('Flask'):", enrolled_courses)

enrolled_courses.add("Python")   # already exists — no error, no duplicate
print("After add('Python') again:", enrolled_courses)   # unchanged

# ── UPDATE: add MULTIPLE items at once ───────────────────────
enrolled_courses.update(["React", "JavaScript", "CSS"])
print("\nAfter update([...]):", enrolled_courses)

# update() accepts any iterable
enrolled_courses.update({"Django", "REST API"})
enrolled_courses.update(("Docker", "Git"))
print("After more updates:", enrolled_courses)

# ── REMOVE: removes item — ERROR if not found ─────────────────
enrolled_courses.remove("HTML")
print("\nAfter remove('HTML'):", enrolled_courses)

try:
    enrolled_courses.remove("Angular")   # ❌ KeyError — not found
except KeyError as e:
    print(f"❌ remove() error: {e}")

# ── DISCARD: removes item — NO error if not found ─────────────
enrolled_courses.discard("CSS")        # removes safely
enrolled_courses.discard("Angular")    # ✅ no error even if missing
print("\nAfter discard:", enrolled_courses)

# ── POP: removes and returns RANDOM item ─────────────────────
removed = enrolled_courses.pop()
print(f"\nPopped (random): {removed}")
print("After pop:", enrolled_courses)

# ── CLEAR: removes ALL items ──────────────────────────────────
temp_set = {1, 2, 3, 4, 5}
temp_set.clear()
print("\nAfter clear():", temp_set)     # set()

# ── len, in, not in ──────────────────────────────────────────
tech_skills = {"Python", "MySQL", "Flask", "React", "Docker"}
print("\nNumber of skills:", len(tech_skills))
print("'Python' in set  :", "Python" in tech_skills)    # True
print("'Angular' in set :", "Angular" in tech_skills)   # False
print("'Angular' not in :", "Angular" not in tech_skills) # True