#Day 6
def main():
    with open("test.txt", "r") as file:
        lines = [line.strip().split() for line in file.readlines()]

    transposed = list(zip(*lines[:-1]))
    total = 0
    for op in range(len(lines[-1])):
        if lines[-1][op] == '+':
            total += sum([int(i) for i in transposed[op]])
        elif lines[-1][op] == '*':
            p = 1
            for i in transposed[op]:
                p *= int(i)
            total += p
    
    print(total)
        
if __name__ == "__main__":
    main()