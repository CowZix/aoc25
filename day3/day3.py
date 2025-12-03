# Day 3
def main():
    with open('input.txt', 'r') as file:
        banks = file.readlines()

    total = 0
    total2 = 0

    for bank in banks:
        bank = bank.strip()
        total += int(jolt(bank, 2, ""))
        total2 += int(jolt(bank, 12, ""))

    print(total, total2)

def jolt(bank: str, size: int, curr = ""):
    if size > len(bank):
        return None
    if size == 0:
        return curr
    if size == 1:
        return curr + max(bank)
    
    for d in "9876543210":
        if d in bank:
            i = bank.index(d)
            search = bank[i+1:]
            output = jolt(search, size -1, curr + d)
            if output is not None:
                return output

    

if __name__ == "__main__":
    main()