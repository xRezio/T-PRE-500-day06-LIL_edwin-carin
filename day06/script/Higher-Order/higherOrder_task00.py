def funA(s, n):
    lowercase_count = sum(1 for char in s if char.islower())
    return lowercase_count >= n

s = input("lowercase check : ")
n = 3

if funA(s, n):
    print(f"'{s}' possède au moins {n} lowercase.")
else:
    print(f"'{s}' ne possède pas au moins  {n} lowercase.")

#############################################################

def funB(t, o):
    uppercase_count = sum(1 for char in t if char.isupper())
    return uppercase_count >= o

t = input("uppercase check : ")
o = 3

if funB(t, o):
    print(f"'{t}' possède au moins {o} uppercase.")
else:
    print(f"'{t}' ne possède pas au moins  {o} uppercase.")

#############################################################

def funC(s, n):
    return len(s) >= n

s = input("char length check : ")
n = 5

if funC(s, n):
    print(f"'{s}' possède au moins {n} characters.")
else:
    print(f"'{s}' ne possède pas au moins {n} characters.")

#############################################################

def funD(s, n):
    special_characters = set("!@#$%^&*ù()_-+=[]{}|;:'\",.<>?")
    special_count = sum(1 for char in s if char in special_characters)
    return special_count >= n

s = input("special char check : ")
n = 3

if funD(s, n):
    print(f"'{s}' possède au moins {n} special characters.")
else:
    print(f"'{s}' ne possède pas au moins {n} special characters.")

#############################################################

def funE(s, n):
    digit_count = sum(1 for char in s if char.isdigit())
    return digit_count >= n

s = input("number check : ")
n = 4

if funE(s, n):
    print(f"'{s}' possède au moins {n} numbers.")
else:
    print(f"'{s}' ne possède pas au moins {n} numbers.")
