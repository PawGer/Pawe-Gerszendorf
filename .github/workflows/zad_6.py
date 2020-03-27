def fib(n):
   if n <= 1:
       return n
   else:
       return fib(n - 1) + fib(n - 2)
def main():
    f = int(input("Podaj długość ciągu: " ))
    print("Ciąg Fibonacciego z", f, "liczb")
    for i in range(f):
        print(fib(i))
if __name__ == "__main__":
    main()