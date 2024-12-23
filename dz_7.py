def is_prime(func):
    def wrapper(*args):
        res_sum = func(*args)
        flag = True
        for i in range(2, res_sum):
            if res_sum % i == 0:
                flag = False
                break
        if flag:
            print('Простое')
        else:
            print('Составное')
        return res_sum
    return wrapper


@is_prime
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