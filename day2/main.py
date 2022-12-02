def main():
    round_winner = {
        "Y": {
            "B": 3,
            "A": 6,
            "C": 0
        },
        "X": {
            "A": 3,
            "C": 6,
            "B": 0
        },
        "Z": {
            "C": 3,
            "B": 6,
            "A": 0
        }
    }

    with open("tournament.txt") as f:
        lines = f.read()
        round_game = lines.split("\n")[:-1]
        # score based on shape selected
        my_score = 0
        for el in round_game:
            if "Z" in el:
                my_score += 3
            elif "X" in el:
                my_score += 1
            else:
                my_score += 2

        for el in round_game:
            first = el[0]
            second = el[-1]
            my_score += round_winner[second][first]

        print(my_score)

    second_strategy = {
        "A": {
            "X": 3,
            "Y": 1,
            "Z": 2,
        },
        "B": {
            "X": 1,
            "Y": 2,
            "Z": 3,
        },
        "C": {
            "X": 2,
            "Y": 3,
            "Z": 1,
        }
    }

    second_score = 0
    for el in round_game:
        opponent = el[0]
        my_move = el[-1]

        if my_move == "Y":
            second_score += 3
        elif my_move == "Z":
            second_score += 6

        second_score += second_strategy[opponent][my_move]

    print(second_score)


if __name__ == "__main__":
    main()
