#Day 5
def main():
    with open("input.txt", "r") as file:
        (ranges, ids) = file.read().split('\n\n')
    ranges = ranges.split('\n')
    ids = ids.split('\n')

    count1 = 0
    for id in ids:
        if in_range(ranges, int(id)):
            count1 += 1
    
    
    known_ranges = set()
    for r in ranges:
        start, end = r.split('-')
        new_range = list(range(int(start), int(end)))
        known_ranges.update(new_range)
    
    count2 = len(known_ranges)+2

    print(count1,count2)
        

def in_range(ranges, id:int) -> bool:
    for r in ranges:
        start, end = r.split('-')
        if int(start) <= id <= int(end):
            return True
    return False

if __name__ == "__main__":
    main()
