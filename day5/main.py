import copy


def insert_crane(start_array, end_array):
    """

    :param end_array: list
    :type start_array: list
    """

    crane = start_array[0]
    start_array = start_array[1:]
    end_array.insert(0, crane)
    return start_array, end_array


def insert_crane_upgrade(start_array, end_array, n):
    group = start_array[:n]
    start_array = start_array[n:]
    for el in group[::-1]:
        end_array.insert(0, el)
    return start_array, end_array


def print_letters(array, l):
    top_letters = ''
    for i in range(1, l + 1):
        if len(array[i]) > 0:
            top_letters += array[i][0]
    return top_letters


def main():
    with open("cargo.txt", "r") as f:
        file = f.read()
        a, b = file.split("\n\n")
        moves = b.split("\n")
        cargos = a.split("\n")[:-1]
        length_cargos = int(a[-1])
        stacks = {}

    for lines in cargos:
        count_stack = 0

        for i in range(len(lines)):
            if i % 4 == 0:
                count_stack += 1

            if lines[i] != ' ' and lines[i] != '[' and lines[i] != ']':
                if count_stack not in stacks.keys():
                    stacks[count_stack] = []
                stacks[count_stack].append(lines[i])

    stacks2 = copy.deepcopy(stacks)
    operations = [el[5:].replace(" from ", "-").replace(" to ", "-").split("-") for el in moves]

    for i in range(len(operations)):
        m = int(operations[i][0])
        f = int(operations[i][1])
        t = int(operations[i][2])
        for _ in range(m):
            stacks[f], stacks[t] = insert_crane(stacks[f], stacks[t])

    print(print_letters(stacks, length_cargos))

    # part 2

    for i in range(len(operations)):
        m = int(operations[i][0])
        f = int(operations[i][1])
        t = int(operations[i][2])

        stacks2[f], stacks2[t] = insert_crane_upgrade(stacks2[f], stacks2[t], m)

    print(print_letters(stacks2, length_cargos))


if __name__ == "__main__":
    main()
