#Day 2
import re

def main():
    with open('input.txt', 'r') as file:
        ranges = file.read().strip().split(',')

    total = 0
    total_2 = 0
    for r in ranges:
        start, end = r.split('-')
        for id in range(int(start), int(end)+1):
            if re.search(r"^(\d+)(?=\1$)", str(id)):
                total += id
            if re.search(r"^(\d+)(?=\1+$)", str(id)):
                total_2 += id

    print(total, total_2)


if __name__ == "__main__":
    main()