def get_total_calories_per_group():
    with open("input01.txt", "r") as f:
        total_calories_per_group = []
        group_calories = 0
        for line in f.readlines():
            if not line.strip():
                total_calories_per_group.append(group_calories)
                group_calories = 0
            else:
                group_calories = group_calories + int(line)
    return total_calories_per_group


def main():
    total_calories_per_group = sorted(get_total_calories_per_group())
    # Find the Elf carrying the most Calories
    print(total_calories_per_group[-1])
    # Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
    print(sum(total_calories_per_group[-3:]))  # second part


if __name__ == "__main__":
    main()
