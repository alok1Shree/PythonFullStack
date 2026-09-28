# =====================================================================
# REAL-WORLD EXAMPLE: AIRLINE REWARD MEMBER SYSTEM
# =====================================================================

# 1. Creating the Dictionary (Key: Member ID -> Value: Profile Data)
# Notice how the value can contain lists, tuples, and strings!
frequent_flyer_db = {
    "FF-9021": {
        "name": "Alice Smith",
        "tier": "Platinum",
        "miles_balance": 75000,
        "recent_flights": ["AA-240", "AA-112"]
    },
    "FF-4412": {
        "name": "Bob Jones",
        "tier": "Bronze",
        "miles_balance": 12500,
        "recent_flights": ["AA-240"]
    }
}

print("💳 Reward Database Initialized.")


# 2. Lightning-Fast Lookup (Accessing Data)
# When a customer scans their membership card at the lounge
scanned_id = "FF-9021"

if scanned_id in frequent_flyer_db:
    passenger_profile = frequent_flyer_db[scanned_id]
    print(f"\n🔍 Lookup Success for ID {scanned_id}:")
    print(f"   Welcome back, {passenger_profile['name']}!")
    print(f"   Status Tier: {passenger_profile['tier']}")


# 3. Modifying and Updating Data (Mutability)
# Bob just flew a new route and earned 1,500 more miles
print(f"\n🔄 Updating account details for Bob (FF-4412)...")

# Modifying an existing value directly
frequent_flyer_db["FF-4412"]["miles_balance"] += 1500

# Appending a new flight to the nested list inside the dictionary
frequent_flyer_db["FF-4412"]["recent_flights"].append("AA-890")

print(f"   New Miles Balance: {frequent_flyer_db['FF-4412']['miles_balance']}")
print(f"   Updated History: {frequent_flyer_db['FF-4412']['recent_flights']}")


# 4. Adding a Brand New Record
new_member_id = "FF-7731"
frequent_flyer_db[new_member_id] = {
    "name": "Charlie Brown",
    "tier": "Silver",
    "miles_balance": 5000,
    "recent_flights": []
}

print(f"\n➕ New member added. Total registered members: {len(frequent_flyer_db)}")
