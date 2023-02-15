def get_min_max(l):
    min_val = max_val = l[0]
    for x in l:
        if min_val > x:
            min_val = x
        if max_val < x:
            max_val = x
    return min_val, max_val

l = [3, 5, 9, 1, 2]
min_val, max_val = get_min_max(l)
l.remove(min_val)
l.remove(max_val)

print(min_val)
print(max_val)
print(l)
print(get_min_max(l))
