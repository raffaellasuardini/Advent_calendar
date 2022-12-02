def main():
    with open('input.txt') as f:
        lines = f.read()
        calories = lines.split("\n")
        sum = 0
        elves = []

        for food in calories:
            if food == "":
                elves.append(sum)
                sum = 0
                continue
            sum += int(food)

        sorted_elves = sorted(elves, reverse=True)
        print(sorted_elves[0])
        top_three = sorted_elves[0:3]

        max_calories = 0
        for elf in top_three:
            max_calories += elf
        print(max_calories)


if __name__ == "__main__":
    main()
