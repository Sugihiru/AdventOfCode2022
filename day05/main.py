import re

# move 5 from 4 to 9
INSTRUCTION_REGEX = re.compile(r"move (\d+) from (\d+) to (\d+)")


def process_stack_input(stacks_input: list[str]) -> list[list[str]]:
    stacks: list[list[str]] = []

    elements_index: list[int] = []
    for idx, char in enumerate(stacks_input[0]):
        if char.isalpha():
            elements_index.append(idx)

    for _ in range(len(elements_index)):
        stacks.append([])

    for line in stacks_input:
        for stack_idx, element_index in enumerate(elements_index):
            if line[element_index].isalpha():
                stacks[stack_idx].append(line[element_index])

    return stacks


def process_instruction(stacks: list[list[str]], instruction: str):
    match = INSTRUCTION_REGEX.match(instruction)
    assert match is not None

    nb_crates_to_move, source_crate_idx, destination_crate_idx = (
        int(match.group(1)),
        int(match.group(2)) - 1,
        int(match.group(3)) - 1,
    )

    # part 01
    # for _ in range(nb_crates_to_move):
    #     try:
    #         stacks[destination_crate_idx].append(stacks[source_crate_idx][-nb_crates_to_move])
    #     except IndexError:
    #         continue

    # part 02
    stacks[destination_crate_idx] += stacks[source_crate_idx][-nb_crates_to_move:]
    stacks[source_crate_idx] = stacks[source_crate_idx][:-nb_crates_to_move]


def get_top_crates(stacks: list[list[str]]):
    return "".join(x[-1] for x in stacks if x)


def main():
    with open("input01.txt", "r") as f:
        stacks = []
        stacks_input = []
        for line in f:
            # Process the first part of the input by building the stacks
            if not stacks:
                if line.strip():
                    stacks_input.append(line)
                else:
                    stacks_input = stacks_input[:-1]
                    stacks_input.reverse()
                    stacks = process_stack_input(stacks_input)
            else:
                process_instruction(stacks, line.strip())
    print(get_top_crates(stacks))


if __name__ == "__main__":
    main()
