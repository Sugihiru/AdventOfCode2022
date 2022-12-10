def read_line(line: str) -> list[tuple[int, int]]:
    pairs = []
    for pair in line.split(","):
        sectors = pair.split("-")
        pairs.append((int(sectors[0]), int(sectors[1])))
    return pairs


def is_fully_contained(
    first_group: tuple[int, int], second_group: tuple[int, int]
) -> bool:
    return (
        first_group[0] >= second_group[0] and first_group[1] <= second_group[1]
    ) or (second_group[0] >= first_group[0] and second_group[1] <= first_group[1])


def overlaps(first_group: tuple[int, int], second_group: tuple[int, int]):
    return (
        second_group[0] <= first_group[0] <= second_group[1]
        or first_group[0] <= second_group[0] <= first_group[1]
    )


def calculate_nb_contained_sections() -> int:
    nb_contained_sections = 0
    with open("input01.txt", "r") as f:
        for line in f:
            line_input = read_line(line)
            # part01
            # nb_contained_sections += int(
            #     is_fully_contained(line_input[0], line_input[1])
            # )
            # part02
            nb_contained_sections += int(overlaps(line_input[0], line_input[1]))
    return nb_contained_sections


def main():
    print(calculate_nb_contained_sections())


def tests():
    assert read_line("7-50,8-33") == [(7, 50), (8, 33)]
    assert is_fully_contained((7, 50), (8, 33)) == True
    assert overlaps((2, 8), (3, 7)) == True


if __name__ == "__main__":
    # tests()
    main()
