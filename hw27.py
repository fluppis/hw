def is_even(digit):
    """ Перевірка чи є парним число """
    x = divmod(digit,2)
    y = len(x) - 1
    j = x[y]
    if j == 0:
        return True
    else:
        return False
assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
assert is_even(44) == True, 'Test4'
assert is_even(1111) == False, 'Test5'
print('OK')