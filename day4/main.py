def main():
    with open("assignments.txt") as f:
        lines = f.read()
    groups = [n.split(",") for n in lines.split("\n")]
    result = 0

    for sections in groups:
        first = sections[0].split('-')
        second = sections[1].split('-')

        if (int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1])) or (
                int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1])):
            result += 1

    print(result)

    # part 2

    second_result = 0
    for group in groups:
        min_first = int(group[0].split('-')[0])
        max_first = int(group[0].split('-')[1])
        min_second = int(group[1].split('-')[0])
        max_second = int(group[1].split('-')[1])
        first_array = [i for i in range(min_first, max_first+1)]
        second_array = [j for j in range(min_second, max_second+1)]


        if len(set(first_array).intersection(set(second_array))) >= 1:

            second_result += 1

    print(second_result)


if __name__ == "__main__":
    main()
