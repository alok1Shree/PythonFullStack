# ============================================================
# PARAMETERS: names inside the function definition
# ARGUMENTS : actual values passed when calling
# ============================================================

def greeting(name, greeting):    # name, greeting = PARAMETERS
    print(f"{greeting}, {name}!")


greeting("Aman", "Good Morning")  # "Aman", "Good Morning" = ARGUMENTS
greeting("Riya", "Hello")
greeting("Zoya", "Welcome")

# SIMPLE RULE:
# Parameters = empty boxes (placeholder names)
# Arguments  = actual values put INTO those boxes