SHAPE_SCORE = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}


RPS_ELEMENTS = ["A", "B", "C"]
ORD_DIFF_ABC_XYZ = ord("X") - ord("A")


def abc_to_xyz(letter: str) -> str:
    return chr(ord(letter) + ORD_DIFF_ABC_XYZ)


def calculate_round_result_score(round_input: list[str]):
    match round_input:
        case [x, y] if abc_to_xyz(x) == y:
            return 3
        case ["A", "Y"] | ["B", "Z"] | ["C", "X"]:
            return 6
        case _:
            return 0


def change_round_input(round_input) -> list:
    match round_input:
        case [x, "X"]:
            return [x, abc_to_xyz(RPS_ELEMENTS[(RPS_ELEMENTS.index(x) - 1)])]
        case [x, "Y"]:
            return [x, abc_to_xyz(x)]
        case [x, "Z"]:
            return [
                x,
                abc_to_xyz(
                    RPS_ELEMENTS[(RPS_ELEMENTS.index(x) + 1) % len(RPS_ELEMENTS)]
                ),
            ]
        case _:
            raise RuntimeError("Unknown case")


def calculate_score():
    score = 0
    with open("input01.txt", "r") as f:
        for line in f.readlines():
            # Part 1
            # round_input = line.strip().split(" ")
            # Part 2
            round_input = change_round_input(line.strip().split(" "))
            score = (
                score
                + calculate_round_result_score(round_input)
                + SHAPE_SCORE[round_input[1]]
            )
    return score


def main():
    print(calculate_score())


if __name__ == "__main__":
    main()
