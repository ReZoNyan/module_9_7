def decorator(func):
    def is_prime(*args):
        res = func(*args)
        count = 0
        for i in range(1, res + 1):
            if res % i == 0:
                count += 1
        if count == 2:
            print('Простое')
            return res
        else:
            return res

    return is_prime


@decorator
def sum_three(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


result = sum_three(2, 3, 6)
print(result)

result_2 = sum_three(5, 5, 3)
print(result_2)

print(sum_three(2, 3, 2))