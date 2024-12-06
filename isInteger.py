def isInteger(user_string):
    blank = 0
    if len(user_string) == 0:
        return False
    for letter in user_string:
        if letter in " ":
            blank += 1
        else:
            break
    if len(user_string) == blank:
        return False
    user_string = user_string.strip()
    if user_string[0] in "+-":
        user_string = user_string[1:]
        if len(user_string) == 0:
            return False
    for letter in user_string:
        if letter not in  "1234567890":
            return False
    return True
    
print(isInteger("       "))
print(isInteger("  11  11"))
print(isInteger(""))
print(isInteger("  11-  "))
print(isInteger("11aa1  "))
print(isInteger("11111-  "))
print(isInteger(" 1+1111 "))
print(isInteger("  -+11111"))
print(isInteger("-11111  "))
print(isInteger("- 11111  "))
print(isInteger("  -five"))
print(isInteger("-"))