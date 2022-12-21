def find_marker(datastream, n):
    for i in range(len(datastream)):
        marker = set(datastream[i:i + n])

        if len(marker) == n:
            return i + n


def main():
    with open('data.txt') as f:
        lines = f.read()

    print(find_marker(lines, 4))
    print(find_marker(lines, 14))


if __name__ == '__main__':
    main()
