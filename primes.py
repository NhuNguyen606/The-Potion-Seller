import math

# def largest_prime(k: int) -> int:
#
#     factor_list = []
#     divisor = 2
#
#     while k >= 2:
#         flag = False
#         while k % divisor == 0:
#             flag = True
#             k /= divisor
#
#         if flag:
#             factor_list.append(divisor)
#
#     largest_prime_num = factor_list[-1]
#
#     return largest_prime_num

def is_prime(x: int) -> bool:
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            return False
    return True


def largest_prime(k: int) -> int:
    for i in range(k - 1, 1, -1):
        if is_prime(i):
            return i
    return


if __name__ == '__main__':
    print(str(largest_prime(27183)))
