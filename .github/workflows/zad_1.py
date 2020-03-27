def main():
    a = int(input("Podaj długość ściany: " ))
    b = int(input("Podaj długość ściany: " ))
    print("*" + "-" * b + "*")
    for z in range(0, a):
        print("|" + "*" * b + "|")
    print("*" + "-" * b + "*")
if __name__ == "__main__":
    main()
