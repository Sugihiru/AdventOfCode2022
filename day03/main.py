def split_rucksack_in_half(rucksack: str) -> tuple:
    return rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]


def get_priority(char: str):
    offset_char = "A"
    offset_value = 26
    if "a" <= char <= "z":
        offset_char = "a"
        offset_value = 0
    return ord(char) - ord(offset_char) + offset_value + 1


def get_common_items(*compartments: set[str]):
    return compartments[0].intersection(*compartments[1:])


def calculate_priority_sum_shared_items():
    priority_sum = 0
    with open("input01.txt", "r") as f:
        for line in f.readlines():
            compartments = split_rucksack_in_half(line.strip())
            common_item = get_common_items(
                set(compartments[0]), set(compartments[1])
            ).pop()
            priority_sum = priority_sum + get_priority(common_item)
    return priority_sum


def calculate_priority_sum_elves_group():
    priority_sum = 0
    with open("input01.txt", "r") as f:
        group_compartments: list[set[str]] = []
        for line in f.readlines():
            group_compartments.append(set(line.strip()))
            if len(group_compartments) == 3:
                common_item = get_common_items(*group_compartments).pop()
                priority_sum = priority_sum + get_priority(common_item)
                group_compartments = []
    return priority_sum


def main():
    print(calculate_priority_sum_shared_items())
    print(calculate_priority_sum_elves_group())


def tests():
    assert get_priority("b") == 2
    assert get_priority("B") == 28
    assert split_rucksack_in_half("abcdef") == ("abc", "def")


if __name__ == "__main__":
    # tests()
    main()
