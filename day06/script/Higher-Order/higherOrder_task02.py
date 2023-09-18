import string

def check_password(critere, n, password):
    try:
        if critere == "lower":
            compil = sum(1 for char in password if char.islower())
            return compil >= n
        elif critere == "special":
            special_characters = set(string.punctuation)
            compil = sum(1 for char in password if char in special_characters)
            return compil >= n
        else:
            raise ValueError("critère invalide. Please use 'lower' or 'special'.")
    except Exception as e:
        return f"Error: {str(e)}"

result1 = check_password("lower", 4, "aelxis15494=))àçza")
result2 = check_password("special", 2, "aelxis15494=))àçza")
result3 = check_password("invalid_critere", 2, "aelxis15494=))àçza")

print(result1)  # Output: True
print(result2)  # Output: True
print(result3)  # Output: Error: Invalid critere. Please use 'lower' or 'special'.
