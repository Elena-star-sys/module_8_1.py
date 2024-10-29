def add_everything_up(a, b):
    try:
        if (isinstance(a, int, float) and isinstance(a, str) and isinstance(b, int), float and isinstance(b, str)):
            return a + b
    except TypeError as exc:
        return str(a) + str(b)



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))



