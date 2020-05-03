def twoStrings(s1, s2):
    set1 = set(s1)
    set2 = set(s2)  
    if set1.intersection(set2):
        return 'YES'
    else:
        return 'NO'
