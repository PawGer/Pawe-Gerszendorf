def main():
    from math import sqrt
    from itertools import count, islice
    zbior = list(range(50))
    print([n**2 for n in zbior if n > 1 and all(n % i for i in islice(count(2), int(sqrt(n))))])
if __name__ == '__main__':
    main()