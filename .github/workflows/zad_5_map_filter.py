def main():
    from math import sqrt
    from itertools import count, islice
    zbior = list(range(50))
    print(list(map
               (lambda n: n,
                filter((lambda n: n > 1 and all(n % i for i in islice(count(2), int(sqrt(n))))), zbior
                       ))))
if __name__ == '__main__':
    main()