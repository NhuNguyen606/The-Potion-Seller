def largest_prime(k: int) -> int:
    for i in range(1, k):
        x = k - i
        prime = True
        for j in range(2, int(x ** 0.5) + 1):
            if x % j == 0:
                prime = False
        if prime:
            return x
