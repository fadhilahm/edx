def max_abs_val(lst):
    max_abs = None
    for num in lst:
        if max_abs is None or (num ** 2) ** 0.5 > max_abs:
            max_abs = int((num ** 2) ** 0.5)
    return max_abs
