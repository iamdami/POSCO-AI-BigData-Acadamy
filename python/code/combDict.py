def comb_dict(d1, d2):
    d1.update(d2)
    return d1

d1 = {'a': 1, 'b': 3, 'd': 7, 'e': 8}
d2 = {'a': 2, 'c': 4, 'e': 1}
d3 = comb_dict(d1, d2)
print(d3)
