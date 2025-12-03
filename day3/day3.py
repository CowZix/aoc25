# Day 3
def main():
    with open('test.txt', 'r') as file:
        banks = file.readlines()

    total = 0
    total2 = 0

    for bank in banks:
        bank = list(bank.strip())
        total += jolt(bank, 2)
        total2 += jolt(bank, 12)

    print(total, total2)

def jolt(bank: list, size: int)-> int:
    end = len(bank)
    maxi = bank.index(max(bank[:end-size+1]))
    jolt = f"{bank[maxi]}"
    for i in range(1,size):
        maxi2 = bank.index(max(bank[maxi+1:end-i+1]))
        jolt += bank[maxi2]

    return int(jolt)

if __name__ == "__main__":
    main()