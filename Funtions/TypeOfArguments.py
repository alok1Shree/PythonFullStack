# ============================================================
# POSITIONAL: matched by POSITION — order matters!
# ============================================================

def register_student(name, course, batch):
    print(f"Registered: {name} | Course: {course} | Batch: {batch}")


# Correct — positional order
register_student("Aman",  "Python",  "Morning")  # ✅
register_student("Riya",  "Java",    "Evening")  # ✅

# Wrong order — different meaning, no error!
register_student("Morning", "Aman", "Python")    # ❌ wrong but no error
# → Registered: Morning | Course: Aman | Batch: Python

# ============================================================
# KEYWORD: pass by NAME — order does NOT matter
# ============================================================

# def register_student(name1, course1, batch1):
#      print(f"Registered: {name} | Course: {course} | Batch: {batch}")
#
#
# # Using keyword arguments — any order works
# register_student(course="Python", name="Aman",  batch="Morning")
# register_student(batch="Evening", course="Java", name="Riya")
#
# # Mix: positional FIRST, then keyword
# register_student("Zoya", batch="Weekend", course="MySQL")
# # ✅ Positional fills 'name', then keywords fill the rest

# ============================================================
# DEFAULT: value used when argument is NOT provided
# ============================================================

def create_account(name, account_type="Savings", interest=4.5):
    print(f"Account: {name} | Type: {account_type} | Interest: {interest}%")


# All provided
create_account("Aman",  "Current", 3.0)
# Using defaults
create_account("Riya")                      # both defaults used
create_account("Zoya",  "Fixed Deposit")    # only interest defaults
create_account("Kabir", interest=7.5)       # only account_type defaults

# OUTPUT:
# Account: Aman  | Type: Current       | Interest: 3.0%
# Account: Riya  | Type: Savings       | Interest: 4.5%
# Account: Zoya  | Type: Fixed Deposit | Interest: 4.5%
# Account: Kabir | Type: Savings       | Interest: 7.5%

# ── IMPORTANT RULE ─────────────────────────────────────────
# Default parameters MUST come AFTER non-default parameters

# def bad(name="Aman",  age):  pass   # ❌ SyntaxError
def good(age, name="Aman"):  pass   # ✅ correct