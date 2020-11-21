def isleapyear(year):
    verdict = None
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                verdict = True
            else:
                verdict = False
        else:
            verdict = True

    else:
        verdict = False
    return verdict
