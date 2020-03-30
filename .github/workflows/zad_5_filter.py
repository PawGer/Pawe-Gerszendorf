def main():
    from math import sqrt
    from itertools import count, islice
    zbior = list(range(50))
    print(list(filter(lambda n: n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1))),zbior)))
if __name__ == '__main__':
    main()