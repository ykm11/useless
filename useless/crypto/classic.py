import string

def caesar(s: str, rot_n: int=0):
    chars = string.ascii_lowercase
    
    s = s.lower()
    res = ""
    for ch in s:
        if ch not in chars:
            res += ch
        else:
            idx = chars.find(ch)
            res += chars[(idx+rot_n) % len(chars)]

    return res

def caesar_with_digits(s: str, rot_n: int=0):
    chars = string.ascii_lowercase + string.digits
    s = s.lower()
    res = ""
    for ch in s:
        if ch not in chars:
            res += ch
        else:
            idx = chars.find(ch)
            res += chars[(idx+rot_n) % len(chars)]

    return res

def caesar_full(s: str, rot_n: int=0):
    chars = string.printable
    res = ""
    for ch in s:
        if ch not in chars:
            res += ch
        else:
            idx = chars.find(ch)
            res += chars[(idx+rot_n) % len(chars)]

    return res

