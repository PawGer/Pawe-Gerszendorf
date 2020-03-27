def main():
    with open('plik.txt', 'r', encoding='UTF-8') as t:
        for i in t:
            print(i, "\n- ilość wyrazów:", len(i.split()))
if __name__ == "__main__":
    main()