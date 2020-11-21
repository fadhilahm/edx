def firstword(s):
    # find the index of space char
    space_idx = s.find(" ")
    if space_idx != -1:
        return s[:space_idx]
    else:
        return s
