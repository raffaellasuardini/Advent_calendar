import string


def priority(letter):
    alphabet = list(string.ascii_letters)
    values = {letter: index + 1 for (index, letter) in enumerate(alphabet)}
    return int(values[letter])


def main():
    with open("sacs.txt") as f:
        stock = f.read().split("\n")

    total = 0

    for item in stock:
        half = int(len(item) / 2)
        first_half = item[:half]
        last_half = item[half:]

        for i in range(half):
            if first_half[i] in last_half:
                total += priority(first_half[i])
                break

    print(f"Solution part 1: {total}")

    # part 2
    solution = 0
    for i in range(0, len(stock), 3):
        first = stock[i]
        second = stock[i + 1]
        last = stock[i + 2]

        for j in range(len(first)):
            if (first[j] in second) and (first[j] in last):
                solution += priority(first[j])
                break

    print(f"Solution part 2: {solution}")


if __name__ == "__main__":
    main()
