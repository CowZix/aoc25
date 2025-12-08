# Day 4
import copy


def main():
    cells = []
    count1 = 0
    count2 = 0
    with open("input.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        cells.append(list(line.strip()))

    count1 = check_cells(cells)[0]

    while check_cells(cells)[0] > 0:
        count2 += check_cells(cells)[0]
        cells = check_cells(cells)[1]

    print(count1, count2)


def check_cells(cells):
    new_cells = copy.deepcopy(cells)
    count = 0
    for r in range(len(cells)):
        for c in range(len(cells[0])):
            if cells[r][c] == "@" and count_neighbors(r, c, cells):
                count += 1
                new_cells[r][c] = "."

    return count, new_cells


def count_neighbors(r: int, c: int, cells: list[list[str]]) -> bool:
    count = 0
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in offsets:
        dr, dc = r + dr, c + dc
        if 0 <= dr < len(cells) and 0 <= dc < len(cells[0]):
            if cells[dr][dc] == "@":
                count += 1
    return count < 4


if __name__ == "__main__":
    main()
