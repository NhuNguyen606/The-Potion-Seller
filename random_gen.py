from typing import Generator

def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed

class RandomGen:
    
    def __init__(self) -> None:
        raise NotImplementedError()

    def randint(self, k: int) -> int:
        raise NotImplementedError()

if __name__ == "__main__":
    Random_gen = lcg(pow(2,32), 134775813, 1, 0)
