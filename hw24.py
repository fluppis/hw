def difference(*args):
    lis_1 = []
    for li in args:
        lis_1.append(li)
    if not lis_1:
        return 0
    else:
        min_numb = min(lis_1)
        max_numb = max(lis_1)
        summary = max_numb - min_numb
        return round(summary, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
