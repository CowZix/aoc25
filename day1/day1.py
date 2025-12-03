# Day 1
start_num = 50

def main():
    zeros = 0
    zero_cross = 0
    cur_num = start_num
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()

        if line[0] == 'R':
            move = int(line[1:])
        elif line[0] == 'L':
            move = -int(line[1:])
        else:
            move = 0

        zero_cross += cross_count(cur_num, move)
        cur_num = wrap(cur_num, move)

        if cur_num == 0:
            zeros += 1

    print(zeros, zero_cross)

def wrap(current: int, move: int)-> int:
    input = (current + move) % 100
    if (input < 0):
        output = input + 100
    else:
        output = input
    
    return output

def cross_count(current: int, move: int)-> int:
    count = 0
    for i in range(abs(move)):
        if move > 0:
            current += 1
        else:
            current -= 1
        current = wrap(current, 0)

        if current == 0:
            count += 1
    return count


if __name__ == "__main__":
    main()