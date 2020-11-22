def max_val(lst):
    max = None
    for num in lst:
        if max is None or num > max:
            max = num
    return max
