# Day 1
start_num = 50

def main():
    zeros = 0
    zero_cross = 0
    cur_num = start_num
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        old_num = cur_num
        line = line.strip()
        if line[0] == 'R':
            cur_num += int(line[1:])
        elif line[0] == 'L':
            cur_num -= int(line[1:])
        cur_num, cross = fix(cur_num)
        zero_cross += cross
        print(line,":",old_num, "->", cur_num)
        if cur_num == 0:
            zeros += 1
            zero_cross += 1
        print("cross", cross)
    print(zeros, zero_cross)

def fix(input: int):
    zeros = abs(input) // 100
    output = input % 100
    if input > 99:
        output = input - 100
    elif (input < 0):
        zeros += 1
        output = input + 100
    else:
        output = input
    
    return output, zeros


if __name__ == "__main__":
    main()