import string

def check_password(criteria, n, password):

    if criteria == "lower":

        count = sum(1 for char in password if char.islower())

        return count >= n

    elif criteria == "special":

        special_characters = set(string.punctuation)

        count = sum(1 for char in password if char in special_characters)

        return count >= n

    else:

        return False

print(check_password("lower", 4, "aelxis15494=))àçza") and check_password("special", 2, "aelxis15494=))àçza"))