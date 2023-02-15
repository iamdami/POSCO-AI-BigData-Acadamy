가변인자
def diff(a, b, *n):
    l = [a, b, *n]
    c = max(l) - min(l)
    return c

print(diff(1, 2, 3, 4, 5))
print(diff(-100, 200))
