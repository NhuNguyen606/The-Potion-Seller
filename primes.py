def largest_prime(k: int) -> int:

    factor_list = []
    divisor = 2

    while k >= 2:
        flag = False
        while k % divisor == 0:
            flag = True
            k /= divisor

        if flag:
            factor_list.append(divisor)

    largest_prime_num = factor_list[-1]

    return largest_prime_num




