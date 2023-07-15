def prime_generator(end):
    li1 = []
    for number in range(2, end + 1):
        no = True
        for k in li1:
            if k * k > number:
                break
            if number % k == 0:
                no = False
                break
        if no:
            li1.append(number)
            yield number


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
