def remainingwords(s):
    result = ""
    space_idx = s.find(" ")
    if space_idx != -1:
        result = s[space_idx + 1:]
    return result
