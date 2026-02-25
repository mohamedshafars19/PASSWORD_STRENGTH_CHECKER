# Password Strength Checker with Change Option (No Class)

# Step 1: Rules (tuple)
rules = (
    "Minimum 8 characters",
    "At least one uppercase letter",
    "At least one lowercase letter",
    "At least one digit",
    "At least one special character"
)

special_chars = set("!@#$%^&*()_+-=[]{}|;:',.<>?/")

print("Password Rules:")
for rule in rules:
    print("-", rule)

# Step 2: Loop until password becomes EXCELLENT
while True:
    password = input("\nEnter your password: ")

    # Step 3: Data structures
    password_chars = list(password)   # list
    conditions = {                    # dict
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "digit": False,
        "special": False
    }

    # Step 4: Check length
    if len(password) >= 8:
        conditions["length"] = True

    # Step 5: Check characters using loop
    for ch in password_chars:
        if ch.isupper():
            conditions["uppercase"] = True
        elif ch.islower():
            conditions["lowercase"] = True
        elif ch.isdigit():
            conditions["digit"] = True
        elif ch in special_chars:
            conditions["special"] = True

    # Step 6: Score calculation
    score = 0
    for value in conditions.values():
        if value:
            score += 1

    # Step 7: Strength decision
    if score <= 2:
        strength = "POOR ❌"
    elif score <= 4:
        strength = "GOOD ⚠️"
    else:
        strength = "EXCELLENT ✅"

    print("\nPassword Strength:", strength)

    # Step 8: Accept or force change
    if strength == "EXCELLENT ✅":
        print("🎉 Password accepted successfully!")
        break
    else:
        print("Please change your password to make it stronger.")