def get_marker_idx(file_input: str) -> int:
    # part01
    # size_of_marker = 4
    # part02
    size_of_marker = 14
    idx = size_of_marker
    while idx < len(file_input):
        if len(set(file_input[idx - size_of_marker : idx])) == size_of_marker:
            return idx
        idx += 1
    raise RuntimeError("Marker not found")


def main():
    with open("input01.txt", "r") as f:
        file_input = f.read()
        print(get_marker_idx(file_input))


if __name__ == "__main__":
    main()
